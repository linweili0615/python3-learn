#/usr/bin/env python3
#coding=utf-8
from locust import HttpLocust, TaskSet, task
from gevent._semaphore import Semaphore
all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()


host = 'http://crm.tuandai.com/'
token = 'b303e06d161f527f91e7d2786c0b273d'
validate_str = '200'

class CrmTaskSet(TaskSet):

    @task(1)
    def index(self):
        with self.client.get(
            name = '资金',
            headers = {'token': token},
            url = host + 'kefu/customerallinfo/investprojectlist?userId=F0A3450D-7E4C-415E-BD91-FE7A9606096F&callNumber=&custID=&'
                         'beginDate=2017-09-25&endDate=2018-09-25&status=-1&inviteType=888&_search=false&nd=1537871687304&limit=15&page=1&sidx=&order=asc&_=1537871687180',
            catch_response = True   # catch_response = True ：布尔类型，如果设置为 True, 允许该请求被标记为成功失败。
        ) as response:
            print('资金:response:{}'.format(response.text))
            if response.status_code == 200:
                if validate_str in response.text:
                    response.success()
                else:
                    print('资金:Response Failed :{}'.format(response.text))
                    response.failure('Response Failed!')
            else:
                print('资金:Request Failed :{}'.format(response.text))
                response.failure('Request Failed!')

    @task(1)
    def index1(self):
        with self.client.get(
            name='资金详情',
            headers={'token': token},
            url=host + 'kefu/customerallinfo/funddetailinfolist?userId=F0A3450D-7E4C-415E-BD91-FE7A9606096F&callNumber=&custID=&'
                       'beginDate=2018-09-01&endDate=2018-09-25&status=-1&_search=false&nd=1537871657071&limit=15&page=1&sidx=&order=asc&_=1537871656903',
            catch_response=True
        ) as response:

            if response.status_code == 200:
                if validate_str in response.text:
                    response.success()
                else:
                    print('资金详情:Response Failed :{}'.format(response.text))
                    response.failure('Response Failed!')
            else:
                print('资金详情:Request Failed!:{}'.format(response.text))
                response.failure('Request Failed!')


class LocustWeb(HttpLocust):
    task_set = CrmTaskSet
    host = host
    # min_wait和max_wait用于设置执行task过程中的等待时间，相当于LR中Pacing的设置，这里都设置为0；
    min_wait = 0
    max_wait = 0

if __name__ == '__main__':
    import subprocess

    # 设置相同的10用户并发，Hatch Rate是每秒启动多少用户的意思。这里设置为10，就是同时启动10个
    subprocess.Popen('locust -f crm.py --no-web --csv=crm --logfile=crm.log -c 10 -r 10 -t 10s',shell=True)

#no-web执行
# –no-web 表示不使用Web界面运行测试。
# -c 设置虚拟用户数。
# -r 设置每秒启动虚拟用户数。
# -t 设置设置运行时间。
    # 10s 默认为秒
    # 5m 表示五分钟
    # 1h
    # 1h30s
# --csv=crm
# 会自动保存2文件到脚本当前目录
# locust -f crm.py --no-web --csv=crm --logfile=crm.log -c 10 -r 10 -t 10s
