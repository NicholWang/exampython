from django.db import models

# Create your models here.


class TClass(models.Model):
    class_name = models.CharField(max_length=60)
    stu_count = models.IntegerField()

    class Meta:
        db_table = "t_class"
        ordering = ['id']

    def get_class(self):
        return {
            'class_id': self.id
        }
