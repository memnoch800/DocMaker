import os 
import openai
import tkinter as tk
import jinja2

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("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")



# OPEN AI TING
response = openai.Completion.create(
    model="text-davinci-003", 
    prompt="Say this is a test", 
    temperature=0, 
    max_tokens=7)


# TKINTER START
window = tk.tk()
