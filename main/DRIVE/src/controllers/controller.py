import numpy
import torch
from os.path import join

from main.DRIVE.src.controllers.memory import ExperienceMemory
from main.DRIVE.src.utils import get_param_or_default

"""
 Skeletal implementation of a (multi-agent) controller.
"""
class Controller:

    def __init__(self, params):
        self.comm_failure_prob = get_param_or_default(params, "comm_failure_prob", 0)
        self.failure_start_epoch = get_param_or_default(params, "failure_start_epoch", 0)
        self.current_epoch = 0
        self.nr_agents = params["nr_agents"]
        self.clip_norm = get_param_or_default(params, "clip_norm", 1)
        self.nr_actions = params["nr_actions"]
        self.gamma = params["gamma"]
        self.learning_rate = params["learning_rate"]
        self.history_length = params["history_length"]
        self.device = get_param_or_default(params, "torch_device", torch.device("cpu"))
        self.observation_dim = params["observation_dim"]
        self.input_dim = int(self.observation_dim*self.history_length)
        self.eps = numpy.finfo(numpy.float32).eps.item()
        self.actions = torch.tensor(list(range(self.nr_actions)), device=self.device)
        self.joint_histories = self.reset_joint_histories()
        self.actor_nets = []
        self.critic_nets = []
        self.token_values = torch.zeros(self.nr_agents, device=self.device)
        self.joint_old_probs = torch.zeros((self.nr_agents, self.nr_actions), device=self.device)
        self.R_max = get_param_or_default(params, "R_max", 3)
        self.memories = [ExperienceMemory(params, i, self.device) for i in range(self.nr_agents)]

    def reset_joint_histories(self):
        return torch.zeros(
            (self.nr_agents, self.history_length, self.observation_dim),
            dtype=torch.float32,
            device=self.device
        )

    def update_joint_histories(self, observations):
        self.joint_histories = torch.roll(self.joint_histories, -1, dims=1)
        self.joint_histories[:, -1, :] = observations
        return self.joint_histories

    def save_model_weights(self, path):
        for i, actor_net, critic_net in zip(range(len(self.actor_nets)), self.actor_nets, self.critic_nets):
            self.save_model_weights_of(path, actor_net, "actor_net_{}.pth".format(i))
            self.save_model_weights_of(path, critic_net, "critic_net_{}.pth".format(i))

    def load_model_weights(self, path):
        for i, actor_net, critic_net in zip(range(len(self.actor_nets)), self.actor_nets, self.critic_nets):
            self.load_model_weights_of(path, actor_net, "actor_net_{}.pth".format(i))
            self.load_model_weights_of(path, critic_net, "critic_net_{}.pth".format(i))

    def save_model_weights_of(self, path, network_model, filename):
        path = join(path, filename)
        torch.save(network_model.state_dict(), path)

    def load_model_weights_of(self, path, network_model, filename):
        path = join(path, filename)
        network_model.load_state_dict(torch.load(path, map_location=self.device))
        network_model.eval()
    
    def policy(self, observations):
        assert len(observations) == self.nr_agents,\
            "Expected {}, got {}".format(len(observations), self.nr_agents)
        observations = torch.as_tensor(numpy.array(observations), dtype=torch.float32, device=self.device)
        joint_probs = []
        joint_action = []
        self.joint_histories = self.update_joint_histories(observations)
        for i in range(self.nr_agents):
            probs = self.local_probs(self.joint_histories[i], i)
            joint_probs.append(probs)
            indices = torch.multinomial(probs, num_samples=1, replacement=True)
            self.joint_old_probs[i] = probs
            joint_action.append(self.actions[indices])
        return joint_action, joint_probs

    def local_probs(self, history, agent_id):
        return torch.ones(self.nr_actions, device=self.device)*1.0/self.nr_actions

    def update(self, observations, joint_action, rewards, next_observations, done, info):
        joint_histories = self.joint_histories
        next_observations = torch.as_tensor(numpy.array(next_observations), dtype=torch.float32, device=self.device)
        next_joint_histories = self.update_joint_histories(next_observations)
        transition = self.prepare_transition(joint_histories, joint_action, rewards, next_joint_histories, done, info)
        is_full = False
        for memory in self.memories:
            memory.save(transition)
            is_full = is_full or memory.is_full()
        if is_full:
            self.update_step()
            self.current_epoch += 1
        if done:
            self.joint_histories = self.reset_joint_histories()
        return transition
        
    def prepare_transition(self, joint_histories, joint_action, rewards, next_joint_histories, done, info):
        return {
            "joint_histories" : joint_histories,
            "joint_action": joint_action,
            "rewards": rewards,
            "extrinsic_rewards": rewards,
            "incentive_rewards": [torch.zeros(self.nr_agents, dtype=torch.float32, device=self.device) for _ in range(self.nr_agents)],
            "next_joint_histories": next_joint_histories,
            "done": done,
            "joint_old_probs": self.joint_old_probs,
            "request_messages_sent": 0,
            "response_messages_sent": 0}

    def update_step(self):
        pass
