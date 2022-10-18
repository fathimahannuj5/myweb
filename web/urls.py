from django.urls import path,include
from . import views

urlpatterns = [
   path('cofeebar/',views.MyCofee,name='cofeebar'),
]
