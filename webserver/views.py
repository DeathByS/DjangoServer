from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from webserver.serializers import InfoDataSerializer, DCDataSerializer, AlarmDataSerializer, OperatingTimeDataSerializer, OperatingDataSerializer 
from webserver.serializers import AbnormalSignSerializer, EmailDataSerializer, SludgeInOutDataSerializer
from webserver.models import InfoData, DCData, AlarmData, OperatingTimeData, OperatingData, AbnormalSignData, EmailData, SludgeInOutData 
# from webserver.models import DCData

# Create your views here.



class InfoDataViewSet(viewsets.ModelViewSet): 
    queryset = InfoData.objects.all()
    serializer_class = InfoDataSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'id' : ['exact', 'in', 'range'], 
                   'machineName' : ['exact'],
                   'timeData' : ['exact', 'range']}    

class DCDataViewSet(viewsets.ModelViewSet): 
    queryset = DCData.objects.all()
    serializer_class = DCDataSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'id' : ['exact', 'in', 'range'], 
                   'machineName' : ['exact'],
                   'timeData' : ['exact', 'range']}       


class AlarmDataViewSet(viewsets.ModelViewSet): 
    queryset = AlarmData.objects.all()
    serializer_class = AlarmDataSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'id' : ['exact', 'in', 'range'], 
                   'machineName' : ['exact'],
                   'timeData' : ['exact', 'range']}

class AbnormalSignDataViewSet(viewsets.ModelViewSet): 
    queryset = AbnormalSignData.objects.all()
    serializer_class = AbnormalSignSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'id' : ['exact', 'in', 'range'], 
                   'machineName' : ['exact'],
                   'timeData' : ['exact', 'range']}


class OperatingTimeDataViewSet(viewsets.ModelViewSet): 
    queryset = OperatingTimeData.objects.all()
    serializer_class = OperatingTimeDataSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'id' : ['exact', 'in', 'range'], 
                   'machineName' : ['exact'],
                   'timeData' : ['exact', 'range']}    

class OperatingDataViewSet(viewsets.ModelViewSet): 
    queryset = OperatingData.objects.all()
    serializer_class = OperatingDataSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'id' : ['exact', 'in', 'range'], 
                   'machineName' : ['exact'],
                   'opName' : ['exact'],
                   'colIndex' : ['exact'],
                   }

class EmailDataViewSet(viewsets.ModelViewSet):
    queryset = EmailData.objects.all()
    serializer_class = EmailDataSerializer
    ilter_backends = (DjangoFilterBackend,)
    filter_fields = {'id' : ['exact'], 
                   'machineName' : ['exact'],
                   'replacePartEmail' : ['exact'],
                   'sludgeOutEmail' : ['exact'],
                   'expendablesPartEmail' : ['exact'],
                   'productionPartEmail' : ['exact'],
                   }

class SludgeInOutDataViewSet(viewsets.ModelViewSet):
    queryset = SludgeInOutData.objects.all()
    serializer_class = SludgeInOutDataSerializer
    ilter_backends = (DjangoFilterBackend,)
    filter_fields = {'id' : ['exact'], 
                   'machineName' : ['exact'],
                   }                   
                     

    # def list(self, request, *args, **kwargs):
    #     # data = super().list(request, args, kwargs)
    #     queryset = self.filter_queryset(self.get_queryset())




