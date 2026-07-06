# Rising-waters
Machine Learning based Flood Prediction System using Flask
# 🌊 Flood Prediction System

## 📌 Project Overview

The Flood Prediction System is a Machine Learning-based web application that predicts the possibility of floods based on weather and rainfall parameters. The application uses a trained machine learning model integrated with a Flask web application to provide real-time flood predictions.

---

## 🚀 Features

- Predicts flood occurrence using Machine Learning.
- User-friendly web interface built with Flask.
- Accepts weather and rainfall parameters.
- Displays prediction results instantly.
- Responsive and simple interface.

---

## 🛠 Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- NumPy
- Pandas
- Scikit-learn
- Joblib

---

## 📂 Project Structure

```
Flood-Prediction-System/
│
├── app.py
├── floods.save
├── flood prediction.ipynb
├── flood prediction - 2.ipynb
├── templates/
│   ├── home.html
│   ├── index.html
│   ├── chance.html
│   └── no_chance.html
│
├── static/
│   ├── main.css
│   └── main.js
│
└── README.md
```

---

## ⚙ Installation

1. Clone the repository

```bash
git clone https://github.com/rupasri43/Rising waters.git
```

2. Install the required libraries

```bash
pip install -r requirements.txt
```

3. Run the Flask application

```bash
python app.py
```

4. Open your browser

```
http://127.0.0.1:5000
```

---

## 📊 Input Parameters

- Temperature
- Humidity
- Cloud Cover
- Annual Rainfall
- Jan-Feb Rainfall
- Mar-May Rainfall
- Jun-Sep Rainfall
- Oct-Dec Rainfall
- Average June Rainfall
- Sub Rainfall

---

## 📈 Output

The application predicts:

- ✅ No Chance of Flood
- ⚠ High Chance of Flood

---

## 🎯 Future Improvements

- Live weather API integration
- Interactive dashboard
- GIS-based flood visualization
- Mobile application support

## 📜 License

This project is developed for academic purposes.
