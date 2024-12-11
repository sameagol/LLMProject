'''
./main -m C:\PythonParaphanalia\Models\mistral-7b-instruct-v0.2.Q4_K_M.gguf --color --temp 0.8 --top_k 40 --top_p 0.95 --ctx_size 2048 --n_predict -1 --keep -1 -p "[INST] I have a headache, nausea, and I recently got my finger amputated. I don't have any pharmaceuticals, what herbal remedies will help me?[/INST]"


'''

a = 1

from llama_cpp import Llama

pre = '<s>[INST] '
prompt = "I have a headache, nausea, and I recently got my finger amputated. I don't have any pharmaceuticals, what herbal remedies will help me?"
post = '[/INST]'

llm = Llama(
    model_path=r'C:\PythonParaphanalia\Models\mistral-7b-instruct-v0.2.Q4_K_M.gguf',
    n_gpu_layers=99,
    n_ctx=2048
)

output = llm(
    pre + prompt + post,
    # stop=["Q:", "\n"],  # Stop generating just before the model would generate a new question
    max_tokens=None,
    echo=True,  # Echo the prompt back in the output
    temperature=0.8,
    # top_k=40,
    # top_p=0.95,
    # color = True,
    # n_predict = -1,  # Assuming -1 stands for predicting until a certain end token or similar
    # keep = -1  # This would need to be defined according to the API's documentation
)

print(output['choices'])



'''
pip install llama-cpp-python -C cmake.args="-DLLAMA_BLAS=ON;-DLLAMA_BLAS_VENDOR=OpenBLAS" 
set "CMAKE_ARGS=-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" && set "FORCE_CMAKE=1" && pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
PS:
$env:CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS"; $env:FORCE_CMAKE="1"; pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
$env:CMAKE_ARGS="-DLLAMA_CUBLAS=ON"; $env:FORCE_CMAKE="1"; pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir


RESULTS

CPU
llm = Llama(
    model_path=r'C:\PythonParaphanalia\Models\mistral-7b-instruct-v0.2.Q4_K_M.gguf',
    n_ctx=2048
)
llama_print_timings:        load time =    2283.70 ms
llama_print_timings:      sample time =      93.92 ms /   593 runs   (    0.16 ms per token,  6314.22 tokens per second)
llama_print_timings: prompt eval time =    2283.61 ms /    49 tokens (   46.60 ms per token,    21.46 tokens per second)
llama_print_timings:        eval time =  106348.41 ms /   592 runs   (  179.64 ms per token,     5.57 tokens per second)
llama_print_timings:       total time =  110655.01 ms /   641 tokens
'''