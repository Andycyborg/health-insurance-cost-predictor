# Health Insurance Charge Predictor 🏥💰

A full-stack web application built with **Django** and **Scikit-Learn** that predicts estimated annual medical health insurance charges using machine learning regression models.

---

## 🚀 Live Demo

- **Hosted Web App:** 

---

## ✨ Features

- **Interactive UI:** Clean, responsive form interface for user inputs (Age, BMI, Smoking Status, Region, etc.).
- **Machine Learning Engine:** Leverages a pre-trained regression model (`joblib`) with feature engineering and standard scaling.
- **Real-Time Predictions:** Instant valuation rendering directly on the web interface.
- **Production-Ready Deployment:** Configured with Gunicorn and WhiteNoise for smooth deployment on Render.

---

## 🛠️ Tech Stack

- **Backend Framework:** Django (Python 3)
- **Machine Learning:** Scikit-Learn, Pandas, Joblib
- **Frontend:** HTML5, CSS3, JavaScript
- **Production Server:** Gunicorn, WhiteNoise

---

## 📁 Project Structure

```text
HealthInsurancePrediction/
│
├── ml_models/
│   ├── insurance_model.joblib   # Trained ML model
│   └── scaler.joblib            # Feature scaler
│
├── mlModel/                     # Core Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── predictor/                   # Django app
│   ├── templates/               # UI HTML templates
│   ├── views.py                 # Prediction logic & scaling
│   └── urls.py
│
├── staticfiles/                 # Static assets for production
├── manage.py
└── requirements.txt             # Python dependencies