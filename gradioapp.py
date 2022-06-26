from main import *
import gradio as gr

gr.Interface(fn=chatbot_response,
            title = "KIRA Bot",
            inputs=["text"],
            outputs=["chatbot", "audio"]).launch(debug=True)
