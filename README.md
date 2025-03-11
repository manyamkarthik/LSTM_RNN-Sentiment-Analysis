# IMDB Sentiment Analysis Web App

This project is a web application that performs sentiment analysis on movie reviews using a Recurrent Neural Network (RNN) model trained on the IMDB dataset. Users can input a movie review, and the application will predict whether the sentiment is positive or negative.

## Overview

This project demonstrates a basic implementation of sentiment analysis.  It provides a user-friendly interface for interacting with a trained model, as well as a foundation for further enhancements and experimentation.

## Project Structure

The project has the following structure:

imdb-sentiment-app/
├── app.py # Flask application
├── imdb_sentiment_model.h5 # Trained RNN model
├── templates/ # HTML templates
│ └── index.html # Main HTML page
└── README.md # This file


*   `app.py`: The Flask application that handles user input, loads the trained model, preprocesses the review text, makes predictions, and renders the results.
*   `imdb_sentiment_model.h5`: The trained RNN model (LSTM network) that has been trained on the IMDB dataset.
*   `templates/index.html`: The HTML template that provides the user interface for entering movie reviews and displaying the sentiment analysis results.
*   `README.md`: This documentation file.

## Technologies Used

*   Python
*   Flask (web framework)
*   TensorFlow/Keras (deep learning library)
*   NumPy (numerical computing)
*   HTML
*   CSS (for basic styling)

## Setup and Installation

1.  **Clone the Repository:**

    ```bash
    git clone [repository URL]
    cd imdb-sentiment-app
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    (You'll need to create a `requirements.txt` file listing all the necessary packages:  `Flask`, `tensorflow`, `Keras`, `numpy`.  See the "Creating requirements.txt" section below.)

4.  **Create a `requirements.txt` file:** If you haven't already create a `requirements.txt` file with the correct versions of `Flask`, `tensorflow`, `Keras`, and `numpy`. If you are not sure, you can use the script in the `VENV` to display the versions.

## Running the Application

1.  **Run the Flask application:**

    ```bash
    python app.py
    ```

2.  **Access the Application:** Open your web browser and navigate to `http://127.0.0.1:Port Number/` or the address shown in your terminal.

## How to Use

1.  **Enter a Movie Review:**  In the text area on the main page, enter the movie review you want to analyze.
2.  **Click "Analyze Sentiment":** Click the "Analyze Sentiment" button.
3.  **View the Results:** The application will display the predicted sentiment (Positive or Negative) and a score indicating the confidence of the prediction. An emoji will also be displayed alongside the sentiment result.


## Limitations

*   **Simplified Preprocessing:** This application uses a very basic text preprocessing method.  More advanced techniques (e.g., stemming, lemmatization, handling stop words) could improve the accuracy of the sentiment analysis.


## Future Enhancements

*   Improve text preprocessing using NLTK or spaCy.
*   Implement different RNN architectures (GRU, Bi-LSTM) for better performance.
*   Fine-tune the model on a larger dataset for greater accuracy.
*   Add more sophisticated emoji integration based on sentiment score ranges.
*   Deploy using another service if the limitations are too high.

## Contributing

Contributions are welcome! Please feel free to submit pull requests to improve this project.
