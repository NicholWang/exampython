from django.db import models
from schoolclass.models import TClass


# Create your models here.


class Teacher(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    teacher_num = models.IntegerField()
    teacher_name = models.CharField(max_length=50)
    account_type = models.CharField(max_length=8)
    teach_class = models.ManyToManyField(TClass)

    class Meta:
        db_table = "teacher"

    def get_teacher(self):
        return {
            'teacher_name': self.teacher_name,
            'teacher_id': self.id
        }

