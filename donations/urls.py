from donations import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('donations/mosaic', views.get_donations_mosaic),
    path('donations/screenleaves', views.get_donations_screen_leaves),
    path('donations/christmaslandingpage', views.get_donations_christmas_landing_page),
    path('donations/cat-dog', views.get_donations_cat_dog),
]
