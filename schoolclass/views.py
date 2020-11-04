from django.shortcuts import render
from django.views.generic import View
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import TClass
from page.index import get_page
import json
# Create your views here.


class AddClass(View):
    def post(self, request):
        req_data = request.body.decode()
        req_data = json.loads(req_data)
        class_entity = {
            'class_name': req_data.get('class_name'),
            'stu_count': req_data.get('stu_count')
        }
        TClass.objects.create(**class_entity)
        return JsonResponse(req_data)


class GetClass(View):
    def get(self, request):
        page_num = request.GET.get('page_num')
        print(page_num)
        try:
            data = get_page(TClass,page_num)
            data = serializers.serialize('json', data)
            return JsonResponse(data, safe=False)
        except Exception as e:
            return HttpResponse("page dont't exist")



class DelClass(View):
    def get(self, request):
        data = request.GET.get('class_name');
        print(data)
        try:
            TClass.objects.filter(class_name=data).delete()
            return HttpResponse('success')
        except Exception as e:
            return HttpResponse('failed')


class UpdateClass(View):
    def post(self, request):
        req_data = request.body.decode()
        req_data = json.loads(req_data)
        stu_count = req_data['stu_count']
        class_name = req_data['class_name']
        print(stu_count,class_name)
        try:
            TClass.objects.filter(class_name=class_name).update(stu_count=stu_count)
            return HttpResponse("success")
        except Exception as e:
            return HttpResponse('failed')

