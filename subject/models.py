from django.db import models
from schoolclass.models import TClass

# Create your models here.


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_period = models.IntegerField()
    subject_character = models.CharField(max_length=20)
    teacher_name = models.CharField(max_length=50, null=True)
    subject_class = models.ManyToManyField(TClass)

    class Meta:
        db_table = 'subject'
        ordering = ['id']

    def get_subject(self):
        return {
            'subject_name': self.subject_name,
            'subject_period': self.subject_period,
            'subject_character': self.subject_character,
            'teacher_name': self.teacher_name
        }