import requests

response = requests.get('http://www.baidu.com/')

print(type(response))
# 获取响应状态码
print(type(response.status_code),response.status_code)
# 获取响应头信息
print(type(response.headers),response.headers)
# 获取响应头中的cookies
print(type(response.cookies),response.cookies)
# 获取访问的url
print(type(response.url),response.url)
# 获取访问的历史记录
print(type(response.history),response.history)