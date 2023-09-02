import requests
import time
import random
import re
import config
import JhWxPusher
import getWxInfo
import datetime
checkDict={
'Mzg2Mzk3Mjk5NQ==':['wz',''],
}
def getmsg():
    lvsion = 'v1.0'
    r=''
    try:
        u='http://175.24.153.42:8881/getmsg'
        p={'type':'ybxkhh'}
        r=requests.get(u,params=p)
        rj=r.json()
        version=rj.get('version')
        gdict = rj.get('gdict')
        gmmsg = rj.get('gmmsg')
        print('系统公告:',gmmsg)
        print(f'最新版本{version}当前版本{lvsion}')
        print(f'系统的公众号字典{len(gdict)}个:{gdict}')
        print(f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')
        print('='*50)
    except Exception as e:
        print(r.text)
        print(e)
        print('公告服务器异常')
def printjson(text):
    if printf==0:
        return
    print(text)
def setstatus():
    u='http://175.24.153.42:8882/setstatus'
    p={'key':key,'type':'ybxkhh','val':'1'}
    r=requests.get(u,params=p)
    print(r.text)

def getstatus():
    u = 'http://175.24.153.42:8882/getstatus'
    p = {'key':key,'type': 'ybxkhh'}
    r = requests.get(u, params=p)
    return r.text
class WXYD:
    def __init__(self, cg,bz):
        self.bz=bz
        self.cg=cg
        self.un = cg.get('un')
        self.token = cg.get('token')
        self.headers = {
            'Host': 'u.cocozx.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
        }

    def info(self):
        u = f'http://u.cocozx.cn/api/{self.bz}/info'
        p = {"code": "XG7QUVEEH", "un": self.un, "token": self.token, "pageSize": 20}
        r = requests.post(u, headers=self.headers, json=p)
        print(r.text)
        rj = r.json()
        if rj.get('code') == 0:
            resul = rj.get('result')
            self.moneyCurrent = int(resul.get('moneyCurrent'))
            dayCount = resul.get('dayCount')
            agreementStatus = resul.get('agreementStatus')
            if agreementStatus != 1:
                print('你还没有同意阅读协议，必须先手动阅读一下')
                return False
            hopeNull = resul.get('hopeNull')
            if hopeNull:
                if hopeNull.get('status') == 60:
                    print('今日文章全部读完,请明天再来')
                if hopeNull.get('status') == 70:
                    tss = hopeNull.get('ts')
                    val = hopeNull.get('val')
                    stime = datetime.datetime.strptime(tss, "%Y-%m-%d %H:%M:%S").timestamp()
                    mm = val - int((int(time.time()) - int(stime)) / 60)
                    print('下一批文章' + str(mm) + '分钟后到来')
                if hopeNull.get('status') == 50 or hopeNull.get('status') == 80:
                    print('您的阅读暂时失效，请明天再来')
                print(f'当前账号今日已经阅读{dayCount}篇文章，剩余金币{self.moneyCurrent}')
                return False
            print(f'当前账号今日已经阅读{dayCount}篇文章，剩余金币{self.moneyCurrent}')
            self.statAccess()
            print('-' * 50)
            return True
        else:
            print('可能是账号异常，ck无效，没填ck')
            print('-' * 50)
            return False

    def statAccess(self):
        u = f'http://u.cocozx.cn/api/{self.bz}/statAccess'
        p = {"code": "XG7QUVEEH", "un": self.un, "token": self.token, "pageSize": 20}
        r = requests.post(u, headers=self.headers, json=p)
        print(r.text)

    def agreement(self):
        u = f'http://u.cocozx.cn/api/{self.bz}/agreement'
        p = {"un": self.un, "token": self.token, "pageSize": 20}
        r = requests.post(u, headers=self.headers, json=p)
        print(r.text)
    def psmoneyc(self):
        u = f'http://u.cocozx.cn/api/{self.bz}/psmoneyc'
        p = {"mid":"QS5PQAEZH","un": self.un, "token": self.token, "pageSize": 20}
        r = requests.post(u, headers=self.headers, json=p)
        printjson(r.text)
    def getReadHost(self):
        u = f'http://u.cocozx.cn/api/{self.bz}/getReadHost'
        p = {"un": self.un, "token": self.token, "pageSize": 20}
        r = requests.post(u, headers=self.headers, json=p)
        print(r.text)
        rj = r.json()
        if rj.get('code') == 0:
            host = rj.get('result').get('host')
            hostid = re.findall('mr(.*?)\.', host)[0]
            print(hostid)
            return hostid
        else:
            print('get read host err')
            return False

    def read(self):
        while True:
            print('-'*50)
            u = f'http://u.cocozx.cn/api/{self.bz}/read'
            p = {"un": self.un, "token": self.token, "pageSize": 20}
            r = requests.post(u, headers=self.headers, json=p)
            print(r.text)
            rj = r.json()
            if rj.get('code') == 0:
                status = rj.get('result').get('status')
                if status == 10:
                    url=rj.get('result').get('url')
                    a=getWxInfo.getinfo(url)
                    if self.testCheck(a,url)==False:
                        return False
                    print('获取文章成功，准备阅读')
                    ts = random.randint(7, 10)
                    print(f'本次模拟读{ts}秒')
                    time.sleep(ts)
                    sub = self.submit()
                    if sub == True: return True
                    if sub == False: return False
                elif status==30:
                    print('未知情况')
                    time.sleep(2)
                    continue
                elif status==50 or status==80:
                    print('您的阅读暂时失效，请明天再来')
                    return False
                else:
                    print('本次推荐文章已全部读完')
                    return True
            else:
                print('read err')
                return False
    def testCheck(self,a,url):
        if checkDict.get(a[4]) != None:
            setstatus()
            for i in range(60):
                if i % 30 == 0:
                    JhWxPusher.push(self.cg['name'],url, a[3], 'ybxkhh',self.cg['uids'])
                getstatusinfo = getstatus()
                if getstatusinfo == '0':
                    print('过检测文章已经阅读')
                    return True
                elif getstatusinfo == '1':
                    print(f'正在等待过检测文章阅读结果{i}秒。。。')
                    time.sleep(1)
                else:
                    print('服务器异常')
                    return False
            print('过检测超时中止脚本防止黑号')
            return False
        else:return True
    def submit(self):
        u = f'http://u.cocozx.cn/api/{self.bz}/submit'
        p = {"un": self.un, "token": self.token, "pageSize": 20}
        r = requests.post(u, headers=self.headers, json=p)
        print(r.text)
        rj = r.json()
        if rj.get('code') == 0:
            result = rj.get('result')
            print(f'获得{result.get("val")}元宝')
            progress = result.get('progress')
            if progress > 0:
                print(f'本轮剩余{progress - 1}篇文章，继续阅读阅读')
            else:
                print('阅读已完成')
                print('-' * 50)
                return True
        else:
            print('异常')
            return False

    def wdmoney(self):
        if self.moneyCurrent < 10000:
            print('没有达到提现标准')
            return False
        elif 3000 <= self.moneyCurrent < 10000:
            txm = 3000
        elif 10000 <= self.moneyCurrent < 50000:
            txm = 10000
        elif 50000 <= self.moneyCurrent < 100000:
            txm = 50000
        else:
            txm = 100000
        u=f'http://u.cocozx.cn/api/{self.bz}/wdmoney'
        if self.bz == 'user':
            u=f'http://u.cocozx.cn/api/{self.bz}/wd'
        p = {"val":txm,"un": self.un, "token": self.token, "pageSize": 20}
        r = requests.post(u, headers=self.headers, json=p)
        print('提现结果',r.text)
    def run(self):
        if self.info():
            if self.bz=='user':
                self.psmoneyc()
            time.sleep(1)
            self.read()
        time.sleep(2)
        self.info()
        time.sleep(2)
        self.wdmoney()

if __name__ == '__main__':
    printf = config.printf
    key = config.key
    getmsg()
    bzl = ['ox']
    for bz in bzl:
        print('='*50)
        print(bz)
        for cg in config.xkybconfig:
            api = WXYD(cg,bz)
            api.run()
            time.sleep(5)