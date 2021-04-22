from django.db import models
from django.utils import timezone
import time
from datetime import datetime


# Create your models here.


class InfoData(models.Model):

    objects = models.Manager()
    id                      =   models.AutoField(primary_key=True)
    timeData                =   models.DateTimeField(auto_now_add=True)
    machineName             =   models.CharField(max_length=100, default='')
    drumFrq                 =   models.FloatField(default=0.0)
    pressrollFrq            =   models.FloatField(default=0.0)
    sludgesupplyFrq         =   models.FloatField(default=0.0)
    sludgespreadFrq         =   models.FloatField(default=0.0)
    drumcolingWater         =   models.FloatField(default=0.0)
    transformersTemp        =   models.FloatField(default=0.0)
    sludgeInput             =   models.FloatField(default=0.0)
    sludgeOutput            =   models.FloatField(default=0.0)
    inputwaterRate          =   models.FloatField(default=0.0)
    outputwaterRate         =   models.FloatField(default=0.0)
    leftBalance             =   models.IntegerField(default=0)
    rightBalance            =   models.IntegerField(default=0)
    kW                      =   models.FloatField(default=0.0)



    def __str__(self):
        return 'InfoData'


class DCData(models.Model):

    objects = models.Manager()
    id                      =   models.AutoField(primary_key=True)
    timeData                =   models.DateTimeField(auto_now_add=True)
    machineName             =   models.CharField(max_length=100, default='')
    dcV                     =   models.FloatField(default=0.0)
    dcA                     =   models.FloatField(default=0.0)



    def __str__(self):
        return 'DCData'


class AlarmData(models.Model):

    objects = models.Manager()
    id                      =   models.AutoField(primary_key=True)
    timeData                =   models.DateTimeField(auto_now_add=True)
    machineName             =   models.CharField(max_length=100, default='')
    alarm                   =   models.CharField(max_length=500, default='')

    def __str__(self):
        return 'AlarmData'

class AbnormalSignData(models.Model):

    objects = models.Manager()
    id                      =   models.AutoField(primary_key=True)
    timeData                =   models.DateTimeField(auto_now_add=True)
    machineName             =   models.CharField(max_length=100, default='')
    alarm                   =   models.CharField(max_length=500, default='')

    def __str__(self):
        return 'AlarmData'        

class OperatingTimeData(models.Model):

    objects = models.Manager()
    id                      =   models.AutoField(primary_key=True)
    timeData                =   models.DateTimeField(auto_now_add=True)
    machineName             =   models.CharField(max_length=100, default='')
    totalOpTime             =   models.IntegerField(default=0) 
    drumCoating             =   models.IntegerField(default=0)
    sludgeScraper           =   models.IntegerField(default=0)
    filterCleaner           =   models.IntegerField(default=0)
    closeSensor             =   models.IntegerField(default=0)
    waterTankSensor         =   models.IntegerField(default=0)
    filter                  =   models.IntegerField(default=0)

class OperatingData(models.Model):

    objects = models.Manager()
    id                      =   models.AutoField(primary_key=True)
    colIndex                =   models.IntegerField(default=0)
    startingTime            =   models.CharField(max_length=500, default=timezone.now)
    machineName             =   models.CharField(max_length=100, default='')    
    opName                  =   models.CharField(max_length=100, default='')
    totalOpTime             =   models.IntegerField(default=0)
    referenceTime           =   models.IntegerField(default=0)
    alarmTime               =   models.IntegerField(default=0)


    
    def __str__(self):
        return 'OperatingData'

class EmailData(models.Model):

    objects = models.Manager()
    id                      =   models.AutoField(primary_key=True)
    machineName             =   models.CharField(max_length=100, default='')
    replacePartEmail        =   models.EmailField(max_length=100, default='')
    productionPartEmail     =   models.EmailField(max_length=100, default='')
    expendablesPartEmail    =   models.EmailField(max_length=100, default='')
    sludgeOutEmail          =   models.EmailField(max_length=100, default='')

    def __str__(self):
        return 'EmailData'        

class SludgeInOutData(models.Model):

    objects = models.Manager()
    id                      =   models.AutoField(primary_key=True)
    timeData                =   models.DateTimeField(auto_now_add=True)
    receiveTime             =   models.FloatField(default=0.0)
    machineName             =   models.CharField(max_length=100, default='')
    sludgeInput             =   models.FloatField(default=0.0)
    sludgeOutput            =   models.FloatField(default=0.0)
    

    def __str__(self):
        return 'SludgeInOutData'          
           
    