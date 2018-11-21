from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import  Boss
from rest_framework import mixins

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boss
        fields = ('job_name', 'salary',"area","experience","education","industry","listed_info","employee_num","company_name","pub_date")