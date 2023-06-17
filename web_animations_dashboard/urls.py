from donations import urls
from django.urls import path, include
from django.contrib import admin
admin.site.site_header = "Animations Dashboard"
admin.site.site_title = "Animations Dashboard"
admin.site.site_url = '/'
admin.site.index_title = "Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('donations.urls')),
]
