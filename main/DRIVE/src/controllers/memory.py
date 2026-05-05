import numpy
import torch


class ExperienceMemory:
    def __init__(self, params, agent_id, device):
        self.device = device
        self.agent_id = agent_id
        self.episode_buffer = []
        self.nr_episodes = params["episodes_per_epoch"]
        self.episode_count = 0
        self.episode_time_limit = params["time_limit"]
        self.gamma = params["gamma"]
        self.eps = numpy.finfo(numpy.float32).eps.item()
        self.abs_incentive_cost = torch.zeros(1, dtype=torch.float32, device=device)

        # pre-allocate buffers
        max_steps = self.nr_episodes * self.episode_time_limit
        self.history_dim = params["observation_dim"] * params["history_length"]
        self.nr_actions = params["nr_actions"]
        self.nr_agents = params["nr_agents"]

        self.histories = torch.zeros((max_steps, params["history_length"], params["observation_dim"]), dtype=torch.float32, device=device)
        self.next_histories = torch.zeros_like(self.histories)
        self.returns = torch.zeros(max_steps, dtype=torch.float32, device=device)
        self.extrinsic_returns = torch.zeros(max_steps, dtype=torch.float32, device=device)
        self.rewards = torch.zeros(max_steps, dtype=torch.float32, device=device)
        self.actions = torch.zeros(max_steps, dtype=torch.long, device=device)
        self.old_probs = torch.zeros((max_steps, self.nr_actions), dtype=torch.float32, device=device)
        self.dones = torch.zeros(max_steps, dtype=torch.float32, device=device)
        self.incentive_rewards = torch.zeros((max_steps, self.nr_agents), dtype=torch.float32, device=device)
        self.ptr = 0  # current write index

    def save(self, new_transition):
        self.episode_buffer.append(new_transition)
        assert len(self.episode_buffer) <= self.episode_time_limit

        if new_transition["done"]:
            self.episode_count += 1
            return_value = 0.0
            extrinsic_return_value = 0.0
            local_abs_incentive_cost = torch.zeros(1, dtype=torch.float32, device=self.device)

            episode_len = len(self.episode_buffer)
            episode_start = self.ptr

            for transition in reversed(self.episode_buffer):
                i = self.ptr
                return_value = transition["rewards"][self.agent_id] + self.gamma * return_value
                extrinsic_return_value = transition["extrinsic_rewards"][self.agent_id] + self.gamma * extrinsic_return_value
                incentive_reward = transition["incentive_rewards"][self.agent_id]
                local_abs_incentive_cost = incentive_reward.exp().abs().sum() + self.gamma * local_abs_incentive_cost

                self.histories[i] = transition["joint_histories"][self.agent_id]
                self.next_histories[i] = transition["next_joint_histories"][self.agent_id]
                self.returns[i] = return_value
                self.extrinsic_returns[i] = extrinsic_return_value
                self.rewards[i] = transition["rewards"][self.agent_id]
                self.actions[i] = transition["joint_action"][self.agent_id]
                self.old_probs[i] = transition["joint_old_probs"][self.agent_id]
                self.dones[i] = transition["done"]
                self.incentive_rewards[i] = incentive_reward
                self.ptr += 1

            self.episode_buffer.clear()
            self.abs_incentive_cost += local_abs_incentive_cost

    def get_training_data(self):
        n = self.ptr
        returns = self.returns[:n]

        # normalize returns
        mu = returns.mean()
        sigma = returns.std()
        returns = (returns - mu) / (sigma + self.eps)

        return (
            self.histories[:n],
            self.next_histories[:n],
            self.actions[:n],
            self.rewards[:n],
            returns,
            self.old_probs[:n],
            self.dones[:n],
            self.incentive_rewards[:n],
        )

    def get_extrinsic_returns(self):
        return self.extrinsic_returns[:self.ptr]

    def get_incentive_rewards_for(self, j):
        return self.incentive_rewards[:self.ptr, j]

    def is_full(self):
        return self.episode_count >= self.nr_episodes

    def clear(self):
        self.episode_count = 0
        self.ptr = 0
        self.abs_incentive_cost = torch.zeros(1, dtype=torch.float32, device=self.device)
        self.episode_buffer.clear()
        # no need to zero out tensors — ptr tracks valid range