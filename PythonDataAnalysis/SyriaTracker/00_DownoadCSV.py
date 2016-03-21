print('test')

import requests
sess = requests.session()
url = "https://syriatracker.crowdmap.com/reports/download"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36', 'Host': 'syriatracker.crowdmap.com', 'Accept-Language': 'ko-KR,en-US;q=0.7,en;q=0.3', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Referer': 'https://syriatracker.crowdmap.com/reports/download'}
response = sess.get(url, headers = headers)
response = sess.get(url, headers = headers)

response.text
plain_text = response.text

from bs4 import BeautifulSoup

# windows is not installed lxml library as pip... T_T
# so use html.parser
soup = BeautifulSoup(plain_text, 'html.parser')

form_auth_token_value
for link in soup.select('form > input'):
    attrs = link.attrs
    if attrs['name'] == 'form_auth_token':
        form_auth_token_value = attrs['value']
        break

form_data_str = 'form_auth_token=' + form_auth_token_value
for link in soup.find_all('input'):
    link
    attrs = link.attrs
    for key in attrs.keys():
        if key == 'name':
            if attrs['name'] == 'category[]':
                form_data_str += '&category%5B%5D=' + attrs['value']
            if attrs['name'] == 'verified[]':
                form_data_str += '&verified%5B%5D=' + attrs['value']
            if attrs['name'] == 'from_date':
                form_data_str += '&from_date=' + attrs['value']
            if attrs['name'] == 'to_date':
                form_data_str += '&to_date=' + attrs['value']
            if attrs['name'] == 'formato':
                form_data_str += '&formato=' + attrs['value']

form_data_str += '&x=67&y=13'

headers = { 'Content-Type' : 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36' } 
#data = 'form_auth_token=494d531a919f0b2b02218d9fc43c36936f2e2e89939a6fcfad870465aa418dfe&category%5B%5D=1004&verified%5B%5D=1&verified%5B%5D=0&from_date=04%2F01%2F2011&to_date=03%2F12%2F2016&formato=0&x=67&y=13'
form_data_str
csv_text = sess.post('https://syriatracker.crowdmap.com/reports/download', headers = headers, data = form_data_str)

# save CSV file to Orign
import StaticPath as SP

file = open(SP.origin_path_str + SP.origin_file_str, 'w')
# column �迭�� ���� �����Ƿ�,
# ù�� column �������� '��ǥ(,)'�� �߰����ش�.