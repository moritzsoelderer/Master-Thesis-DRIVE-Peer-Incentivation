import numpy as np

from main.DRIVE.src.controllers.drive import DRIVE


class AdversarialAgentDrive(DRIVE):

    def __init__(self, params):
        super(AdversarialAgentDrive, self).__init__(params)
        self.num_adversarial_agents = int(params["num_adversarial_agents"])
        assert self.num_adversarial_agents <= params["nr_agents"]
        self.adversarial_agents_indices = list(range(self.num_adversarial_agents))

    def update_token_value(self, i, neighborhood):
        if i in self.adversarial_agents_indices:
            # set own estimate to the minimal reward sent in the request
            own_estimate = self.trust_request_matrix[neighborhood, i].min()
        else:
            own_estimate = np.mean(self.reward_buffer[:, i])
        neighborhood_size = len(neighborhood) * 1.0
        if neighborhood_size > 0:
            # Track all the reward differences according to Algorithm 2
            self.tracked_deltas[i] += np.mean(own_estimate - self.trust_request_matrix[neighborhood, i])