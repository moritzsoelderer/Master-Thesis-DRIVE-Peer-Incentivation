import numpy as np

from main.DRIVE.src.controllers.drive import DRIVE
from main.DRIVE.src.utils import get_param_or_default


class NoisyResponseMisreportingDrive(DRIVE):

    def __init__(self, params):
        super(NoisyResponseMisreportingDrive, self).__init__(params)
        self.misreporting_agents_ratio = get_param_or_default(params, "misreporting_agents_ratio", 0.2)
        self.noise_perc = get_param_or_default(params, "noise_perc", 0.25)

    def update_token_value(self, i, neighborhood):
        is_misreporting = np.random.rand() < self.misreporting_agents_ratio
        if is_misreporting:
            # set own estimate to the minimal reward sent in the request
            mean = np.mean(self.reward_buffer[:, i])
            scale = self.noise_perc * reward_range # implement way to find reward range
            own_estimate = mean + np.random.normal(loc=0, scale=scale) # add gaussian noise
        else:
            own_estimate = np.mean(self.reward_buffer[:, i])
        neighborhood_size = len(neighborhood) * 1.0
        if neighborhood_size > 0:
            # Track all the reward differences according to Algorithm 2
            self.tracked_deltas[i] += np.mean(own_estimate - self.trust_request_matrix[neighborhood, i])