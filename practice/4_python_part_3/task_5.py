"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     #>>> make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple
from html5lib import html5parser
import urllib3
from unittest.mock import Mock, patch

query="https://www.google.com/"
def test_deserved_value(monkeypatch):
    status, response = make_request(input_mock.method())
    assert status == 200
def test_deserved_value_type(monkeypatch):
    status, response = make_request(input_mock.method())
    assert "<class 'urllib3.response.HTTPResponse'>" == str(type(response))


def make_request(url: str) -> Tuple[int, str]:
    http = urllib3.PoolManager()
    url = 'http://webcode.me'
    resp = http.request('GET', url)
    #print(resp.status)
    print(type(resp))
    return resp.status,resp


input_mock = Mock()
input_mock.method.return_value = 'https://www.google.com'

make_request(query)



"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""
