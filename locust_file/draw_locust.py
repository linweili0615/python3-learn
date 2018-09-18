#/usr/bin/env python3
#coding=utf-8
from locust import TaskSet, HttpLocust, task
from locust.clients import HttpSession

telno = '15866660001'

class DrawTask(TaskSet):
    session = None
    host = 'https://passport.tuandai.com'

    def on_start(self):
        # 设置sesssion
        self.session = HttpSession(self.host)
        # 使用 session 来登录
        # params = 'un={}&pd=123456a&loadType=2&encrypt=0&t=65446446&geetestChallenge=&geetestValidate=&geetestSeccode='.format(telno)
        params = {
            'un': '15866660001',
            'pd': '123456a',
            'loadType': 2,
            'encrypt' : 0,
            't' : 65446446
        }
        url = '/2login'
        response = self.session.post(url=self.host + url, data=params)
        print("login_result:", response.status_code, response.text)

    def on_stop(self):
        pass

    @task(1)
    def draw_redpacket(self):
        response = self.session.post(url='https://at.tuandai.com/userActivity/midAutumn/toFuDaiDraw', data='type=1')
        print("Draw_result:", response.status_code, response.text)

class DrawLocust(HttpLocust):
    task_set = DrawTask
    host = "https://at.tuandai.com"  # （待测试的ip或者域名）
    # 每个模拟用户将在请求之间等待5至15秒
    min_wait = 3000
    max_wait = 6000


if __name__ == '__main__':
    import subprocess
    subprocess.Popen('locust -f draw_locust.py', shell=True)


