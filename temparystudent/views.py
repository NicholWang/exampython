from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from schoolclass.models import TClass
from .models import TempStu
from page.index import get_page
import json
# Create your views here.


class GetTempStu(View):
    def get(self, request):
        page_num = request.GET.get('page_num')
        print(page_num)
        try:
            data = get_page(TempStu, page_num)
            data = serializers.serialize('json', data)
            return JsonResponse(data, safe=False)
        except Exception as e:
            return HttpResponse("page dont't exist")


class AddTempStu(View):
    def post(self, request):
        data = request.body.decode()
        data = json.loads(data)
        stu_class = data.get('stu_class')
        print(stu_class)
        try:
            ret = TClass.objects.get(class_name=stu_class)
            TempStu.objects.create(**data)
            return HttpResponse('success')
        except Exception as e:
            return HttpResponse('failed')


class DelTempStu(View):
    def get(self, request):
        data = request.GET.get('stu_num')
        print(data)
        try:
            ret = TempStu.objects.filter(stu_num=data).delete()
            print(ret)
            return HttpResponse('success')
        except Exception as e:
            return HttpResponse('failed')
