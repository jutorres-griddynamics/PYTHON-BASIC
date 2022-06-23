"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    #>>>is_http_domain('http://wikipedia.org')
    True
    #>>>is_http_domain('https://ru.wikipedia.org/')
    True
    #>>>is_http_domain('griddynamics.com')
    False
"""
import re
import pytest

class NotFoundAdress(Exception):
    pass

@pytest.mark.parametrize("input,expected",  [('http://wikipedia.org',True), ('https://ru.wikipedia.org/', True),('griddynamics.com',False)])
def test_eval(input,expected):
    result = is_http_domain(input)
    assert result == expected

def is_http_domain(domain: str) -> bool:

    def Find(string):
        # findall() has been used
        # with valid conditions for urls in string
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex, string)
        return [x[0] for x in url]

    url = Find(domain)
    if len(url)>=1: return True
    else: return False


print(is_http_domain('https://wikipedia.org'))

"""
write tests for is_http_domain function
"""