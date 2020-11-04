from django.db import models

# Create your models here.


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_period = models.IntegerField()
    subject_character = models.CharField(max_length=20)
    class Meta:
        db_table = 'subject'
        ordering = ['id']
