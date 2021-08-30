from django.db.models import fields
from rest_framework import serializers
from . models import *

class student_details_serializer(serializers.ModelSerializer):
    class Meta:
        model = student_details
        fields="__all__"