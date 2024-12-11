# ROCm on WSL: Issues and Observations

## Why It Didn't Work

1. **Hardware Access**
   - **Direct Hardware Access**: ROCm needs direct access to the GPU hardware to function correctly. WSL acts as an abstraction layer over Windows, which complicates direct hardware interfacing. While recent updates to WSL have started to include some GPU compute capabilities via NVIDIA CUDA (WSLg), AMD GPU support through ROCm in WSL isn't officially documented or supported.
   - **GPU Pass-through**: Unlike native Linux, where the OS has direct access to the hardware, WSL does not support GPU pass-through in a way that ROCm can utilize AMD GPUs fully.

2. **Driver Support**
   - **AMD Drivers**: ROCm on Linux requires specific drivers that interact with the kernel and the hardware. These drivers are not available or functional within the WSL environment because they require a level of integration with the system and hardware that WSL currently does not provide.

---

## WSL Commands

### Kernel Version
```bash
> uname -r
5.15.146.1-microsoft-standard-WSL2
> df -T /
Filesystem     Type  1K-blocks     Used Available Use% Mounted on
/dev/sdc       ext4 1055762868 29263924 972795472   3% /
```

Prereqs:
 * WSL Ubuntu 22
 * sudo apt update
 * sudo apt upgrade

To activate python environment I made:
. venv/bin/activate
