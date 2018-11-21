import re
import datetime


def re_date(date_str):
    pattern = re.compile(r'发布于(.*)')
    m1 = pattern.match(date_str)
    if '月' in m1.group(1):
        pattern_date=re.compile(r'(\d+)月(\d+)日')
        month=pattern_date.match(m1.group(1)).group(1)
        date=pattern_date.match(m1.group(1)).group(2)

        # pub_date = datetime.datetime.strptime("2018-{}-{}".format(month,date),"%Y-%m-%d")
        pub_date=datetime.date(2018,int(month),int(date))
    elif ':' in m1.group(1):
        pub_date=datetime.date.today()
    elif '昨天' in m1.group(1):
        pub_date = datetime.date.today()-datetime.timedelta(days=1)
    return pub_date


def re_salary(salary_data):
    salary_pattern=re.compile(r"(\d+)k-(\d+)k")
    salary_min=salary_pattern.match(salary_data).group(1)
    salary_max=salary_pattern.match(salary_data).group(2)

    return int(salary_min),int(salary_max)

def re_experience(exp_data):
    try:
        experience_pattern=re.compile(r"(.*)年.*")
        exp_year=experience_pattern.match(exp_data).groups(1)[0]

        if '以上' in exp_data:
            exp_year=(int(exp_year))
        elif "以内" in exp_data:
            exp_year=-(int(exp_year))
        elif "-"  in exp_data:
            experience_pattern = re.compile(r"(\d+)-(\d+)")
            exp_year_min=int(experience_pattern.match(exp_year).group(1))
            exp_year_max=int(experience_pattern.match(exp_year).group(2))
        else:
            exp_year=0
    except Exception as e:
        exp_year = 0
    pass


def re_employee(exp_data):
    try:
        experience_pattern=re.compile(r"(.*)人.*")
        employee_num=experience_pattern.match(exp_data).groups(1)[0]

        if '以上' in exp_data:
            employee_num=(int(employee_num))

        elif "-"  in exp_data:
            experience_pattern = re.compile(r"(\d+)-(\d+)")
            employee_num_min=int(experience_pattern.match(employee_num).group(1))
            employee_num_max=int(experience_pattern.match(employee_num).group(2))
        else:
            employee_num=0
    except Exception as e:
        employee_num = 0
    pass

if __name__ == "__main__":
    str1="发布于10月24日"
    str2="发布于09:23"
    str3="发布于昨天"
    str4="8k-16k"
    str5="10年以上"
    str6="3-5年"
    str7="3年以内"
    str8="20-30人"
    str9="10000人以上"
    str10=""
    #
    # re_date(str1)
    # re_date(str2)
    # re_date(str3)
    #
    #
    #
    # re_experience(str5)
    # re_experience(str6)
    # re_experience(str7)
    # re_experience(r"经验不限")


    re_employee(str8)
    re_employee(str9)
    re_employee(str10)
    pass