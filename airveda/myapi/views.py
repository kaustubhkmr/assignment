from .models import Device, HumidityReading, TemperatureReading
from .serializers import DeviceSerializer, TemperatureReadingSerializer, HumidityReadingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import dateutil.parser 

@api_view(['GET','POST'])
def device_list(request):
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def device_detail(request,pk):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DeviceSerializer(device)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DeviceSerializer(device,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_readings(request,device,parameter):
    start_on = str(request.query_params.get('start_on'))
    end_on = str(request.query_params.get('end_on'))
    READING_VALUE = ['temperature', 'humidity']
    try:
        start_on = dateutil.parser.parse(start_on).strftime('%Y-%m-%d %H:%M:%S')
        end_on = dateutil.parser.parse(end_on).strftime('%Y-%m-%d %H:%M:%S')
        device_temp = Device.objects.get(pk=device)
        if(start_on>=end_on):
            raise ValueError('start date is before end date')
        if not(parameter in READING_VALUE):
            raise ValueError('parameter is wrong')
        return Response(get_data(device,parameter,start_on,end_on))
    except (ValueError,Device.DoesNotExist) as errors:
        return Response(str(errors),status=status.HTTP_400_BAD_REQUEST)

def get_data(device,parameter,start_on,end_on):
    if(parameter == 'temperature'):
       return TemperatureReadingSerializer(TemperatureReading.objects.filter(device__uid = device,date__gte=start_on,date__lte=end_on),many=True).data
    if(parameter == 'humidity'):
       return HumidityReadingSerializer(HumidityReading.objects.filter(device__uid = device,date__gte=start_on,date__lte=end_on),many=True).data