from django.db import models

# Create your models here.


class TempStu(models.Model):
    stu_num = models.IntegerField()
    stu_name = models.CharField(max_length=50)
    stu_class = models.CharField(max_length=50)

    class Meta:
        db_table = 'tempstudent'
        ordering = ['id']
