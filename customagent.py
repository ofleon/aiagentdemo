from dotenv import load_dotenv
from openai import OpenAI
from tools import websearch
import os

class MyAgent:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY_DEMO"))
        self.system_message = "You're a helpful assistant."
        self.messages = []
        self.messages.append({"role": "system", "content": self.system_message})

    def chat(self, prompt, iswebsearch=False):
        if iswebsearch:
            print("Searching data from web.")
            search_results = websearch(prompt)
            formatted_prompt = f"return a breif summary of a maximal of 250 characters of the following web search results: {search_results}"
            self.messages.append({"role": "user", "content": formatted_prompt})
            completion = self.client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "user", "content": formatted_prompt},
                ],
            )

            #setting the short term memory
            self.messages.append({"role": "assistant", "content": completion.choices[0].message.content})

            return completion.choices[0].message.content
        else:
            self.messages.append({"role": "user", "content": prompt})
            completion = self.client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "user", "content": prompt},
                ],
            )

            #setting the short term memory
            self.messages.append({"role": "assistant", "content": completion.choices[0].message.content})
            return completion.choices[0].message.content