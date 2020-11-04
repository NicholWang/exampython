from django.db import models

# Create your models here.


class TempTeacher(models.Model):
    teacher_num = models.IntegerField()
    teacher_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'tempteacher'
        ordering =['id']
