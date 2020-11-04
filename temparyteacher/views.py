from django.shortcuts import render
from django.views.generic import View
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import TempTeacher
from page.index import get_page
import json

# Create your views here.


class GetTempTeacher(View):
    def get(self, request):
        page_num = request.GET.get('page_num')
        print(page_num)
        try:
            data = get_page(TempTeacher, page_num)
            data = serializers.serialize('json', data)
            return JsonResponse(data, safe=False)
        except Exception as e:
            return HttpResponse("page dont't exist")


class AddTempTeacher(View):
    def post(self, request):
        data = request.body.decode()
        data = json.loads(data)
        print(data)
        try:
            TempTeacher.objects.create(**data)
            print('增加成功')
            return HttpResponse('success')
        except Exception as e:
            print("增加失败")
            return HttpResponse('failed')


class DelTempTeacher(View):
    def get(self, request):
        data = request.GET.get('teacher_num')
        try:
            TempTeacher.objects.filter(teacher_num=data).delete()
            return HttpResponse('success')
        except Exception as e:
            return HttpResponse('failed')

