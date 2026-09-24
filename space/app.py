import os

import gradio as gr
from huggingface_hub import InferenceClient

MODEL = os.environ.get("HERMES_MODEL", "Qwen/Qwen2.5-7B-Instruct")
TOKEN = os.environ.get("HF_TOKEN")

client = InferenceClient(model=MODEL, token=TOKEN)


def respond(message, history):
    messages = list(history or [])
    messages.append({"role": "user", "content": message})
    response = client.chat_completion(
        messages=messages,
        max_tokens=1024,
        temperature=0.7,
    )
    return response.choices[0].message.content


demo = gr.ChatInterface(
    fn=respond,
    type="messages",
    title="Hermes Stack",
    description=f"Free Gradio Space using {MODEL}",
    textbox=gr.Textbox(placeholder="Ask something...", container=False),
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
