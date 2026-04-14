from main import actor_critic, lio, inequity_aversion, mate, drive, controller
from main import unstable_communication

def make(params):
    algorithm_name = params["algorithm_name"]
    if algorithm_name == "Random":
        return controller.Controller(params)
    if algorithm_name == "IAC":
        return actor_critic.ActorCritic(params)
    if algorithm_name.startswith("LIO"):
        return lio.LIO(params)
    if algorithm_name.startswith("IA"):
        return inequity_aversion.InequityAversion(params)
    if algorithm_name.startswith("MATE-TD"):
        params["mate_mode"] = "td_error"
        return mate.MATE(params)
    if algorithm_name.startswith("DRIVE-TD-UNSTABLE-COMMUNICATION"):
        params["mate_mode"] = "td_error"
        return unstable_communication.UnstableCommunicationDRIVE(params)
    if algorithm_name.startswith("DRIVE-TD"):
        params["mate_mode"] = "td_error"
        return drive.DRIVE(params)
    raise ValueError("Unknown algorithm '{}'".format(algorithm_name))