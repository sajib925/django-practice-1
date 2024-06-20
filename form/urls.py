from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('practice/', views.practice_form_view, name='practice_form'),
    path('model/', views.model_form_view, name='model_form'),
    
]
