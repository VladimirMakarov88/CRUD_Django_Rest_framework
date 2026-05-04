from django.contrib import admin
from django.urls import path, include

from measurements import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('measurements.urls')),
]
