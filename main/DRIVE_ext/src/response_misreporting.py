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
        own_estimate = np.mean(self.reward_buffer[:, i])
        misreporting_agents = [j for j in range(len(neighborhood)) if self.rng.random() < self.misreporting_agents_ratio]
        for j in misreporting_agents:
            self.trust_request_matrix[j, i] = own_estimate * self.misreporting_agents_estimate_relative

        super(DRIVE, self).update_token_value(i, neighborhood)