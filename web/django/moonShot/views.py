'''
Created on Oct 29, 2016

@author: alexei.minin
'''
from django.template.response import TemplateResponse
    
    
def show_angular_client_app(request):
    return TemplateResponse(request, 'front_end/index.html')