from django.urls import path
from CSK.views import*
urlpatterns=[
    path('Captian/',Captian,name='Captian'),
    path('Vicecaptian/',Vicecaptian,name='Vicecaptian'),
]