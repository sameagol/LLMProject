'''
https://llm-tracker.info/howto/AMD-GPUs#windows
"
For an easy time, go to llama.cpp’s release page and download a bin-win-clblast version.
In the Windows terminal, run it with -ngl 99 to load all the layers into memory.
.\main.exe -m model.bin -ngl 99
On a Radeon 7900XT, you should get about double the performance of CPU-only execution.

---
To use:


"

CPU:
PS C:/PythonParaphanalia/llama-b2754-bin-win-clblast-x64>
./main -m C:\PythonParaphanalia\Models\mistral-7b-instruct-v0.2.Q4_K_M.gguf --color --temp 0.8 --top_k 40 --top_p 0.95 --ctx_size 2048 --n_predict -1 --keep -1 -p "[INST] I have a headache, nausea, and I recently got my finger amputated. I don't have any pharmaceuticals, what herbal remedies will help me?[/INST]"
llama_print_timings:        load time =     922.21 ms
llama_print_timings:      sample time =      22.14 ms /   653 runs   (    0.03 ms per token, 29496.79 tokens per second)
llama_print_timings: prompt eval time =    4988.39 ms /    48 tokens (  103.92 ms per token,     9.62 tokens per second)
llama_print_timings:        eval time =  113651.74 ms /   652 runs   (  174.31 ms per token,     5.74 tokens per second)
llama_print_timings:       total time =  118819.44 ms /   700 tokens

GPU:
PS C:/PythonParaphanalia/llama-b2754-bin-win-clblast-x64>
./main -m C:\PythonParaphanalia\Models\mistral-7b-instruct-v0.2.Q4_K_M.gguf --color --temp 0.8 --top_k 40 --top_p 0.95 --ctx_size 2048 --n_predict -1 --keep -1 -p "[INST] I have a headache, nausea, and I recently got my finger amputated. I don't have any pharmaceuticals, what herbal remedies will help me?[/INST]" -ngl 99
llama_print_timings:        load time =   12350.45 ms
llama_print_timings:      sample time =      15.58 ms /   484 runs   (    0.03 ms per token, 31075.44 tokens per second)
llama_print_timings: prompt eval time =    3129.80 ms /    48 tokens (   65.20 ms per token,    15.34 tokens per second)
llama_print_timings:        eval time =   51743.03 ms /   483 runs   (  107.13 ms per token,     9.33 tokens per second)
llama_print_timings:       total time =   54999.63 ms /   531 tokens

'''

import subprocess

import subprocess


def send_command(command):
    """ Send a command to the CMD process """
    process.stdin.write(command + "\n")
    process.stdin.flush()  # Ensure the command is sent


def read_output():
    """ Read the response from the CMD process """
    return process.stdout.readline()


def close_terminal():
    """ Close the CMD process """
    process.terminate()


def run_win_cmd(cmd):
    result = []
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for line in process.stdout:
        result.append(line)
    errcode = process.returncode
    for line in result:
        print(line)
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', cmd)

# Start the CMD process
process = subprocess.Popen(['cmd'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


a = 1


##################
setup_command = '''
cd C:/PythonParaphanalia/llama-b2754-bin-win-clblast-x64
'''
process.stdin.write(setup_command + "\n")
process.stdin.flush()  # Ensure the command is sent
print(process.stdout.readline())

# send_command(setup_command)

##################

# Example of usage
try:
    send_command('echo Hello, CMD!')
    print("CMD Response:", read_output())
    # Add more interactions as needed
finally:
    close_terminal()


# Example command: list directory contents
command = "cd C:/PythonParaphanalia/llama-b2754-bin-win-clblast-x64"
command = 'dir'

# Run command and capture output
try:
    result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
    print("Command output:", result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

