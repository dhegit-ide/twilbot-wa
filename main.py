import string
import pickle
import numpy as np
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from util import JSONParser

app = Flask(__name__)  

@app.route("/wasms", methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').strip()
    print(incoming_msg)

    resp = MessagingResponse()
    msg = resp.message()


    # CHATBOT SKLEARN TRAIN
    # cleaning data
    def preprocess(chat):
        chat = chat.lower()
        tandabaca = tuple(string.punctuation)
        chat = ''.join(ch for ch in chat if ch not in tandabaca)
        return chat
    
    def bot_response(chat, pipeline, jp):
        chat = preprocess(chat)
        res = pipeline.predict_proba([chat])
        max_prob = max(res[0])
        if max_prob < 0.2:
            return "Maaf kak, aku ga ngerti :("
        else:
            max_id = np.argmax(res[0])
            pred_tag = pipeline.classes_[max_id]
            return jp.get_response(pred_tag)

    # load data
    path = "data/intents.json"
    jp = JSONParser()
    jp.parse(path)
    df = jp.get_dataframe()

    # preprosesing data
    df['text_input_prep'] = df.text_input.apply(preprocess)

    # pemodelan
    pipeline = make_pipeline(CountVectorizer(), RandomForestClassifier())

    # train
    pipeline.fit(df.text_input_prep, df.intents)

    # END


    output = bot_response(incoming_msg, pipeline, jp)

    msg.body(output)
    return str(resp)

if __name__ == "__main__":	
    app.run(debug=True)