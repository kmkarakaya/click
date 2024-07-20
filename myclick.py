import click 

import pathlib
import textwrap

import google.generativeai as genai

import os

google_api_key = os.getenv('GOOGLE_API_KEY')


genai.configure(api_key=google_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

@click.command()
@click.argument('prompt', required=False)
def main(prompt="Hello!"):
    """
    Start the chat. 

    PROMPT is the initial message to send. If not provided, it defaults to "Hello!".
    """
    if not prompt:
        prompt = "Hello!"
    #create a loop for a chat
    while True:
        response = chat.send_message(prompt, stream=True)
        click.echo("Model: ")
        for chunk in response:
            click.echo(chunk.text)
            #print("_"*80)

        prompt = input("You: ")
        if prompt.lower() == "bye":
            break
   
    input("Press Enter to exit...")

if __name__ == '__main__':
    main()
    

    

