"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

import argparse
import sys
import re
from faker import Faker
import pytest
from unittest.mock import Mock, patch
def test_deserved_value_type(monkeypatch):
    dictionary_Result = print_name_address(input_mock.method().split())
    for elements in dictionary_Result:
        assert type(elements) is dict

def test_deserved_keys_values(monkeypatch):

    dictionary_Result =  print_name_address(input_mock.method().split())
    for elements in dictionary_Result:
        for i in elements.values():
            assert type(i) is str

def print_name_address(args: argparse.Namespace) -> None:
    list_of_Dictionary = []
    #Delete first argument (script calling)
    args.pop(0)
    #Get number of items u want to generate
    number = int(args.pop(0))
    #Create dictionarys
    for i in range(number):
        temporary_Dictionary = {}
        for argument in args:
            # Looking for the first alphanumeric index
            m = re.search(r'[a-z]', argument, re.I)
            if m is not None:

                #Delete '--' if its found in argument
                argument = argument[m.start():]

                #Separate dictionary key and value
                dict_Key, dict_Value = argument.split('=')
                #print(dict_Key,dict_Value)

                instruction = 'fake.' + str(dict_Value) + '()'
                temporary_Dictionary[dict_Key] = eval(instruction)

        list_of_Dictionary.append(temporary_Dictionary)

    return list_of_Dictionary


input_mock = Mock()
outputmock = Mock()
input_mock.method.return_value = 'task_4.py 2 --fake-address=address --some_name=name'
outputmock.method.return_value = {"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}

fake = Faker()
########################## COMMENT NEXT LINE IF YOU ARE TESTING
#print(print_name_address(sys.argv))

"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""
