import numpy as np
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load IMDb's word index
word_index = imdb.get_word_index()

# Load the trained sentiment model
model = load_model('imdb_sentiment_model.h5')

# Parameters (must match training)
max_features = 10000  # Vocabulary size
maxlen = 200  # Maximum length of sequences

# Function to convert a review into a sequence
def encode_review(review):
    words = review.lower().split()  # Simple tokenization (space-based)
    encoded = [word_index[word] + 3 if word in word_index and word_index[word] < max_features else 2 for word in words]
    return pad_sequences([encoded], maxlen=maxlen)

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_review = request.form["review"]  # Get review from form
        encoded_review = encode_review(user_review)  # Encode the review
        prediction = model.predict(encoded_review)[0][0]  # Get prediction

        # Determine sentiment
        sentiment = "Positive 😊" if prediction > 0.5 else "Negative 😡"
        score = f"{prediction:.4f}"

        return render_template("index.html", review=user_review, sentiment=sentiment, score=score)

    return render_template("index.html", review="", sentiment=None, score=None)

if __name__ == "__main__":
    app.run(debug=True)
