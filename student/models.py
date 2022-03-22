from django.db import models

# Create your models here.
class studentinformation(models.Model):
    Student_name=models.CharField(max_length=200)
    Fathers_name=models.CharField(max_length=200)
    Mother_name=models.CharField(max_length=200)
    Email=models.CharField(max_length=100)
    Phone_no=models.CharField(max_length=100)

    def __str__(self):
        return self.name