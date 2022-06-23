"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
from unittest.mock import patch
from unittest.mock import Mock, patch
import sys
from io import StringIO
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/julitorresma/PycharmProjects/PYTHON-BASIC/practice/2_python_part_2')
from task_input_output import read_numbers
import pytest
import mock

'''
https://stackoverflow.com/questions/66222805/mock-patch-multiple-user-inputs-in-sequence
'''

def test_read_numbers_without_text_input(monkeypatch):
    numbers_n = 4
    inputList = [1, 2, 3, 4]
    list_atributes = []
    '''
    Improved StackOverflow tutorial using an iterator to create
    several mock objects just substituting at the same variable 
    and appending directly to a local list.
    '''
    for i in range(numbers_n):
        input_mock_y = Mock()
        input_mock_y.return_value =     str(inputList[i])
        list_atributes.append(input_mock_y.return_value)
    input_mock.side_effect = list_atributes
    with patch('builtins.input', input_mock) as mock_method:
        result = read_numbers(numbers_n)
    assert result == ('Avg:', 2.5)
    # go about using input() like you normally would:



def test_read_numbers_with_text_input():
    numbers_n = 4
    inputList = ["Hola", 2, 3, 4]
    list_atributes = []
    for i in range(numbers_n):
        input_mock_y = Mock()
        input_mock_y.return_value = str(inputList[i])
        list_atributes.append(input_mock_y.return_value)
    input_mock.side_effect = list_atributes
    with patch('builtins.input', input_mock) as mock_method:
        result = read_numbers(numbers_n)
    assert result == ('Avg:', 3.0)
    # go about using input() like you normally would:

input_mock = Mock()
input_mock.side_effect = []

