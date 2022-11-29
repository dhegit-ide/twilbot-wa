from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/wasms", methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').strip().lower()
    print(incoming_msg)

    resp = MessagingResponse()
    msg = resp.message()

    msg.body("helow")
    return str(resp)

if __name__ == "__main__":	
    app.run(debug=True)