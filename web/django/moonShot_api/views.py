'''
Created on Oct 29, 2016

@author: alexei.minin
'''

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from moonShot_api.serializers import DrawSerializer, LotterySerializer
from moonShot_structure.models import Lottery, Draw
from rest_framework.response import Response
from moonShot_structure.tasks import get_lottery_data
from django.http import HttpResponse

class DrawViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing draws.
    """
    queryset = Draw.objects.all()
    serializer_class = DrawSerializer
    permission_classes = [AllowAny]
    
    #update lottery filed in draw model.
    def update(self, request, pk=None):
        try:
            draw_obj = self.queryset.get(id = pk)
            new_lottery = request.data.get('lottery')
            draw_obj.lottery_id = new_lottery
            draw_obj.save()
            json_data = self.serializer_class(draw_obj)
            return Response(json_data.data)
        except Exception as e:
            raise
    
class LotteryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing lotteries.
    """
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializer
    permission_classes = [AllowAny]


def init_data(request):
    get_lottery_data()
    return HttpResponse(status=201)
