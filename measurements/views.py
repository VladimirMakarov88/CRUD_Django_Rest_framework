from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from measurements.models import Sensor
from measurements.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


@api_view(['POST'])
def create_sensor(request):
    serializer = SensorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PATCH'])
def update_sensor(request, pk):
    sensor = get_object_or_404(Sensor, pk=pk)
    serializer = SensorSerializer(sensor, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def add_measurement(request):
    sensor_id = request.data.get('sensor')
    if sensor_id:
        get_object_or_404(Sensor, pk=sensor_id)
    serializer = MeasurementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def get_sensors_list(request):
    sensors = Sensor.objects.all()
    serializer = SensorSerializer(sensors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_sensors_detail(request, pk):
    sensor = get_object_or_404(Sensor, pk=pk)
    serializer = SensorDetailSerializer(sensor)
    return Response(serializer.data)