from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

model_path = os.path.join(os.getcwd(), 'sentiment_model.pkl')
vectorizer_path = os.path.join(os.getcwd(), 'vectorizer.pkl')

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    print("Model and vectorizer loaded successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}")
    raise FileNotFoundError("Ensure 'sentiment_model.pkl' and 'vectorizer.pkl' are in the working directory.")

@app.route("/", methods=["GET"])
def read_form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def predict():
    text = request.form["text"]
    try:
        processed_text = vectorizer.transform([text])
        prediction = model.predict(processed_text)[0]
        sentiment = "Positive" if prediction.lower() == "positive" else "Negative"
        return render_template("result.html", sentiment=sentiment)
    except Exception as e:
        return render_template("error.html", error_message=str(e))

if __name__ == "__main__":
    app.run(debug=True)
