#/usr/bin/env python3
#coding=utf-8
from locust import HttpLocust, TaskSet, task
from gevent._semaphore import Semaphore
all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()

# catch_response = True ：布尔类型，如果设置为 True, 允许该请求被标记为失败。
#min_wait和max_wait用于设置执行task过程中的等待时间，相当于LR中Pacing的设置，这里都设置为0；
#设置相同的10用户并发，Hatch Rate是每秒启动多少用户的意思。这里设置为10，就是同时启动10个



host = 'http://crm.tuandai.com/'
token = 'b303e06d161f527f91e7d2786c0b273d'

class CrmTaskSet(TaskSet):

    @task(1)
    def index(self):
        with self.client.get(
            namd = '资金',
            headers = {'token': token},
            url = host + 'kefu/customerallinfo/investprojectlist?userId=F0A3450D-7E4C-415E-BD91-FE7A9606096F&callNumber=&custID=&'
                         'beginDate=2017-09-25&endDate=2018-09-25&status=-1&inviteType=888&_search=false&nd=1537871687304&limit=15&page=1&sidx=&order=asc&_=1537871687180',
            catch_response = True
        ) as response:
            if response.status_code == 200:
                if 'code' in response.text:
                    response.failure('Failed!')
                else:
                    response.failure('Failed!')
            else:
                response.failure('Failed!')

    @task(1)
    def index1(self):
        with self.client.get(
            namd='资金详情',
            headers={'token': token},
            url=host + 'kefu/customerallinfo/funddetailinfolist?userId=F0A3450D-7E4C-415E-BD91-FE7A9606096F&callNumber=&custID=&'
                       'beginDate=2018-09-01&endDate=2018-09-25&status=-1&_search=false&nd=1537871657071&limit=15&page=1&sidx=&order=asc&_=1537871656903',
            catch_response=True
        ) as response:
            if response.status_code == 200:
                if 'code' in response.text:
                    response.success('Failed!')
                else:
                    response.failure('Failed!')
            else:
                response.failure('Failed!')


class LocustWeb(HttpLocust):
    task_set = CrmTaskSet
    host = host
    min_wait = 0
    max_wait = 0

if __name__ == '__main__':
    import subprocess
    subprocess.Popen('locust -f crm.py',shell=True)
