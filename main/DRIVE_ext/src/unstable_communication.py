import numpy as np

from main.DRIVE.src.controllers.drive import DRIVE
from main.DRIVE.src.utils import get_param_or_default


class UnstableCommunicationDRIVE(DRIVE):
    def __init__(self, params):
        super(UnstableCommunicationDRIVE, self).__init__(params)
        self.failing_communication_ratio = get_param_or_default(params, "failing_communication_ratio", 0.2)

    def prepare_transition(self, joint_histories, joint_action, rewards, next_joint_histories, done, info):
        for neighborhood in info["neighbor_agents"]:
            to_remove = [i for i in range(len(neighborhood)) if np.random.rand() < self.failing_communication_ratio]
            for index in reversed(to_remove): # reversed to prevent index out of bounds errors
                neighborhood.pop(index)

        return super(UnstableCommunicationDRIVE, self).prepare_transition(joint_histories, joint_action, rewards, next_joint_histories, done, info)