"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""
import pytest
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/julitorresma/PycharmProjects/PYTHON-BASIC/practice/2_python_part_2')
from task_exceptions import division

def test_division_ok(capfd):
    division(2, 2)
    out, err = capfd.readouterr()
    assert out == str(2/2)+"\n"

def test_division_by_zero(capfd):
    division(1, 0)
    out, err = capfd.readouterr()
    assert out == "Division by 0\n"

def test_division_by_one(capfd):
    division(1, 1)
    out, err = capfd.readouterr()
    assert out == "Deletion on 1 get the same result\n"
