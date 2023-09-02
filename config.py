'''
这个文件是总配置文件，请仔细读配置说明
'''
'''
czgmconfig是充值购买的参数配置列表
活动入口,微信打开：http://2478987.epghgkvalp.wjbk.25obcxyume.cloud/?p=2478987
打开活动入口，抓包的任意接口cookies中的gfsessionid参数,填入ck。
单账户填写样式。(这里只是样式，不要填这里)
czgmconfig = [
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
]
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
czgmconfig = [
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
]
参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口cookies中的gfsessionid参数
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送主题后，会在主题的关注列表中显示
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 用户管理->用户列表 能看到uids，用户uids可以单个推送消息给用户
'''
czgmconfig = [
    {'name': '账号1', 'ck': 'o-0fIv5OxxxxL9jpvo', "uids": 'UID_11xxxxxxQ'},
    {'name': '账号2', 'ck': 'xxxx', "uids": 'xxx'},
]
#########################################################################
'''
mtzconfig是美添赚的参数配置列表
活动入口,微信打开：http://tg.1693182678.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=115772
打开活动入口，抓包的任意接口headers中的Authorization参数，填入ck。
单账户填写样式(这里只是样式，不要填这里)
mtzconfig = [
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
]
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
mtzconfig = [
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
]
参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口headers中的Authorization参数
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送主题后，会在主题的关注列表中显示
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 用户管理->用户列表 能看到uids，用户uids可以单个推送消息给用户
'''
mtzconfig = [
    {'name': '账号1', 'ck': 'share:login:18axxxxxx9c68adc1c1', "uids": 'UID_11ZHxxxxxxxxxxQ'},
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
]
#########################################################################
'''
xyyconfig是小阅阅的参数配置列表
活动入口,微信打开：https://wib.quannengjiaoyu.top:10265/yunonline/v1/auth/693f35a37d8da489478562a1feab678f?codeurl=wib.quannengjiaoyu.top:10265&codeuserid=2&time=1693118713
打开活动入口，抓包的任意接口cookies中的ysm_uid参数,填入ck。
单账户填写样式(这里只是样式，不要填这里)
xyyconfig = [
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
]
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
xyyconfig = [
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
]
参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口headers中的Authorization参数
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送主题后，会在主题的关注列表中显示
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 用户管理->用户列表 能看到uids，用过uids可以单个推送消息给用户
'''
xyyconfig = [
    {'name': '账号1', 'ck': 'oZdBp08xxxxxx8KpwY', "uids": 'UID_11ZH0xxxxxxxxxxxQ'},
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
    {'name': 'xxx', 'ck': 'xxxx', "uids": 'xxx'},
]
#########################################################################
'''
公共推送参数
参数解释
key:回调服务器的key，通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
多用户可以只使用一个key,key永不过期。为了防止恶意调用key接口，限制每个ip每天只能获取一个key。
appToken:wxpusher的参数，在你创建应用的过程中，你应该已经看到appToken，如果没有保存，可以通过下面的方式重制它。
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 应用管理->appToken->重置appToken
topicIds:wxpusher的参数
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 主题管理能够看到
'''
key = '642ae5xxxxxxxd2334c'
appToken = 'AT_r1vxxxxxxxxYg'
topicIds = 4781
#########################################################################
'''
其他参数
参数解释
printf:日志打印参数，0是不打印调试日志，1是打印调试日志
'''
printf = 0
