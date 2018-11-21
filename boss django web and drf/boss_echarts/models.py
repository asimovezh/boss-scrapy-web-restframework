# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from utils.regex_data import *
from utils.regex_data import *


class Boss(models.Model):

    id = models.CharField(unique=True,primary_key=True,max_length=100)
    job_name = models.CharField(blank=True, null=True,max_length=100)  # This field type is a guess.
    salary = models.CharField(blank=True, null=True,max_length=100)  # This field type is a guess.
    area = models.CharField(blank=True, null=True,max_length=100)  # This field type is a guess.
    experience = models.CharField(blank=True, null=True,max_length=100)  # This field type is a guess.
    education = models.CharField(blank=True, null=True,max_length=100)  # This field type is a guess.
    industry = models.CharField(blank=True, null=True,max_length=100)  # This field type is a guess.
    listed_info = models.CharField(blank=True, null=True,max_length=100)  # This field type is a guess.
    employee_num = models.CharField(blank=True, null=True,max_length=100)  # This field type is a guess.
    company_name = models.CharField(blank=True, null=True,max_length=100)  # This field type is a guess.
    pub_date = models.CharField(blank=True, null=True,max_length=100)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'boss'


    def get_min_max_salary(self):
        salary_min,salary_max=re_salary(self.salary)
        return [int(salary_min),int(salary_max)]


class refined_boss(models.Model):
    raw_boss=models.ForeignKey("Boss",on_delete=models.Case)
    job_name=models.CharField(blank=True, null=True,max_length=100)
    pub_date=models.DateField()
    salary_min=models.IntegerField()
    salary_max=models.IntegerField()
    experience=models.CharField(max_length=100,null=True)
    education = models.CharField(blank=True, null=True, max_length=100)

    class Meta:
        managed = True
        db_table = 'refined_boss'