# flask for backend like connecting the html file and notebook

from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained model
model, le = joblib.load("iris_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    #Use same feature names as training
    input_data = pd.DataFrame([[sepal_length, sepal_width,
                                petal_length, petal_width]],
                              columns=model.feature_names_in_)

    prediction = model.predict(input_data)
    prediction = le.inverse_transform(prediction)

    return render_template("index.html",
                           prediction_text=f"Predicted Species: {prediction[0]}")


if __name__ == "__main__":
    app.run(debug=True)