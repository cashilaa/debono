import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API client
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("No OpenAI API key found. Please set OPENAI_API_KEY in .env file.")

openai = OpenAI(api_key)

# Define the Gradio interface using `Blocks`
with gr.Blocks() as demo:
    query = gr.Textbox(label="Problem", placeholder="Provide a problem to think about")
    submit_button = gr.Button("Submit")
    
    # Textbox for displaying the result
    result_textbox = gr.Textbox(label="Result", interactive=False)

    async def handle_submit(query):
        try:
            # Request completion from OpenAI's API using the provided query
            response = await openai.Completion.create(
                engine="text-davinci-003",
                prompt=query,
                max_tokens=1000,
                stop=None
            )
            
            # Extract the generated response
            result = response['choices'][0]['text']
            
            # Update the result textbox with the obtained result
            result_textbox.text = result
        
        except Exception as e:
            print(f"Error: {e}")
    
    # Link button click to handle_submit function
    submit_button.click(
        fn=handle_submit,
        inputs=[query],
        outputs=None,  # No immediate output binding here
    )

# Launch the Gradio interface
if __name__ == "__main__":
    gr.Interface(
        fn=None,  # No function binding needed for initial launch
        inputs=[query, submit_button],  # Inputs include query and submit button
        outputs=[result_textbox],  # Output is the result textbox
        title="Six Thinking Hats",
    ).launch()
