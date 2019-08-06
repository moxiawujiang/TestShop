

from django.views.generic.base import View
from django.http import JsonResponse
from django.core import serializers
from goods.models import Goods
#from django.views.generic import  ListView
import json

class GoodsListView(View):

    def get(self,request):
        goods=Goods.objects.all()[:5]

        json_data=serializers.serialize('json',goods)
        json_data=json.loads(json_data)
        return JsonResponse(json_data,safe=False)
