#/usr/bin/env python3
#coding=utf-8
from locust import HttpLocust, TaskSet, task
import datetime

def login(l):
    print('login: in')
    response = l.client.get(
        '/2login')
    print("Response status code:", response.status_code)
    print("Response content:", response.text)
    print('login: out')

def login_post(l):
    print('login_post: in')
    response = l.client.post(
        url = '/2login',
        data = {
            'un': '15866660001',
            'pd': '123456a',
            'loadType':2,
            'encrypt':0,
            't': datetime.datetime
        }
    )
    print("Response status code:", response.status_code)
    print("Response content:", response.text)
    print('login_post: out')

def end(l):
    print('end: out')

class LoginTaskSet(TaskSet):
    def on_start(self):
        login(self)
        login_post(self)

    def on_stop(self):
        end(self)

    @task(1)
    def index(l):
        print('index')

class LocustWeb(HttpLocust):
    task_set = LoginTaskSet
    host = 'https://passport.tuandai.com'
    min_wait = 1000
    max_wait = 2000

if __name__ == '__main__':
    import subprocess
    subprocess.Popen('locust -f locust_example.py',shell=True)
