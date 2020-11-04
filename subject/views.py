from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from schoolclass.models import TClass
from teacherlogin.models import Teacher
import json

# Create your views here.


class AddSubject(View):
    def post(self, request):
        data = request.body.decode()
        data = json.loads(data)
        print(data)
        teach_class = data.get("teach_class")
        teacher_name = data.get("teacher_name")
        print(teacher_name)
        try:
            c_id = TClass.objects.get(class_name=teach_class).get_class()
            print(c_id)
            t_id = Teacher.objects.get(teacher_name=teacher_name).get_teacher()
            print(t_id)
            return JsonResponse(data)
        except Exception as e:
            return HttpResponse("班级不存在!")

