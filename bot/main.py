from flask import Flask, request
from bot.whatsapp import handle_message



app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').lower()
    sender = request.values.get('From', '')
    return handle_message(incoming_msg, sender)

if __name__ == "__main__":
    app.run(debug=True)
