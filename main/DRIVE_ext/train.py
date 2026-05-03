import random
import sys

import joblib
import numpy as np
import torch
from joblib import delayed

from main.DRIVE.src import domains, data, experiments
from main.DRIVE_ext.settings import params
from main.DRIVE_ext.src import algorithms

params["domain_name"] = sys.argv[1]
params["algorithm_name"] = sys.argv[2]
drift_function_name = sys.argv[3]
params["drift_function"] = domains.drift_function(drift_function_name)

suffix = ''
if len(sys.argv) > 4:
    if "UNSTABLE-COMMUNICATION" in params["algorithm_name"]:
        params["failing_communication_ratio"] = float(sys.argv[4])
        suffix = '_' + str(params["failing_communication_ratio"]) + '_'
        print("UNSTABLE-COMMUNICATION " + suffix)
    elif "RESPONSE-MISREPORTING" in params["algorithm_name"]:
        params["misreporting_agents_ratio"] = float(sys.argv[4])
        params["misreporting_agents_estimate_relative"] = float(sys.argv[5])
        suffix = '_' + str(params["misreporting_agents_ratio"]) + '_' + str(params["misreporting_agents_estimate_relative"]) + '_'
        print("RESPONSE-MISREPORTING " + suffix)

"""
seed = 1234
np.random.seed(seed)
torch.manual_seed(seed)
random.seed(seed)

env = domains.make(params)
env.reset()
controller = algorithms.make(params)

params["directory"] = params["output_folder"] + "/" + (params["data_prefix_pattern"] + suffix). \
    format(
    params["nr_agents"], \
    params["domain_name"], \
    drift_function_name, \
    params["algorithm_name"])
params["directory"] = data.mkdir_with_timestap(params["directory"])
experiments.run_training(env, controller, params)

"""
def execute_in_parallel(seed, params, suffix):
    np.random.seed(seed)
    torch.manual_seed(seed)
    random.seed(seed)

    suffix += f"_seed_{seed}_"

    env = domains.make(params)
    env.reset()
    controller = algorithms.make(params)

    params["directory"] = params["output_folder"] + "/" + (params["data_prefix_pattern"] + suffix). \
        format(
        params["nr_agents"], \
        params["domain_name"], \
        drift_function_name, \
        params["algorithm_name"])
    params["directory"] = data.mkdir_with_timestap(params["directory"])
    experiments.run_training(env, controller, params)


print("Epochs", params["nr_epochs"])

joblib.Parallel(n_jobs=8, verbose=50)(delayed(execute_in_parallel)(seed, params, suffix) for seed in range(1, 9))
