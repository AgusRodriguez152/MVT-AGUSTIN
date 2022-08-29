
from django.urls import path
from AppFamilia.views import *

urlpatterns = [
    path("familiar/", familiar),
    path("familiar1/", familiar1),
    path("familiar2/", familiar2),
    path("familiares/", familiares),
    path("familiares1/", familiares1),
    path("familiares2/", familiares2),
    path("", Inicio),
    
]