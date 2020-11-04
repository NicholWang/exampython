from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from schoolclass.models import TClass
from teacherlogin.models import Teacher
from .models import Subject
import json

# Create your views here.


class GetSubject(View):
    def get(self, request):
        teacher_name = request.GET.get('teacher_name')
        print('teacher_name:', teacher_name)
        ret_data = []
        # 通过教师名去查询教师所教授的班级
        ret_teacher = Teacher.objects.get(teacher_name=teacher_name)
        relate_classlist = ret_teacher.teach_class.all()
        # print(relate_classlist)
        for rc in relate_classlist:
            # 通过遍历班级去查看对应的班级课程
            relate_courselist = rc.subject_set.all()
            print(relate_courselist)
            for rl in relate_courselist:
                ret_dict = {}
                ret_dict["teacher_name"] = teacher_name
                ret_dict['teach_class'] = rc.get_class().get('class_name')
                ret_subject_info = rl.get_subject()
                if ret_subject_info.get('teacher_name') == teacher_name:
                    for attr, value in ret_subject_info.items():
                        ret_dict[attr] = value
                    ret_data.append(ret_dict)
            # print(rc.get_class())

        return JsonResponse(ret_data, safe=False)



class AddSubject(View):
    def post(self, request):
        data = request.body.decode()
        data = json.loads(data)
        print(data)
        teach_class = data.get("teach_class")
        teacher_name = data.get("teacher_name")
        print(teacher_name)
        try:
            ret_class = TClass.objects.get(class_name=teach_class)
            # print(c_id)
            ret_teacher = Teacher.objects.get(teacher_name=teacher_name)
            # print(t_id)

            ret_teacher.teach_class.add(ret_class)
            data.pop('teach_class')
            # data.pop('teacher_name')
            ret_subject = Subject.objects.create(**data)
            ret_subject.subject_class.add(ret_class)
            return JsonResponse(data)
        except Exception as e:
            return HttpResponse("班级不存在!")

