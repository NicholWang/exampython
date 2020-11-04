from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .models import Teacher
from temparyteacher.models import TempTeacher
from validmail.index import is_valid
import json
import os

# Create your views here.


class LoginView(View):
    def post(self, request):
        data = request.body.decode()
        data = json.loads(data)
        email = data.get('email')
        teacher_num = data.get('teacher_num')
        teacher_name = data.get('teacher_name')
        ret = is_valid(email)
        if not ret:
            return HttpResponse('邮箱格式错误')
        try:
            TempTeacher.objects.get(teacher_num=teacher_num)
        except Exception as e:
            print(e)
            return HttpResponse("系统中没有您的信息,您没有注册权限")
        try:
            TempTeacher.objects.get(teacher_name=teacher_name)
            Teacher.objects.create(**data)
            return HttpResponse('success')
        except Exception as e:
            return HttpResponse('您的姓名信息有误,请重新填写姓名')