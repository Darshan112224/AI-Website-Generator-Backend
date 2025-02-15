from django.urls import path
from . import views

urlpatterns = [
    path('generate_website/', views.generate_website, name='generate_website'),
]
