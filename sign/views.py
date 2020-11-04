from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from studentlogin.models import Student
from teacherlogin.models import Teacher
import json


class SignView(View):

    def post(self, request):
        data = request.body.decode()
        data = json.loads(data)
        print(data)
        email = data.get("email")
        password = data.get("password")
        if email == 'root123456@qq.com' and password == '1213wz06&':
            ret = {
                'user': '管理员',
                'type': '管理'
            }
            return JsonResponse(ret)
        else:
            try:
                ret_obj = Student.objects.get(email=email,password=password).get_stu()
                ret = {
                    'user': ret_obj['stu_name'],
                    'type': '学生'
                }
                return JsonResponse(ret)
            except Exception as e:
                print(e)
            try:
                ret_obj = Teacher.objects.get(email=email, password=password).get_teacher()
                ret = {
                    'user': ret_obj['teacher_name'],
                    'type': '教师'
                }
                return JsonResponse(ret)
            except Exception as e:
                print(e)
                return HttpResponse("failed")
