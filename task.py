from config import *



import openai

openai.api_key = OPENAI_KEY
text= input("Enter the text:\n")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"The application has to categorize the input sentence as chitchat or not. If the provided sentence is chitchat it has to respond with “It’s chitchat” or “It’s not chitchat\n {text}",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

print(f"Response:{response['choices'][0]['text']}")