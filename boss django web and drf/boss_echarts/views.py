from django.shortcuts import render
import json
# Create your views here.
from django.db.models.aggregates import Count,Sum,Func
from django.db.models import DateTimeField, ExpressionWrapper, F
from django.views.generic.base import View
from .models import  Boss,refined_boss
from  utils.regex_data import *
import collections



class IndexView(View):
    def get(self,request,chart_name):
        if chart_name =="coding_language":
            ave_min_salary=[]
            ave_max_salary=[]
            legendData=[]
            seriesData=[]
            selected={}
            total = refined_boss.objects.values("job_name").annotate(count_num=Count("id"), sum_min=Sum("salary_min"), sum_max=Sum("salary_max")).values("job_name","count_num","sum_min","sum_max")
            for i in total:
                legendData.append(i["job_name"])
                seriesData.append({"name":i["job_name"],"value":i["count_num"]})
                selected[i["job_name"]]=True
                ave_min_salary.append(i["sum_min"]/i["count_num"])
                ave_max_salary.append(i["sum_max"]/i["count_num"])
            data = {"legendData": json.dumps(legendData), "seriesData": json.dumps(seriesData), "selected": json.dumps(selected)}
            data["salary_min"] = ave_min_salary
            data["salary_max"] = ave_max_salary
            return  render(request, "boss_echarts/coding_language.html", data)

        if chart_name =="experience":
            total = refined_boss.objects.values("job_name", "experience").annotate(count_num=Count("id"),sum_min=Sum("salary_min"),sum_max=Sum("salary_max")).values("job_name", "experience", "count_num", "sum_min", "sum_max")
            language=["python","c","java"]
            exp_all = ["经验不限","应届生","1年以内","1-3年","3-5年","5-10年","10年以上"]

            # experience_tmp = refined_boss.objects.values("experience").distinct().all()
            # for i in experience_tmp:
            #     exp_all.append(i["experience"])

            python_num = []
            c_num = []
            java_num = []

            python_smin=[]
            c_smin = []
            java_smin=[]

            python_smax = []
            c_smax = []
            java_smax = []
            for i in exp_all:
                try:
                    python_num.append(total.get(job_name="python",experience=i)["count_num"])
                    python_smin.append(total.get(job_name="python", experience=i)["sum_min"]/total.get(job_name="python", experience=i)["count_num"])
                    python_smax.append(total.get(job_name="python", experience=i)["sum_max"]/total.get(job_name="python", experience=i)["count_num"])

                except Exception as e:
                    python_num.append(0)
                    python_smin.append(0)
                    python_smax.append(0)
                try:
                    c_num.append(total.get(job_name="c", experience=i)["count_num"])
                    c_smin.append(total.get(job_name="c", experience=i)["sum_min"]/total.get(job_name="c", experience=i)["count_num"])
                    c_smax.append(total.get(job_name="c", experience=i)["sum_max"]/total.get(job_name="c", experience=i)["count_num"])

                except Exception as e:
                    c_num.append(0)
                    c_smin.append(0)
                    c_smax.append(0)
                try:
                    java_num.append(total.get(job_name="java", experience=i)["count_num"])
                    java_smin.append(total.get(job_name="java", experience=i)["sum_min"]/total.get(job_name="java", experience=i)["count_num"])
                    java_smax.append(total.get(job_name="java", experience=i)["sum_max"]/total.get(job_name="java", experience=i)["count_num"])

                except Exception as e:
                    java_num.append(0)
                    java_smin.append(0)
                    java_smax.append(0)

            data = {"language": json.dumps(language), }
            data["python_num"]=json.dumps(python_num)
            data["python_smin"] = json.dumps(python_smin)
            data["python_smax"] = json.dumps(python_smax)
            data["c_num"] = json.dumps(c_num)
            data["c_smin"] = json.dumps(c_smin)
            data["c_smax"] = json.dumps(c_smax)
            data["java_num"] = json.dumps(java_num)
            data["java_smin"] = json.dumps(java_smin)
            data["java_smax"] = json.dumps(java_smax)
            data["exp_all"]=json.dumps(exp_all)
            return render(request,"boss_echarts/experience.html",data)

        if chart_name == "education":
            total = refined_boss.objects.values("job_name", "education").annotate(count_num=Count("id"),
                                                                                   sum_min=Sum("salary_min"),
                                                                                   sum_max=Sum("salary_max")).values(
                "job_name", "education", "count_num", "sum_min", "sum_max")
            language = ["python", "c", "java"]
            edu_all = ["学历不限", "高中", "大专", "本科", "硕士",]

            # edu_tmp = refined_boss.objects.values("education").distinct().all()
            # for i in experience_tmp:
            #     edu_all.append(i["education"])

            python_num = []
            c_num = []
            java_num = []

            python_smin = []
            c_smin = []
            java_smin = []

            python_smax = []
            c_smax = []
            java_smax = []
            for i in edu_all:
                try:
                    python_num.append(total.get(job_name="python", education=i)["count_num"])
                    python_smin.append(total.get(job_name="python", education=i)["sum_min"]/total.get(job_name="python", education=i)["count_num"])
                    python_smax.append(total.get(job_name="python", education=i)["sum_max"]/total.get(job_name="python", education=i)["count_num"])

                except Exception as e:
                    python_num.append(0)
                    python_smin.append(0)
                    python_smax.append(0)
                try:
                    c_num.append(total.get(job_name="c", education=i)["count_num"])
                    c_smin.append(total.get(job_name="c", education=i)["sum_min"]/total.get(job_name="c", education=i)["count_num"])
                    c_smax.append(total.get(job_name="c", education=i)["sum_max"]/total.get(job_name="c", education=i)["count_num"])

                except Exception as e:
                    c_num.append(0)
                    c_smin.append(0)
                    c_smax.append(0)
                try:
                    java_num.append(total.get(job_name="java", education=i)["count_num"])
                    java_smin.append(total.get(job_name="java", education=i)["sum_min"]/total.get(job_name="java", education=i)["count_num"])
                    java_smax.append(total.get(job_name="java", education=i)["sum_max"]/total.get(job_name="java", education=i)["count_num"])

                except Exception as e:
                    java_num.append(0)
                    java_smin.append(0)
                    java_smax.append(0)

            data = {"language": json.dumps(language), }
            data["python_num"] = json.dumps(python_num)
            data["python_smin"] = json.dumps(python_smin)
            data["python_smax"] = json.dumps(python_smax)
            data["c_num"] = json.dumps(c_num)
            data["c_smin"] = json.dumps(c_smin)
            data["c_smax"] = json.dumps(c_smax)
            data["java_num"] = json.dumps(java_num)
            data["java_smin"] = json.dumps(java_smin)
            data["java_smax"] = json.dumps(java_smax)
            data["edu_all"] = json.dumps(edu_all)
            return render(request, "boss_echarts/education.html", data)



