from donations import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('donations/mosaic', views.get_donations_mosaic),
]
