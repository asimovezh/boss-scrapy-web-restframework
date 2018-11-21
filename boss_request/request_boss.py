#coding:utf-8
import requests
from bs4 import BeautifulSoup
import random
import sqlite3
import uuid
# html=requests.get("https://www.zhipin.com/")
#
# with open('test.html','wb+') as h:
#     for line in html.text:
#         line=line.encode('utf-8')
#         h.write(line)

start_url="https://www.zhipin.com/c101270100/?query={}&page={}&ka=page-next"
proxy_ip=["175.175.217.250:1133","118.190.95.35:9001","61.135.217.7:80","121.19.96.197:8118"]
proxies = {
    "http": "{}"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
}

ip_test_web="http://ip.filefab.com/index.php"


# with open('test.html','rb+') as h:
#     soup = BeautifulSoup(h.read())


def html_parser(html,conn):
    conn=conn
    content=html.text
    soup=BeautifulSoup(content, 'lxml')
    # with open('test.html', 'rb+') as h:
    #     soup = BeautifulSoup(h.read())

    job_list=soup.select(".job-list > ul > li")
    for job in job_list:
        try:
            job_info = job.select(".info-primary > h3 > a")[0].contents
            job_name=job_info[1].text
            salary=job_info[3].text
        except Exception as e:
            job_name = ""
            salary = ""

        try:
            area_info=job.select(".info-primary > p")[0].contents
            area=area_info[0]
            experience=area_info[2]
            education=area_info[4]
        except Exception as e:
            area = ""
            experience = ""
            education = ""

        try:
            company_info=job.select(".info-company .company-text > p")[0].contents
            industry=company_info[0]
            listed_info=company_info[2]
            employee_num=company_info[4]
        except Exception as e:
            industry = ""
            listed_info = ""
            employee_num = ""



        company_name = job.select(".info-company .company-text > h3 > a")[0].text
        pub_date=job.select(".info-publis > p")[0].text

        cursor = conn.cursor()
        id = uuid.uuid4().hex
        insert_sql = 'insert into boss (id, job_name,salary,area,experience,education,industry,listed_info,employee_num,company_name,pub_date) values ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'
        insert_sql = insert_sql.format(id, job_name, salary, area, experience, education, industry, listed_info, employee_num, company_name, pub_date)

        cursor.execute(insert_sql)

        cursor.close()
        conn.commit()

    page_next = soup.select('a[ka="page-next"]')
    global is_next
    page_next_class=page_next[0].attrs["class"]
    a=len(page_next_class)
    if len(page_next_class) == 1:
        is_next=True
    else:
        is_next=False





    pass
if __name__ == "__main__":

    global is_next
    is_next=True
    page = 1
    conn=sqlite3.connect('boss.db')
    while is_next:
        url=start_url.format("c",str(page))
        rand_proxy=proxy_ip[random.randint(0,3)]

        proxies = {
            "http": rand_proxy
        }
        res = requests.get(url =url, headers = headers, proxies=proxies, timeout = 10)
        html_parser(res,conn)
        page+=1
    conn.close()
    pass
