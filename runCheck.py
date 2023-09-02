import config
import requests
import time
import hashlib
def sha_256(text):
    hash = hashlib.sha256()
    hash.update(text.encode())
    t = hash.hexdigest()
    return t
def push(name,text, uids):
    summary = name + ':' + text
    appToken = config.appToken
    topicIds=config.topicIds
    content = f'{name}{text}测试成功'
    datapust = {
        "appToken": appToken,
        "content": content,
        "summary": summary,
        "contentType": 2,
        "topicIds": [topicIds],
        "uids": [uids],
        "url": "https://t.me/bwersgt",
    }
    urlpust = 'http://wxpusher.zjiecode.com/api/send/message'
    try:
        p = requests.post(url=urlpust, json=datapust).text
        print(p)
        return True
    except:
        print('推送失败！')
        return False
def getstatus():
    u = 'http://175.24.153.42:8882/getstatus'
    p = {'key':config.key,'type': 'czgm'}
    r = requests.get(u, params=p)
    print('key:',r.text)
print('-'*50)
print('检测推送参数')
if config.key=='xxxx' or type(config.key)!=str:
    print(f'key参数未填写或填写有误-->{config.key}')
else:
    print('key格式填写正确')
if config.appToken=='xxxx' or type(config.appToken)!=str:
    print(f'appToken参数未填写或填写有误-->{config.appToken}')
else:
    print('appToken格式填写正确')
if config.topicIds=='xxxx' or type(config.topicIds)!=int:
    print(f'topicIds参数未填写或填写有误-->{config.topicIds}')
else:
    print('topicIds格式填写正确')
print('-'*50)
name=config.czgmconfig[0].get('name')
uids=config.czgmconfig[0].get('uids')
ck=config.czgmconfig[0].get('ck')
def user_info():
    headers = {
        'Host': '2478987.jilixczlz.ix47965in5.cloud',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh',
        'Cookie': f'gfsessionid={ck}',
    }
    ts = int(time.time())
    text = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={ts}'
    sign = sha_256(text)
    u = f'http://2478987.jilixczlz.ix47965in5.cloud/user/info?time={ts}&sign={sign}'
    r = requests.get(u,headers=headers)
    rj = r.json()
    if rj.get('code') == 0:
        print(f'用户UID:{rj.get("data").get("uid")}')
    else:
        print(f'获取用户信息失败，ck没用填对')
        print(rj)
print('测试参数有效性')
print('测试key(显示数字代表有效)')
getstatus()
print('测试推送')
push(name,'充值购买测试',uids)
print('请已实际推送结果为准')
print('-'*50)
print('只检测充值购买参数,如果这个没问相信你其他的也不会填错,脚本选择第一个用户测试')
user_info()
time.sleep(5)