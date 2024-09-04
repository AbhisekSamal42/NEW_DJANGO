from django.urls import path
from MI.views import*
urlpatterns=[
    path('Captian/',Captian,name='Captian'),
    path('Vicecaptian/',Vicecaptian,name='Vicecaptian'),
]