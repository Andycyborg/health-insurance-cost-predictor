import os
import joblib
import pandas as pd

from django.conf import settings
from django.shortcuts import render




MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    'ml_models',
    'insurance_model.joblib'
)

SCALER_PATH = os.path.join(
    settings.BASE_DIR,
    'ml_models',
    'scaler.joblib'
)

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)




def predict_charge(request):

    prediction = None
    error = None

    if request.method == 'POST':

        try:
            

            age = float(request.POST.get('age'))
            bmi = float(request.POST.get('bmi'))
            children = float(request.POST.get('children'))

            is_female = int(request.POST.get('is_female'))
            is_smoker = int(request.POST.get('is_smoker'))

            region = request.POST.get('region')


            

            region_southeast = (
                1 if region == 'southeast' else 0
            )

            region_northwest = (
                1 if region == 'northwest' else 0
            )

            bmi_category_Obese = (
                1 if bmi >= 30.0 else 0
            )


           

            raw_customer = pd.DataFrame([{
                'age': age,
                'is_female': is_female,
                'bmi': bmi,
                'children': children,
                'is_smoker': is_smoker,
                'region_southeast': region_southeast,
                'bmi_category_Obese': bmi_category_Obese,
                'region_northwest': region_northwest
            }])


            

            cols_to_scale = [
                'age',
                'bmi',
                'children'
            ]

            raw_customer[cols_to_scale] = scaler.transform(
                raw_customer[cols_to_scale]
            )


            

            feature_columns = [
                'age',
                'is_female',
                'bmi',
                'children',
                'is_smoker',
                'region_southeast',
                'bmi_category_Obese',
                'region_northwest'
            ]

            raw_customer = raw_customer[feature_columns]


            

            predicted_value = model.predict(
                raw_customer
            )[0]


            

            prediction = f"${predicted_value:,.2f}"


        except Exception as e:

            error = f"Prediction error: {str(e)}"


    return render(
        request,
        'predict.html',
        {
            'prediction': prediction,
            'error': error
        }
    )