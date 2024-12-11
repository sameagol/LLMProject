# AMD GPU Setup for Llama with ROCm

## Useful Links
- [LLM Tracker: AMD GPUs](https://llm-tracker.info/howto/AMD-GPUs#windows)
- [Visual Studio](https://visualstudio.microsoft.com/vs/)
- [CMake](https://cmake.org/download/)
- [Clang](https://clang.llvm.org/get_started.html)

## Installation Steps
1. **Install Visual Studio**  
   Download and install from [Visual Studio](https://visualstudio.microsoft.com/vs/).
   
2. **Install CMake**  
   Download and install from [CMake](https://cmake.org/download/).

3. **Install Clang**  
   Follow the steps on [Clang's website](https://clang.llvm.org/get_started.html).  
   - Be cautious of differences in Visual Studio versions.  
   - If successful, an `LLVM.sln` file will be created in the build directory.

4. **Install Perl (Optional)**  

---

## CMake Commands

Run the following commands based on your configuration:

### For `gfx1100` Target
```bash
cmake.exe .. -G "Visual Studio 17 2022" -DCMAKE_BUILD_TYPE=Release -DLLAMA_HIPBLAS=on -DCMAKE_C_COMPILER="C:\Program Files\AMD\ROCm\5.7\bin\clang.exe" -DCMAKE_CXX_COMPILER="C:\Program Files\AMD\ROCm\5.7\bin\clang++.exe" -DAMDGPU_TARGETS="gfx1100" -DCMAKE_PREFIX_PATH="C:\Program Files\AMD\ROCm\5.7" -DHIP_PLATFORM=hcc
cmake.exe .. -G "Visual Studio 17 2022" -DCMAKE_BUILD_TYPE=Release -DLLAMA_HIPBLAS=on -DCMAKE_C_COMPILER="C:\Program Files\AMD\ROCm\5.7\bin\clang.exe" -DCMAKE_CXX_COMPILER="C:\Program Files\AMD\ROCm\5.7\bin\clang++.exe" -DAMDGPU_TARGETS="gfx1100" -DCMAKE_PREFIX_PATH="C:\Program Files\AMD\ROCm\5.7" -DHIP_PLATFORM=hcc
cmake.exe .. -G "Visual Studio 17 2022" -DCMAKE_BUILD_TYPE=Release -DLLAMA_HIPBLAS=on -DCMAKE_C_COMPILER="C:\\Program Files\\AMD\\ROCm\\5.7\\bin\\clang.exe" -DCMAKE_CXX_COMPILER="C:\\Program Files\\AMD\\ROCm\\5.7\\bin\\clang++.exe" -DAMDGPU_TARGETS="gfx1030" -DCMAKE_PREFIX_PATH="C:\\Program Files\\AMD\\ROCm\\5.7" -DHIP_PLATFORM=hcc
cmake.exe .. -G "Visual Studio 17 2022" -DCMAKE_BUILD_TYPE=Release -DLLAMA_HIPBLAS=on -DCMAKE_C_COMPILER="C:\\Program Files\\AMD\\ROCm\\5.7\\bin\\clang.exe" -DCMAKE_CXX_COMPILER="C:\\Program Files\\AMD\\ROCm\\5.7\\bin\\clang++.exe" -DAMDGPU_TARGETS="gfx1030" -DCMAKE_PREFIX_PATH="C:\\Program Files\\AMD\\ROCm\\5.7"
cmake.exe .. -G "Visual Studio 17 2022" -DCMAKE_BUILD_TYPE=Release -DLLAMA_HIPBLAS=on -DCMAKE_C_COMPILER="C:\\Program Files\\AMD\\ROCm\\5.7\\bin\\clang.exe" -DCMAKE_CXX_COMPILER="C:\\Program Files\\AMD\\ROCm\\5.7\\bin\\clang++.exe" -DAMDGPU_TARGETS="gfx1030" -DCMAKE_PREFIX_PATH="C:\\Program Files\\AMD\\ROCm\\5.7\\bin" -DHIP_PATH="C:\\Program Files\\AMD\\ROCm\\5.7\\bin"

CC=C:\\Program Files\\AMD\\ROCm\\5.7\\bin\\clang CXX=C:\\Program Files\\AMD\\ROCm\\5.7\\bin\\clang++ cmake .. -DLLAMA_HIPBLAS=ON -DLLAMA_CUDA_DMMV_X=64 -DLLAMA_CUDA_MMV_Y=2

cmake .. -DLLAMA_HIPBLAS=ON -DLLAMA_CUDA_DMMV_X=64 -DLLAMA_CUDA_MMV_Y=2 CC=C:\\Program Files\\AMD\\ROCm\\5.7\\bin\\clang CXX=C:\\Program Files\\AMD\\ROCm\\5.7\\bin\\clang++

set PATH=%PATH%;C:\Program Files\AMD\ROCm\5.7\bin
set HIP_PATH=C:\Program Files\AMD\ROCm\5.7\hip
set ROCM_PATH=C:\Program Files\AMD\ROCm\5.7
cmake.exe --build .
```