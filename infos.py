import torch
import platform
import psutil
import platform

print(platform.processor())
print("OS:", platform.platform())
print("Python:", platform.python_version())
print("PyTorch:", torch.__version__)
print("CUDA:", torch.version.cuda)
print("cuDNN:", torch.backends.cudnn.version())
print("GPU:", torch.cuda.get_device_name(0))
print("VRAM:", round(torch.cuda.get_device_properties(0).total_memory / 1024**3, 2), "GB")
print("RAM:", round(psutil.virtual_memory().total / 1024**3, 2), "GB")