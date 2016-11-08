'''
Created on Oct 29, 2016

@author: alexei.minin
'''

from rest_framework import serializers
from moonShot_structure import models


class LotterySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lottery

class DrawSerializer(serializers.ModelSerializer):
    lottery = LotterySerializer(read_only = True)
    
    class Meta:
        model = models.Draw
      



