import numpy as np
import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)
CORS(app)  # ✅ Fix CORS issue

# Load model & tokenizer
model = load_model("next_word_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

max_seq_len = 10

def predict_next_word(text):
    token_list = tokenizer.texts_to_sequences([text])[0]
    token_list = pad_sequences([token_list], maxlen=max_seq_len-1, padding='pre')

    predicted = np.argmax(model.predict(token_list), axis=-1)[0]

    for word, index in tokenizer.word_index.items():
        if index == predicted:
            return word

    return "No prediction"

# ✅ Home route
@app.route("/")
def home():
    return "API is running 🚀"

# ✅ Predict route (POST only – clean API)
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text")

    if not text:
        return jsonify({"error": "No input text provided"}), 400

    next_word = predict_next_word(text)

    return jsonify({
        "input": text,
        "next_word": next_word
    })

if __name__ == "__main__":
    app.run(debug=True)