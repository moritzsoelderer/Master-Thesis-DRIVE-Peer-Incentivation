import torch

CPU_DEVICE = "cpu"
GPU_DEVICE = "gpu"
MPS_DEVICE = "mps"

device_type = CPU_DEVICE
device = torch.device(device_type)
print(f"Using device: {device}")

params = {}
params["episodes_per_epoch"] = 10
params["nr_epochs"] = 1000
params["nr_hidden_units"] = 64
params["clip_norm"] = 1
params["learning_rate"] = 0.001
params["output_folder"] = "output"
params["data_prefix_pattern"] = "{}-agents_domain-{}_drift-{}_{}"
params["torch_device"] = device

## additional (moritz)
params["failing_communication_ratio"] = 0.1
params["misreporting_agents_ratio"] = 0.1
params["misreporting_agents_estimate_relative"] = 0.9