from django.shortcuts import render
from django.http import HttpResponse
from .models import Idcs, Cabinet
from .serializers import IdcSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def idc_list(request, *args, **kwargs):
    if  request.method == 'GET':
        queryset = Idcs.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        content = JSONRenderer().render(serializer.data)
        return HttpResponse(content, content_type='application/json')
    elif request.method == 'POST':
        data = JSONParser.parse(request)
