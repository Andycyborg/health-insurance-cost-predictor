from django.urls import path
from . import views


app_name = 'predictor'


urlpatterns = [
    path(
        '',
        views.predict_charge,
        name='predict_charge'
    ),
]