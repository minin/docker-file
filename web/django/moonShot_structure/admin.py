'''
Created on Oct 29, 2016

@author: alexei.minin
'''
from django.contrib import admin
from moonShot_structure import models

'''
admin classes, can be edit for better display and content control.
'''
class LotteryAdmin(admin.ModelAdmin):
    pass

class DrawAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Draw, DrawAdmin)
admin.site.register(models.Lottery, LotteryAdmin)