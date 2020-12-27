from django.shortcuts import render
from django.http import HttpResponse
from .models import Idcs, Cabinet
from .serializers import IdcSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


############################## 版本一 ##################################
def idc_list(request, *args, **kwargs):
    if  request.method == 'GET':
        queryset = Idcs.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        content = JSONRenderer().render(serializer.data)
        return HttpResponse(content, content_type='application/json')
    elif request.method == 'POST':
        content = JSONParser.parse(request)
        serializer = IdcSerializer(data=content)
        if serializer.is_valid():
            content = JSONRenderer().render(serializer.data)
            return HttpResponse(content, content_type='application/json')


def idc_detail(request, pk, *args, **kwargs):
    try:
        idc = Idcs.objects.get(pk=pk)
    except Idcs.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = IdcSerializer(idc)
        content = JSONRenderer().render(serializer.data)
        return HttpResponse(content, content_type='application/json')
    elif request.method == 'POST':
        content = JSONParser.parse(request)
        serializer = IdcSerializer(data=content)
        if serializer.is_valid():
            serializer.save()
            content = JSONRenderer().render(serializer.data)
            return HttpResponse(content, content_type='application/json')
        return HttpResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        idc.delete()
        return HttpResponse(status=204)

from rest_framework.decorators import api_view
from rest_framework import status


def idc_list_v2(request, *args, **kwargs):
    if request.method == 'GET':
        queryset = Idcs.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        content = JSONRenderer().render(serializer.data)
        return HttpResponse(content, content_type='application/json')
    elif request.method == 'POST':
