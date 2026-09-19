# Health Insurance Cost Predictor 🏥

An end-to-end Machine Learning web application built using **Django** and **Scikit-Learn** that estimates annual medical health insurance charges based on user demographic and health metrics[cite: 1, 2].

The model processes inputs directly through a custom feature processing pipeline—handling feature scaling and categorical encoding on the fly to render instant cost predictions[cite: 1].

---

## 🔗 Live Application

- **Live Web App:** [https://health-insurance-cost-predictor-l1g6.onrender.com/](https://health-insurance-cost-predictor-l1g6.onrender.com/)

---

## ✨ Features

- **Interactive Dashboard:** Clean, user-friendly form interface for inputting age, BMI, children, gender, smoking status, and region.
- **Real-Time ML Inference:** Instant predictions rendered on the UI without page-reload friction[cite: 1, 2].
- **Feature Engineering & Preprocessing:** Dynamically standardizes numeric values and creates one-hot encoded and derived features (such as `bmi_category_Obese`) matching the trained model requirements[cite: 1].
- **Production-Ready Setup:** Integrated with **WhiteNoise** for static asset management and **Gunicorn** for WSGI deployment on Render.

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Django[cite: 1]
- **Machine Learning & Data Processing:** Scikit-Learn, Pandas, NumPy, Joblib[cite: 1, 3, 4]
- **Frontend:** HTML5, CSS3[cite: 2]
- **Deployment & Web Server:** Gunicorn, WhiteNoise, Render

---

## 🧠 Model & Feature Pipeline Details

The underlying model uses a pre-trained **Linear Regression** model (`insurance_model.joblib`) along with a pre-fitted **StandardScaler** (`scaler.joblib`)[cite: 1, 3, 4].

The pipeline performs the following steps during each prediction request:
1. **Inputs Extracted:** Age, BMI, Children, Gender (`is_female`), Smoker Status (`is_smoker`), and Region[cite: 1].
2. **Derived Features Engineered:**
   - Regional flags (`region_southeast`, `region_northwest`)[cite: 1].
   - High-risk indicator `bmi_category_Obese` (triggered when $\text{BMI} \ge 30.0$)[cite: 1].
3. **Scaling:** Continuous variables (`age`, `bmi`, `children`) are transformed using the saved `StandardScaler`[cite: 1].
4. **Prediction:** Transformed features are fed into the model to produce the final currency-formatted prediction[cite: 1].

---

## 📁 Project Structure

```text
HealthInsurancePrediction/
│
├── ml_models/                   # Pre-trained ML artifacts
│   ├── insurance_model.joblib   # Linear regression model
│   └── scaler.joblib            # Fitted StandardScaler
│
├── mlModel/                     # Django root configuration
│   ├── settings.py              # App settings, WhiteNoise & production config
│   ├── urls.py                  # Global routing
│   └── wsgi.py                  # WSGI entrypoint for deployment
│
├── predictor/                   # Core application app
│   ├── migrations/              # Django migrations directory
│   ├── templates/
│   │   └── predict.html         # UI template for form and prediction display
│   ├── views.py                 # Core request logic, feature processing, & model execution
│   ├── urls.py                  # Predictor route mapping
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   └── tests.py
│
├── .gitignore                   # Version control exclusions
├── manage.py                    # Django management script
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies


---

## 👤 Author

Developed by **Anand Kumar Yadav**  
GitHub: [@Andycyborg](https://github.com/Andycyborg)

---