from django.contrib import admin
from django.urls import path

from measurements import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', views.create_sensor, name='sensors_create'),
    path('sensors/<int:pk>/', views.update_sensor, name='update-sensor'),
    path('measurements/', views.add_measurement, name='add_measurement'),
    path('sensors/list/', views.get_sensors_list, name='get_sensors_list'),
    path('sensors/<int:pk>/detail/', views.get_sensors_detail, name='sensor-detail'),
]