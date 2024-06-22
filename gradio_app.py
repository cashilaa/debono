import gradio as gr
from openai import OpenAI
import os

# Initialize OpenAI API client
api_key = os.getenv("OPENAI_API_KEY")

# Define the Gradio interface using `Blocks`
with gr.Blocks() as demo:
    query = gr.Textbox(label="Problem", placeholder="Provide a problem to think about")
    submit_button = gr.Button("Submit")
    
    # Textboxes for different hats
    with gr.Row():
        white_hat = gr.Textbox(label="White Hat", interactive=False)
        red_hat = gr.Textbox(label="Red Hat", interactive=False)
        black_hat = gr.Textbox(label="Black Hat", interactive=False)
        yellow_hat = gr.Textbox(label="Yellow Hat", interactive=False)
        green_hat = gr.Textbox(label="Green Hat", interactive=False)
    blue_hat = gr.Textbox(label="Blue Hat (synthesis)", interactive=False)
    my_hat = gr.Textbox(label="My Hat", interactive=False)  # New textbox for "My Hat"

    async def handle_submit(query):
        try:
            # Request completion from OpenAI's API using the provided query
            response = await openai.Completion.create(
                engine="text-davinci-003",
                prompt=query,
                max_tokens=1000,
                stop=None
            )
            
            # Extract responses for each hat from OpenAI's response
            white_hat.text = response['choices'][0]['text']
            red_hat.text = response['choices'][1]['text']
            black_hat.text = response['choices'][2]['text']
            yellow_hat.text = response['choices'][3]['text']
            green_hat.text = response['choices'][4]['text']
            my_hat.text = response['choices'][5]['text']
            blue_hat.text = response['choices'][6]['text']
        
        except Exception as e:
            print(f"Error: {e}")
    
    submit_button.click(
        fn=handle_submit,
        inputs=[query],
        outputs=[
            white_hat,
            red_hat,
            black_hat,
            yellow_hat,
            green_hat,
            blue_hat,
            my_hat
        ],
    )

# Launch the Gradio interface
if __name__ == "__main__":
    demo.launch()
