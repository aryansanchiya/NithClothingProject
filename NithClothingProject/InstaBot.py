from instapy import InstaPy
import openai
import os
import pandas as pd
import openai 
openai.api_key = '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'
messages = [ {"role": "system", "content": 
			"You are a intelligent assistant."} ] 
while True: 
	message = input("User : ") 
	if message: 
		messages.append( 
			{"role": "user", "content": message}, 
		) 
		chat = openai.ChatCompletion.create( 
			model="gpt-3.5-turbo", messages=messages 
		) 
	reply = chat.choices[0].message.content 
	print(f"ChatGPT: {reply}") 
	messages.append({"role": "assistant", "content": reply}) 
