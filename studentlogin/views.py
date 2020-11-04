from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .models import Student
from schoolclass.models import TClass
from temparystudent.models import TempStu
from validmail.index import is_valid
import json
# Create your views here.


class StudentLogin(View):
    def post(self, request):
        data = request.body.decode()
        data = json.loads(data)
        stu_num = data.get('stu_num')
        stu_name = data.get('stu_name')
        class_name = data.get('class_name')
        email = data.get("email")
        valid = is_valid(email)
        if not valid:
            return HttpResponse("邮箱格式错误,请重新填写邮箱")
        try:
            TempStu.objects.get(stu_name=stu_name)
        except Exception as e:
            return HttpResponse("系统中没有您的信息,您没有注册权限")
        try:
            TempStu.objects.get(stu_num=stu_num, stu_name=stu_name)
        except Exception as e:
            return HttpResponse("学号错误,请重新填写")
        try:
            ret_obj = TClass.objects.get(class_name=class_name)
            ret = ret_obj.get_class()
            data.pop('class_name')
            data['stu_class_id'] = ret_obj
            print('data',data)
            Student.objects.create(**data)
            return HttpResponse("success")
        except Exception as e:
            print(e)
            return HttpResponse("班级不存在,请重新填写班级")
