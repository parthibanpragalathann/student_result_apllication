from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField

# Create your models here.
class student_details(models.Model):
    Name=CharField(max_length=200,blank=True)
    RollNumber=CharField(unique=True,max_length=100,blank=True,null=True)
    DateofBirth=DateField(help_text="Date of Birth",blank=True)
    marks=IntegerField(default=0,blank=True, null=True)