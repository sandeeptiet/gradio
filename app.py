import gradio as gr
import requests
import os

# Read the inference URL from an environment variable for flexibility
INFERENCE_URL = os.environ.get("INFERENCE_URL", "http://default-inference-url")

# Retrieve the port from the environment; default to 7860 if not set
port = int(os.environ.get("PORT", 7860))

def chat(input_text):
    # Call the AI model inference endpoint
    response = requests.post(INFERENCE_URL, json={"inputs": input_text})
    # Assuming the response returns a JSON with a key 'generated_text'
    result = response.json().get("generated_text", "No response")
    return result

iface = gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text",
    title="Chatbot UI",
    allow_flagging="never"
)

iface.launch(server_name="0.0.0.0", server_port=port)
