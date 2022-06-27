from bs4 import BeautifulSoup
import requests
import urllib3
import re

def get_page(url):
    """Download a webpage and return a beautiful soup doc"""
    response = requests.get(url)
    if not response.ok:
        print('Status code:', response.status_code)
        raise Exception('Failed to load page {}'.format(url))
    page_content = response.text
    doc = BeautifulSoup(page_content, 'html.parser')
    return doc




my_url = 'https://finance.yahoo.com/most-active'


http = urllib3.PoolManager()

response = http.request('GET', my_url)
soup = BeautifulSoup(response)
rows = soup.findAll('tr', attrs={'class': re.compile('W(100%)')})