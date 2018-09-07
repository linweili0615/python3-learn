#/usr/bin/env python3
#coding=utf-8
from locust import TaskSet, HttpLocust, task
#HttpLocust（用来模拟发请求的类）
#TaskSet（顾名思义，任务集）
#task（任务类）

#Locust能在使用较少压力机的前提下支持极高并发数的测试

#页面
#python locust_eg.py
#命令行
#--no-web是用来选择无浏览器模式，-c后面接的是模拟用户数，-r后面接的每秒模拟用户并发数，-n后面接的是模拟请求数
#locust -f .\locust_test_1.py --host='http://api.winyyg.com' --no-web -c 1000 -r 10 -n 1000


#性能测试任务类
class UserBehavior(TaskSet):    #传入TaskSet参数，说明这是一个包含了任务集的类
    #开始
    def on_start(self):     #on_start函数可有可无，他会先于所有task函数运行
        pass

    #任务
    @task(1)                #被@task装饰器装饰的方法都是任务方法,传入的参数代表了权重
    def getUserInfo(self):
        u'''
        request_url ：请求路径
        request_params : 请求头
        request_json  :  请求json参数
        '''
        request_url = '/user/F50024E6-CF0C-40EA-9263-6772417758C5/memberUpgradeV3'
        request_params = {

        }
        request_json = {

        }
        response = self.client.post(
            url = request_url,
            params = request_params,
            json = request_json
        )
        if response.status_code != 200:
            print('%s: 返回异常' % response.status_code)
        elif response.status_code == 200:
            print('%s: 返回正常' % response.status_code)
        # 这里可以编写自己需要校验的返回内容
        # content = json.loads(response.content)["content"]
        # if content["tagKey"] == 25:
        #     print u"校验成功"
        #     print json.dumps(content, encoding="UTF-8", ensure_ascii=False)

#性能测试配置
class UserInfoLocust(HttpLocust):
    u"""
    min_wait ：用户执行任务之间等待时间的下界，单位：毫秒。
    max_wait ：用户执行任务之间等待时间的上界，单位：毫秒。
    """
    # weight = 3
    #http://10.100.14.5:9002/user/F50024E6-CF0C-40EA-9263-6772417758C5/memberUpgradeV3
    task_set = UserBehavior
    host = "http://10.100.14.5:9002"  #（待测试的ip或者域名）
    #每个模拟用户将在请求之间等待5至15秒
    min_wait = 3000
    max_wait = 6000

if __name__ == '__main__':
    import subprocess
    subprocess.Popen('locust -f locust_eg.py', shell=True)

    # 模拟的用户总数
    #每秒钟并发的用户数量