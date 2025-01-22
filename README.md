# Sentiment Analysis Web App

A simple web application that performs sentiment analysis using logistic regression to predict whether a given text has a positive, negative or neutral sentiment.

## Features

- Real-time sentiment analysis of user-provided text
- Binary classification (Positive/Negative) of text sentiment
- Simple and intuitive user interface
- Powered by a pre-trained logistic regression model

## Demo

Try the live demo at [https://sentiment-analysis-kzeu.onrender.com/](https://sentiment-analysis-kzeu.onrender.com/)

## Technologies Used

- **Flask**: Web application framework
- **scikit-learn**: Machine learning library for the sentiment analysis model
- **joblib**: Model serialization and loading
- **HTML/CSS**: Frontend interface
- **Render**: Cloud platform for deployment

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sentiment-analysis-webapp.git
cd sentiment-analysis-webapp
```

2. Create and activate a virtual environment (recommended):

Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Ensure the following files are in your project directory:
- `sentiment_model.pkl`: Trained logistic regression model
- `vectorizer.pkl`: Fitted text vectorizer

## Usage

1. Start the application locally:
```bash
python app.py
```

2. Open your web browser and navigate to `http://127.0.0.1:5000`

3. Enter text in the input field and click "Analyze Sentiment" to see the prediction

## Deployment on Render

This application is deployed on Render. Follow these steps to deploy your own instance:

1. **Prepare Your Repository**:
   - Ensure your repository includes:
     - `requirements.txt`
     - `app.py`
     - Model files (`sentiment_model.pkl` and `vectorizer.pkl`)
   - Your `app.py` should use `os.environ.get('PORT')` for the port number:
   ```python
   if __name__ == '__main__':
       port = int(os.environ.get('PORT', 5000))
       app.run(host='0.0.0.0', port=port)
   ```

2. **Deploy on Render**:
   - Sign up for a Render account at [render.com](https://render.com)
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository
   - Fill in the deployment details:
     - **Name**: Your app name
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `python app.py`
   - Choose your instance type (Free tier is available)
   - Click "Create Web Service"

3. **Environment Variables** (if needed):
   - Go to your web service dashboard
   - Click on "Environment"
   - Add any required environment variables

4. **Monitoring**:
   - Render provides logs and metrics in the dashboard
   - You can monitor your app's health and performance
   - Set up notifications for any issues
