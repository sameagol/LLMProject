'''
Seems like bitsandbytes is a wrapper for cuda functions. This is not a thing.
 - https://discuss.huggingface.co/t/inference-8-bit-or-4-bit-bit-models-on-cpu/47237
'''

from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import file_utils
from transformers import BitsAndBytesConfig
import torch


model_name = 'transformers-mistral-instruct'
model_path = ''
model_type = ''

if model_name == 'mistral':
    model_path = r'C:\PythonParaphanalia\Models\mistral-7b-v0.1.Q4_K_M.gguf'
    model_type = 'mistral'
elif model_name == 'mistral-instruct':
    model_path = r'C:\PythonParaphanalia\Models\mistral-7b-instruct-v0.2.Q4_K_M.gguf'
    model_type = 'mistral'
elif model_name == 'transformers-mistral-instruct':
    model_path = r'C:\Users\samea\.cache\huggingface\hub\models--mistralai--Mistral-7B-Instruct-v0.2\snapshots\41b61a33a2483885c981aa79e0df6b32407ed873'
    model_type = 'mistral'
elif model_name == 'vicuna':
    model_path = r'C:\PythonParaphanalia\Models\Wizard-Vicuna-13B-Uncensored.Q4_K_M.gguf'
    model_type = 'vicuna'
elif model_name == 'tiny-llama':
    model_path = r'C:\PythonParaphanalia\Models\tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf'
    model_type = 'llama'

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

tokenizer = AutoTokenizer.from_pretrained(model_path)

model = AutoModelForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.float16,
    trust_remote_code=True,
    device_map="auto",
    quantization_config=quantization_config,
    cache_dir='../model'
)

# Load the model and quantize it to 8-bit
model = AutoModelForCausalLM.from_pretrained(model_path,
                                             load_in_8bit=True,
                                             device_map='auto')

llm = AutoModelForCausalLM.from_pretrained(model_path, model_type=model_type)
system_instruction = 'the system is a useful ai assistant'

a = 1


# ??
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True, cache_dir='../model')
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, torch_dtype=torch.float16,
    trust_remote_code=True,
    device_map="auto",
    quantization_config=quantization_config,
    cache_dir='../model'
)


# Huggingface hub location
cache_dir = file_utils.default_cache_path
print(f"The Hugging Face cache directory is located at: {cache_dir}")

