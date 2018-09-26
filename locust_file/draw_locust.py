#/usr/bin/env python3
#coding=utf-8
from locust import TaskSet, HttpLocust, task, events
from locust.clients import HttpSession

web = 'https://at.tuandai.com'

from gevent._semaphore import Semaphore
all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()

def on_hatch_complete(**kwargs):
    all_locusts_spawned.release()

events.hatch_complete += on_hatch_complete

class TestTask(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()
        all_locusts_spawned.wait()

class DrawTask(TaskSet):
    session = None

    def on_start(self):
        host = 'https://passport.tuandai.com'
        # 设置sesssion
        self.session = HttpSession(self.host)
        res = self.session.get(url=host + '/2login?ret=http://at.tuandai.com/userActivity/midAutumn/we/index')
        print(res.cookies.values())
        params = {
            'un': '15866660001',
            'pd': '123456a',
            'loadType': 2,
            'encrypt' : 0,
            't' : 65446446
        }
        url = '/2login'
        # 使用 session 来登录
        response = self.session.post(url=host + url, data=params)
        print("login_result:", response.status_code, response.text)

    def on_stop(self):
        pass

    @task(1)
    def FIRST_ROUND(self):
        response = self.session.get(url=web + '/huodong/answerQuestion/drawPrize',
                                    params='drawFlag=ANSWER_QUESTION_FIRST_ROUND')
        print("FIRST_ROUND:", response.status_code, response.text)

    @task(1)
    def SECOND_ROUND(self):
        response = self.session.get(url=web + '/huodong/answerQuestion/drawPrize',
                                    params ='drawFlag=ANSWER_QUESTION_SECOND_ROUND')
        print("SECOND_ROUND:", response.status_code, response.text)

    @task(1)
    def THIRD_ROUND(self):
        response = self.session.get(url=web + '/huodong/answerQuestion/drawPrize',
                                    params='drawFlag=ANSWER_QUESTION_THIRD_ROUND')
        print("THIRD_ROUND:", response.status_code, response.text)


class DrawLocust(HttpLocust):
    task_set = DrawTask
    host = web  # （待测试的ip或者域名）
    # 每个模拟用户将在请求之间等待5至15秒
    min_wait = 3000
    max_wait = 6000


if __name__ == '__main__':
    import subprocess
    subprocess.Popen('locust -f draw_locust.py', shell=True)


