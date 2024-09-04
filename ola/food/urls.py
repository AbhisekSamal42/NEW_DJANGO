from django.urls import path
from food.views import *

app_name='foodies'

urlpatterns=[
    path('mahaprasad/',mahaprasad,name='mahaprasad'),
]