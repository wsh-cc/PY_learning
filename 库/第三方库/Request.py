import requests

r=requests.get('https://www.baidu.com/')
print(r.text)

R = requests.request('get','https://www.baidu.com/')
print(R.text)
# R = requests.request('GET','https://www.baidu.com/')
# print(R.text)
#get大小写一样，request方法的第一个参数是请求方法，可以是'get'、'post'等，大小写不敏感。第二个参数是URL，返回一个Response对象。可以通过Response对象的text属性获取响应内容。

