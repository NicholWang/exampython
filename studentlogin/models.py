from django.db import models
from schoolclass.models import TClass

# Create your models here.


class Student(models.Model):
    stu_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    stu_num = models.IntegerField()
    stu_class_id = models.ForeignKey(TClass, on_delete=models.CASCADE)
    class Meta:
        db_table = 'student'
        ordering = ['id']

    def get_stu(self):
        return {
            'stu_name': self.stu_name
        }