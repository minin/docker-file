'''
Created on Oct 29, 2016

@author: alexei.minin
'''

from __future__ import unicode_literals
from django.conf import settings
from django.db import models


    
    
class Lottery(models.Model):
    '''
    lottery table
    '''
    title = models.CharField(max_length = settings.MAX_CHAR_SIZE, unique=True) # There are lotteries with different ids and same names.
    def __str__(self):
        return self.title
    
      
    
class Draw(models.Model):
    '''
    draw table
    '''
    title = models.CharField(max_length = settings.MAX_CHAR_SIZE, db_index=True)
    jackpot = models.CharField(max_length = settings.MAX_CHAR_SIZE, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, editable=True, blank=True, null=True)
    date = models.CharField(max_length = settings.MAX_CHAR_SIZE, blank=True, null=True)
    lottery = models.ForeignKey(Lottery)
    
    def __str__(self):
        return self.title        
    
    
