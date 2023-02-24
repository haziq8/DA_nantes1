import requests

headers = {
    'User-Agent': 'Mobile'
}

url = 'http://www.wikipedia.org'
webpage = requests.get(url)

print(webpage.text)

print("Status code:")
print("\t *", webpage.status_code)

h= requests.head(url)
print("Header:")
print("**********")

for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

headers = {'User-Agent': 'Iphone 14'}

url2 = 'http://httpbin.org/headers'
request_header = requests.get(url2, headers=headers)
print(request_header.text)

# Modify the Header user-agent to display "iPhone 14"
headers = {'User-Agent': 'iPhone 14'}
# Test against test site that output the requester user-agent
#url2 = 'http://httpbin.org/headers'
url2 = 'http://172.18.58.80/headers.php'
request_header = requests.get(url2, headers=headers)
print(request_header.text)
