from flask import Flask, render_template_string, request
import joblib
import os

app = Flask(__name__)

# Load the model and vectorizer
model_path = os.path.join(os.getcwd(), 'sentiment_model.pkl')
vectorizer_path = os.path.join(os.getcwd(), 'vectorizer.pkl')

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    print("Model and vectorizer loaded successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}")
    raise FileNotFoundError("Ensure 'sentiment_model.pkl' and 'vectorizer.pkl' are in the working directory.")

# Define a function for rendering the main form
def render_form():
    return """
    <html>
    <head>
        <title>Sentiment Analysis</title>
        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            body {
                background-color: #f0f4f8;
                color: #333;
                font-size: 16px;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 600px;
                padding: 30px;
                text-align: center;
            }
            h2 {
                color: #2c3e50;
                margin-bottom: 20px;
            }
            textarea {
                width: 100%;
                height: 150px;
                padding: 15px;
                border: 2px solid #ddd;
                border-radius: 8px;
                font-size: 16px;
                resize: none;
                margin-bottom: 20px;
                transition: border-color 0.3s ease;
            }
            textarea:focus {
                border-color: #4CAF50;
                outline: none;
            }
            .submit-btn {
                padding: 12px 30px;
                background-color: #4CAF50;
                color: #fff;
                border: none;
                border-radius: 8px;
                font-size: 18px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            .submit-btn:hover {
                background-color: #45a049;
            }
            .result {
                background-color: #ecf0f1;
                padding: 20px;
                margin-top: 30px;
                border-radius: 8px;
                font-size: 18px;
                color: #27ae60;
                font-weight: bold;
            }
            a {
                text-decoration: none;
                color: #2980b9;
                font-size: 16px;
                display: block;
                margin-top: 20px;
                font-weight: 600;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Sentiment Analysis</h2>
            <form method="POST" action="/predict">
                <textarea name="text" placeholder="Enter text here..." required></textarea><br>
                <button type="submit" class="submit-btn">Analyze Sentiment</button>
            </form>
        </div>
    </body>
    </html>
    """

# Define a function to render the result page
def render_result(sentiment):
    return f"""
    <html>
    <head>
        <title>Sentiment Analysis Result</title>
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            body {{
                background-color: #f0f4f8;
                color: #333;
                font-size: 16px;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .container {{
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 600px;
                padding: 30px;
                text-align: center;
            }}
            h2 {{
                color: #2c3e50;
                margin-bottom: 20px;
            }}
            .result {{
                background-color: #ecf0f1;
                padding: 20px;
                border-radius: 8px;
                font-size: 18px;
                color: #27ae60;
                font-weight: bold;
            }}
            a {{
                text-decoration: none;
                color: #2980b9;
                font-size: 16px;
                display: block;
                margin-top: 20px;
                font-weight: 600;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Sentiment Analysis Result</h2>
            <div class="result">Sentiment: {sentiment}</div>
            <a href="/">Back</a>
        </div>
    </body>
    </html>
    """

# Define a function to render error messages
def render_error(error_message):
    return f"""
    <html>
    <head>
        <title>Error</title>
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            body {{
                background-color: #f0f4f8;
                color: #333;
                font-size: 16px;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .container {{
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 600px;
                padding: 30px;
                text-align: center;
            }}
            h2 {{
                color: red;
            }}
            a {{
                text-decoration: none;
                color: #2980b9;
                font-size: 16px;
                display: block;
                margin-top: 20px;
                font-weight: 600;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Error: {error_message}</h2>
            <a href="/">Back</a>
        </div>
    </body>
    </html>
    """

@app.route("/", methods=["GET"])
def read_form():
    return render_form()

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["text"]
    try:
        # Transform input text
        processed_text = vectorizer.transform([text])
        # Predict sentiment
        prediction = model.predict(processed_text)[0]
        sentiment = "Positive" if prediction.lower() == "positive" else "Negative"
        return render_result(sentiment)
    
    except Exception as e:
        return render_error(str(e))

if __name__ == "__main__":
    app.run(debug=True)
