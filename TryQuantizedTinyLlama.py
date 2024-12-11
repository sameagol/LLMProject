'''
ctransformers docs: https://github.com/marella/ctransformers?tab=readme-ov-file#documentation

Useful prompt guide for Mistral Instruct
https://www.promptingguide.ai/models/mistral-7b

Try this? https://huggingface.co/LeroyDyer/Mixtral_Uncensored_7b/tree/main

Try:
Passing parameters
GPU

'''

from ctransformers import AutoModelForCausalLM

model_name = 'tiny-llama'
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
## Understanding Tiny LLAMA ##
prompt = 'Who was the president in 2003 and why?'
total_prompt = f'''<|im_start|>system {system_instruction}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
'''
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=1.2))
'''Bill Clinton served as the 42nd President of the United States from January 19, 1993 to January 20, 2001. He was elected to a second term following the death of President George H. W. Bush.<|im_end|>'''
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=0.8))
'''The President of the United States in 2003 was George W. Bush. He was re-elected in 2004, after a failed bid for a third term in 2000.
In his first term, he implemented policies such as the US invasion of Iraq and the war on terrorism, which led to the deaths of thousands of people and the displacement of millions more. He also signed numerous legislative packages that increased the national debt and deficit, which had a negative impact on the economy and the U.S.' credit ratings. He ultimately made four incorrect attempts to nuke North Korea; while such acts constitute non-provoked threats by duly-serving US leadership of hostile invasion from nuclear armed rivals such as USSR<|im_end|>'''

####################
## Tiny LLAMA: Hard Prompts and Hyperparameter Tuning ##
# Recall
prompt = 'Who was the president in 2003 and why?'
total_prompt = f'''<|im_start|>system {system_instruction}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
'''
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=0.8))
'''Bill Clinton was the 42nd President of the United States from March 19, 1993 to January 20, 2001. He succeeded George W. Bush as the 43rd President following the resignation of Bush in the aftermath of the September 11, 2001 attacks.
In office, Clinton focused on domestic policy issues such as poverty, welfare reform, and reducing the deficit. He also implemented a series of reforms to the health care system, including the Affordable Care Act. Clinton was known for his successful marriage to former First Lady Hillary Rodham Clinton, and for signing the American Recovery and Reinvestment Act of 2009, which provided economic stimulus and job creation during the Great Recession.<|im_end|>'''
'''Democrats control both houses of congress and have had a few presidents, but none since George W Bush in 2008.<|im_end|>'''
'''The President of the United States in 2003 was George W. Bush. He was re-elected in 2004 and served as President until his term expired in 2009.<|im_end|>'''
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=0.5))
'''During the year 2003, there were two U.S. presidents: George W. Bush for the second term as President of the United States and Barack Obama for his first term as President of the United States.<|im_end|>'''
'''The President of the United States in 2003 was George W. Bush. He was re-elected in 2004 and served until January 2009, after which his term was ratified by a vote of the people. The presidency is the highest office in the federal government of the United States.<|im_end|>'''
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=0.1))
'''The president of the United States in 2003 was George W. Bush. He was re-elected in 2004 and served until 2009, during which time he signed several major legislative acts into law, including the USA PATRIOT Act and the American Recovery and Reinvestment Act of 2009.<|im_end|>'''

# Communicate Complex Topics
prompt = 'In a paragraph, explain the difference between quantum physics and Newtonian physics.'
total_prompt = f'''<|im_start|>system {system_instruction}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
'''
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=0.8))
answer = '''
Quantum physics and Newtonian physics are two branches of physics that have different aspects.
Quantum physics deals with tiny particles, like atoms or electrons. It focuses on how these tiny particles interact to form large-scale structures. Quantum mechanics describes the behavior of these tiny particles at the quantum level. For example, it explains why electrons move in a certain way and why light is always described as a wave instead of a particle.
Newtonian physics, on the other hand, deals with objects that are not so small. It focuses on how large forces and motion behave on Earth and beyond. Newton's laws of motion govern the behavior of these large-scale objects, like planets, stars, and galaxies. For example, it explains why some things fall and others rise.
The main difference between quantum physics and Newtonian physics is that quantum physics focuses on the behavior of tiny particles, while Newtonian physics focuses on large-scale objects. However, they both provide valuable insights into how the universe works at the atomic and subatomic level.<|im_end|>
'''
# ^ Answer Quality: Quantum physics summary is wrong - electrons sometimes act like waves and sometimes like particles
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=0.2))
answer = '''
Quantum physics and Newtonian physics are two branches of physics that have different characteristics. Here are some key differences between them:
1. Quantum Physics: Quantum physics is the branch of physics that deals with subatomic particles, such as electrons and protons. It is based on the idea that everything in the universe is made up of tiny particles called quanta. These particles have a definite position and momentum at any given time, and can be described by mathematical equations. In contrast to classical physics, quantum physics has a more fundamental nature, because it deals with the smallest possible units of measurement.
2. Newtonian Physics: Newtonian physics is the branch of physics that was developed by Isaac Newton. It is based on the idea that everything in the universe is governed by the same laws of motion as objects in a vacuum. In this theory, gravity is considered to be a force that acts between two particles, and their movement is determined by the mass and momentum of each particle.
3. Quantum Mechanics: Quantum mechanics is the branch of physics that deals with the behavior of particles at the quantum level. It is based on the idea that everything in the universe is made up of tiny particles, such as electrons or protons. These particles have a definite position and momentum at any given time, but can be described by wave-like patterns called quanta. The laws of quantum mechanics apply to these particles, and they obey the principle of superposition.
4. Newton's Laws: Newton's laws are mathematical principles that describe how things move in the universe. They are based on the idea that everything in the universe is governed by the same laws of motion as objects in a vacuum. These laws include the first law of thermodynamics, which states that energy cannot be created or destroyed, only transferred from one form to another; and the second law of thermodynamics, which states that energy can neither be created nor destroyed in the universe, but can be used up or released.
5. Newton's Third Law: Newton's
'''
# ^ Answer Quality: Repeats summary of quantum physics. Separates address of newtonian physics
prompt = 'Explain the difference between quantum physics and Newtonian physics.'
total_prompt = f'''<|im_start|>system {system_instruction}<|im_end|>
{prompt}
'''
total_prompt = f'''
system: {system_instruction}
{prompt}
'''
total_prompt = f'''
<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
'''
total_prompt = f'''
<|im_start|>system\n{system_instruction}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
'''
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=0.8))
answer = '''
Quantum physics and Newtonian physics are two different branches of physics that study the behavior of matter and energy at the atomic and subatomic level.
The main differences between the two are:
- Quantum physics is based on the principles of quantum mechanics, which states that particles can exist in multiple states simultaneously, and that their properties depend on the strength of the probability distribution for these states. This means that particles can exhibit both a definite position and a definite velocity at the same time, whereas Newtonian mechanics only allows for one state of being for an object.
- Newton's laws of motion, which describe how objects move and interact with each other, are based on the principles of classical physics, which does not consider quantum effects.
Both areas of physics have their strengths and limitations, and have contributed to advancements in technology, medicine, and science. The two also share some connections through the concept of wave-particle duality, where particles can exhibit both wave-like and particle-like properties.<|im_end|>
'''

# Combine Recall and Reasoning
prompt = 'Briefly explain the role of carbon in biological life, and suggest another element that could serve a similar role.'
total_prompt = f'''
<|im_start|>system\n{system_instruction}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
'''
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=0.8))
answer = '''
As a cofactor in the synthesis of many biochemical pathways, such as the respiratory chain and the biosynthesis of amino acids.
As an essential component of DNA and RNA, which are the building blocks of life.
As a key component of cellular respiration, which converts organic compounds into usable forms for further chemical reactions.
As a component of the water cycle, which helps to maintain a stable temperature and humidity environment in our planet.
As an essential component of many enzymes, which catalyze complex chemical reactions.
In addition to these important roles, carbon is also found in trace quantities in some minerals and metals, such as cobalt and vanadium.
Despite its importance, the exact role of carbon in biological systems remains a subject of ongoing research and debate. The understanding of carbon's role in life is complex and involves a wide range of disciplines, including biochemistry, molecular biology, environmental science, and chemical physics.<|im_end|>
'''
# ^ Lacks other element
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=2))

# Complex Language
prompt = 'Summarize the main arguments presented in the last State of the Union address and evaluate their potential impact on public policy.'
total_prompt = f'''
<|im_start|>system\n{system_instruction}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
'''
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=0.8))
answer = '''
The main arguments presented in the last State of the Union address were:
1. The need to invest in infrastructure for the country’s prosperity
2. Raise minimum wage
3. Stop abuse by private businesses over the rights and dignity of workers
4. Improve access to healthcare for all
5. End the tax breaks for the wealthy
6. Reduce the federal government’s size
7. End the use of drones for surveillance
8. End the use of military force without congressional approval
9. Protect the environment and public health
10. End the war in Afghanistan
These are just a few of the main arguments presented by President Biden during his last State of the Union address. These issues will continue to be discussed and debated in the coming years as the United States grapples with several economic, political, and social challenges.<|im_end|>
'''
# ^ Misses latter half

# Sarcasm
prompt = 'Analyze the sentiment of the following statement: "I just love waiting in traffic, it us the highlight of my day."'
total_prompt = f'''
<|im_start|>system\n{system_instruction}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
'''
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=0.8))
answer = '''
I understand that you are a useful ai assistant and I am here to help you with any questions or information you need. However, I would like to point out that waiting in traffic can be bothersome and annoying, especially if it is an extended period of time. However, if you love the feeling of waiting in traffic then it could also be a highlight of your day since it is one of those situations where you get what you pay for. If you would like more information on this subject I can provide you with some additional information that might be helpful to your decision.<|im_end|>
'''
# ^ Nope
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=2))
answer = '''
'''

# Creativity
prompt = 'Write a short story about a detective solving a mystery in a futuristic city using only sustainable technologies.'
total_prompt = f'''
<|im_start|>system\n{system_instruction}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
'''
print(llm(total_prompt, max_new_tokens=450, repetition_penalty=1.1, temperature=0.8))
answer = '''
In the year 2068, San Francisco was a thriving metropolis with cutting-edge technology and an impressive downtown area. But that wasn't all there was to this bustling city. Just beyond the bustle of the busy streets, a mysterious mist had spread like a blanket over the entire city. It was as if something were haunting the place, but no one knew what it was or why it was there.
Detective Lance Stevenson was one of the first people to notice the strange mist. He worked as a detective in the city's crime division and had seen many strange incidents take place throughout his years in the department. Most were due to people hearing or seeing things that didn't actually exist.
Lance noticed something different though. Something that was slightly out of place, but not entirely out of place. It wasn't a real thing. In fact, it had only ever been in his imagination.
It wasn't until after midnight on the evening of the fourth of July when he received his day off did Lance really notice that everything had somehow changed. Not only that, but all around him things began to look a little odd.
He looked down at his jeans and shirt, both of which were socks. The shirt was completely untucked with his buttoning down efforts resulting in only two cups visible when he stood before it could've easily fit 5, with half that still coming off due to the fabric being too tight.
Lance looked up at the sky and saw a strange light. It wasn't exactly blue. In fact, it was more of a purple-violet hue that stretched as far as his eyes could see. As if it were reaching out from the depths of the city's darkness.
"What is that?" he asked in a low voice to no one in particular.
He looked around and saw other people doing the same thing. They all had their own version of their hands ons too- their own unique gearly different reactions taken
'''

####################
## Medical Use Case ##
updated_prompt = '''
Here are my symptoms: low energy, brain fog, body aches.
Here are my triggers: herbs, carbs, sugar, processed foods, stress, pollen/hay fever.
I get relief from walking at the beach, and eboo (extracorporeal blood oxidation ozonation).
What medical diagnoses might be appropriate for me?
'''
total_medical_prompt = f'''<|im_start|>system {system_instruction}<|im_end|>
<|im_start|>user
{updated_prompt}<|im_end|>
<|im_start|>assistant
'''
print(llm(total_medical_prompt, max_new_tokens=500, repetition_penalty=1.1, temperature=1.5))
answer = '''
An autopsy report usually describes various heart failure stages; so according to experts with many experience in cardiology, a pollen allergy could be one of the possible causes. However, if you have no symptoms and are healthy enough, it is not clear what could be causing your health problems. It would be best to consult a doctor for a proper diagnosis.<|im_end|>
'''
print(llm(total_medical_prompt, max_new_tokens=500, repetition_penalty=1.1, temperature=.8))
answer = '''
For a medical condition related to energy level or brain fog, a neurologist or psychiatrist could help you get the proper evaluation and treatment.
As far as triggers, herbs can have various causes. Some common ones include:
- Pollen sensitivity: Consuming products that contain alfalfa, chamomile, lily of the valley, mint or parsley, as they contain specific mucilages
- Food intolerances or sensitivities: Consuming gluten, dairy, eggs, nuts, soy, or sulfur compounds can cause digestive issues and autoimmune disorders.
- Stress: Chronic stress can lead to hormonal changes that can affect the brain and mood.
I hope this information was helpful! Let me know if you need more assistance.
'''

####################
'''
Here are some of the most influential parameters:

Temperature:
This parameter significantly impacts the randomness and creativity of the model's responses. A lower temperature results in more predictable and safer outputs, while a higher temperature makes the responses more diverse and less deterministic. It is one of the most direct ways to influence the style of generated text.
Top-k Sampling:
By limiting the next word predictions to the top k most likely candidates, this parameter effectively narrows down the choices the model considers, which can greatly influence the coherence and relevance of the output. It's particularly useful in maintaining a balance between randomness and the precision of the output.
Top-p (Nucleus) Sampling:
This parameter dynamically adjusts the number of words considered at each step based on their cumulative probability. It is influential in ensuring that the generated text remains within a plausible and coherent range while allowing for enough variability to keep the text engaging.
Repetition Penalty:
The repetition penalty is crucial for controlling redundancy in the model's output. It discourages the model from repeating the same words or phrases, which is essential for generating long-form content or in dialog systems where repetitive responses can diminish user experience.
No Repeat N-Gram Size:
This parameter prevents the model from repeating any sequence of n words that it has already used, significantly affecting the uniqueness and readability of the text. It's particularly valuable in creative writing and content generation to ensure the output is engaging and varied.
Max Length and Min Length:
These parameters define the bounds of the output's length, directly influencing how concise or detailed the model's responses are. They are crucial in applications where the length of the output matters, such as summarization (max length) or ensuring adequate explanation (min length).
'''