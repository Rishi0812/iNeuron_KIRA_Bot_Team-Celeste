from main import *
from flask import Flask, render_template, request, Response

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("chatwindow.html")

# @app.route("/mp3")
# def streamwav():
#     def generate():
#         with open("temp.mp3", "rb") as fwav:
#             data = fwav.read(1024)
#             while data:
#                 yield data
#                 data = fwav.read(1024)
#     return Response(generate(), mimetype="audio/x-wav")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    temp = str(chatbot_response(userText))
    return temp, speak

@app.route('/post')
def load_dialogue():
    return "pic.gif"


if __name__ == "__main__":
    app.run()
