import numpy as np

from main.DRIVE.src.controllers.drive import DRIVE
from main.DRIVE.src.utils import get_param_or_default


class ResponseMisreportingDrive(DRIVE):

    def __init__(self, params):
        super(ResponseMisreportingDrive, self).__init__(params)
        self.misreporting_agents_ratio = get_param_or_default(params, "misreporting_agents_ratio", 0.2)
        self.misreporting_agents_estimate_relative = get_param_or_default(params, "misreporting_agents_estimate_relative", 0.9)
        self.rng = np.random.default_rng(1234)

    def update_token_value(self, i, neighborhood):
        is_misreporting = self.rng.random() < self.misreporting_agents_ratio
        if is_misreporting:
            # set own estimate slightly smaller than the minimal reward sent in the request
            min_request = self.trust_request_matrix[neighborhood, i].min()
            perc_factor = self.misreporting_agents_estimate_relative if min_request >= 0 else 1 - self.misreporting_agents_estimate_relative
            own_estimate = self.trust_request_matrix[neighborhood, i].min() * perc_factor
        else:
            own_estimate = np.mean(self.reward_buffer[:, i])
        neighborhood_size = len(neighborhood) * 1.0
        if neighborhood_size > 0:
            # Track all the reward differences according to Algorithm 2
            self.tracked_deltas[i] += np.mean(own_estimate - self.trust_request_matrix[neighborhood, i])