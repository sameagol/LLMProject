'''
This script:
- Supports multiple language models for text classification.
- Uses regex and predefined prompts to extract and clean model predictions.
- Includes accuracy calculations and performance benchmarking.
'''

from ctransformers import AutoModelForCausalLM
import re
import pandas as pd


def get_label_tiny_llama(description):
    answer = llm(f'''<|im_start|>system {system_instruction}<|im_end|>
        <|im_start|>user
        Here is an article: 
        
        {description[:400]}
        
        In one word, tell me which one of these categories matches it best.
        - Politics
        - Sport
        - Technology
        - Entertainment
        - Business

        <|im_end|>
        <|im_start|>assistant
        ''', max_new_tokens=15, temperature=0.5)

    # print('raw answer: ' + answer)

    answer = answer.strip()
    #
    # cleaned_answer = answer.strip().replace('<|im_end|', '')
    #
    # # Remove all special characters
    # cleaned_answer = re.sub(r'[^A-Za-z0-9 ]+', '', cleaned_answer)

    # Find the position of the first '<' character
    index = answer.find('<')

    # Slice the string up to the position of '<' if it is found, otherwise return the full string
    if index != -1:
        return answer[:index]
    else:
        return answer

    return answer



def get_label_mistral(description):
    answer = llm(f'''{pre}Here is an article: 

        {example_text[:400]}

        Tell me which one of these categories matches it best: Politics, Sport, Technology, Entertainment, Business

        Please respond in one single word.
        {post}''', max_new_tokens=15, temperature=0.5)

    # print('raw answer: ' + answer)
    pattern = r'\b(' + '|'.join(map(re.escape, list(category_to_code.keys()))) + r')\b'

    # Search for the pattern in the text
    match = re.search(pattern, answer)

    # If a match is found, return the matched word
    if match:
        return match.group(1)
    else:
        return None


model_name = 'mistral-instruct'
model_path = ''
model_type = ''

if model_name == 'mistral':
    model_path = r'C:\PythonParaphanalia\Models\mistral-7b-v0.1.Q4_K_M.gguf'
    model_type = 'mistral'
elif model_name == 'mistral-instruct':
    model_path = r'C:\PythonParaphanalia\Models\mistral-7b-instruct-v0.2.Q4_K_M.gguf'
    model_type = 'mistral'
elif model_name == 'vicuna':
    model_path = r'C:\PythonParaphanalia\Models\Wizard-Vicuna-13B-Uncensored.Q4_K_M.gguf'
    model_type = 'vicuna'
elif model_name == 'tiny-llama':
    model_path = r'C:\PythonParaphanalia\Models\tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf'
    model_type = 'llama'

llm = AutoModelForCausalLM.from_pretrained(model_path, model_type=model_type)
system_instruction = 'the system is a useful ai assistant'

a = 1

####################
## Try Labeling ##

# Path to the CSV file
file_path = r'C:\PythonParaphanalia\Data\df_file.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(df.head())

# Split the data into training and test datasets
# train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
# print(train_data.head())

example_text = '''Budget to set scene for election\n \n Gordon Brown will seek to put the economy at the centre of Labour\'s bid for a third term in power when he delivers his ninth Budget at 1230 GMT. He is expected to stress the importance of continued economic stability, with low unemployment and interest rates. The chancellor is expected to freeze petrol duty and raise the stamp duty threshold from Â£60,000. But the Conservatives and Lib Dems insist voters face higher taxes and more means-testing under Labour.\n \n Treasury officials have said there will not be a pre-election giveaway, but Mr Brown is thought to have about Â£2bn to spare.\n \n - Increase in the stamp duty threshold from Â£60,000 \n  - A freeze on petrol duty \n  - An extension of tax credit scheme for poorer families \n  - Possible help for pensioners The stamp duty threshold rise is intended to help first time buyers - a likely theme of all three of the main parties\' general election manifestos. Ten years ago, buyers had a much greater chance of avoiding stamp duty, with close to half a million properties, in England and Wales alone, selling for less than Â£60,000. Since then, average UK property prices have more than doubled while the starting threshold for stamp duty has not increased. Tax credits As a result, the number of properties incurring stamp duty has rocketed as has the government\'s tax take. The Liberal Democrats unveiled their own proposals to raise the stamp duty threshold to Â£150,000 in February.\n \n The Tories are also thought likely to propose increased thresholds, with shadow chancellor Oliver Letwin branding stamp duty a "classic Labour stealth tax". The Tories say whatever the chancellor gives away will be clawed back in higher taxes if Labour is returned to power. Shadow Treasury chief secretary George Osborne said: "Everyone who looks at the British economy at the moment says there has been a sharp deterioration in the public finances, that there is a black hole," he said. "If Labour is elected there will be a very substantial tax increase in the Budget after the election, of the order of around Â£10bn."\n \n But Mr Brown\'s former advisor Ed Balls, now a parliamentary hopeful, said an examination of Tory plans for the economy showed there would be a Â£35bn difference in investment by the end of the next parliament between the two main parties. He added: "I don\'t accept there is any need for any changes to the plans we have set out to meet our spending commitments."\n \n For the Lib Dems David Laws said: "The chancellor will no doubt tell us today how wonderfully the economy is doing," he said. "But a lot of that is built on an increase in personal and consumer debt over the last few years - that makes the economy quite vulnerable potentially if interest rates ever do have to go up in a significant way." SNP leader Alex Salmond said his party would introduce a Â£2,000 grant for first time buyers, reduce corporation tax and introduce a citizens pension free from means testing. Plaid Cymru\'s economics spokesman Adam Price said he wanted help to get people on the housing ladder and an increase in the minimum wage to Â£5.60 an hour.\n'''
get_label_tiny_llama(example_text[:400])

# Mapping of categories to codes
category_to_code = {
    'Politics': 0,
    'Sport': 1,
    'Technology': 2,
    'Entertainment': 3,
    'Business': 4
}

a = 1

df_slim = df.sample(frac=.01)
print(df_slim.shape[0])
df_slim['New Label'] = df_slim['Text'].apply(lambda x: get_label_mistral(x))

# Replace the text labels with their corresponding numeric codes
df_slim['New Label Code'] = df_slim['New Label'].replace(category_to_code)

print('total length of df_slim: ' + str(df_slim.shape[0]))
correct_df = df_slim[df_slim['Label'] == df_slim['New Label Code']]
print('total length of correct_df: ' + str(correct_df.shape[0]))
print('percentage correct: ' + str(round(correct_df.shape[0] / df_slim.shape[0], 2)))
# 9% with tinyllama, 5 minutes or so to do 200 entries
# 23% with mistral instruct, 5 minutes or so to do 20 entries


##############################
## Understanding Tiny LLAMA ##
prompt = f'''<|im_start|>system {system_instruction}<|im_end|>
    <|im_start|>user
    Here is an article: 
    
    {text}
    
    In one word, tell me which category matches it best.
    
    Politics
    Sport
    Technology
    Entertainment
    Business

    <|im_end|>
    <|im_start|>assistant
    '''
print(llm(prompt, max_new_tokens=10, repetition_penalty=1.1, temperature=1.2))


'''
Politics = 0
Sport = 1
Technology = 2
Entertainment =3
Business = 4
'''


###########################
## Understanding Mistral ##
pre = '<s>[INST] '
post = '[/INST] '

answer = llm(f'''{pre}Here is an article: 

    {example_text[:400]}

    Tell me which one of these categories matches it best: Politics, Sport, Technology, Entertainment, Business
    
    Please respond in one single word.
    {post}''', max_new_tokens=15, temperature=0.5)

# print('raw answer: ' + answer)
pattern = r'\b(' + '|'.join(map(re.escape, list(category_to_code.keys()))) + r')\b'

# Search for the pattern in the text
match = re.search(pattern, answer)

# If a match is found, return the matched word
if match:
    print(match.group(1))
else:
    print(None)