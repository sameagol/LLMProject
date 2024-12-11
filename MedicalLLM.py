'''
This script:
- Provides configuration paths for different medical LLMs, including quantized models.
- Includes examples of models with high performance on the Hugging Face leaderboard.
- Prepares system and user prompts for model input.

Huggingface Leaderboard: https://huggingface.co/spaces/openlifescienceai/open_medical_llm_leaderboard

Bloke's largest/newest medical LLM is based on AdaptLLM's Medicine 13B
 - https://huggingface.co/TheBloke/medicine-LLM-13B-GGUF
 - https://huggingface.co/AdaptLLM/medicine-LLM-13B

Palmyra-Med-70B gets good scores, but it's big
 - Quantized: https://huggingface.co/mradermacher/Palmyra-Med-70B-GGUF

John Snow Labs has a bunch of medical ones
 - johnsnowlabs/JSL-MedLlama-3-8B-v2.0
   - Quantized: https://huggingface.co/bartowski/JSL-MedLlama-3-8B-v2.0-GGUF
   - From: https://huggingface.co/johnsnowlabs/JSL-MedLlama-3-8B-v2.0
 - vkocaman/JSL-MedMX-7X
   - Quantized: https://huggingface.co/mradermacher/JSL-MedMX-7X-GGUF
   - From this model: https://huggingface.co/vkocaman/JSL-MedMX-7X
'''


model_name = 'jsl-medllama'
model_path = ''
model_type = ''

if model_name == 'mistral':
    model_path = r'C:\PythonParaphanalia\Models\mistral-7b-v0.1.Q4_K_M.gguf'
    model_type = 'mistral'
elif model_name == 'mistral-instruct':
    model_path = r'C:\PythonParaphanalia\Models\mistral-7b-instruct-v0.2.Q4_K_M.gguf'
    model_type = 'mistral'
elif model_name == 'jsl-medllama':
    model_path = r'C:\PythonParaphanalia\Models\JSL-MedLlama-3-8B-v2.0-Q6_K.gguf'
    model_type = 'llama'

a = 1

############## JSL MedLlama-3 ###############
system_prompt = ''
prompt = ''

f'''
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
'''

