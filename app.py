from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("floods.save")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict_page")
def predict_page():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = [
        float(request.form["Temp"]),
        float(request.form["Humidity"]),
        float(request.form["Cloud_Cover"]),
        float(request.form["ANNUAL"]),
        float(request.form["Jan_Feb"]),
        float(request.form["Mar_May"]),
        float(request.form["Jun_Sep"]),
        float(request.form["Oct_Dec"]),
        float(request.form["avgjune"]),
        float(request.form["sub"])
    ]

    prediction = model.predict([data])

    if prediction[0] == 1:
        return render_template("chance.html")
    else:
        return render_template("no_chance.html")


if __name__ == "__main__":
    app.run(debug=True)