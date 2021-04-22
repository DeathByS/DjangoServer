from webserver.models import InfoData, DCData, AlarmData, OperatingTimeData, OperatingData, AbnormalSignData, EmailData, SludgeInOutData
from rest_framework import serializers


class InfoDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InfoData
        fields = '__all__'

class DCDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DCData
        fields = '__all__'   

class AlarmDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlarmData
        fields = '__all__'   

class AbnormalSignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbnormalSignData
        fields = '__all__'       

class OperatingTimeDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OperatingTimeData
        fields = '__all__'   

class OperatingDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OperatingData
        fields = '__all__'    

class EmailDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailData 
        fields = '__all__'      

class SludgeInOutDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SludgeInOutData
        fields= '__all__'        

