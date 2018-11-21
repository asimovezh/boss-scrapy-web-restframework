from django.shortcuts import render
import json
# Create your views here.
from django.db.models.aggregates import Count,Sum,Func
from django.db.models import DateTimeField, ExpressionWrapper, F
import os
import django

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boss.settings")
django.setup()
from boss_echarts.models import  Boss,refined_boss
from utils.regex_data import  *




#
# java = Boss.objects.filter(job_name__contains="java")
#
# python = Boss.objects.filter(job_name__contains="python")
# c = Boss.objects.filter(job_name__contains="c")
# print(java.count(),python.count(),c.count())
# for i in java:
#     job_name="java"
#     pub_date=re_date(i.pub_date)
#     salary_min,salary_max=re_salary(i.salary)
#     u=refined_boss(raw_boss=i,job_name=job_name,pub_date=pub_date,salary_min=salary_min,salary_max=salary_max,experience=i.experience,education=i.education)
#     u.save()
# for i in python:
#     job_name="python"
#     pub_date=re_date(i.pub_date)
#     salary_min,salary_max=re_salary(i.salary)
#     u = refined_boss(raw_boss=i, job_name=job_name, pub_date=pub_date, salary_min=salary_min,salary_max=salary_max,experience=i.experience,education=i.education)
#     u.save()
#
# for i in c:
#     job_name="c"
#     pub_date=re_date(i.pub_date)
#     salary_min,salary_max=re_salary(i.salary)
#     u = refined_boss(raw_boss=i, job_name=job_name, pub_date=pub_date, salary_min=salary_min,salary_max=salary_max,experience=i.experience,education=i.education)
#     u.save()

education=refined_boss.objects.values("education").distinct()

pass



