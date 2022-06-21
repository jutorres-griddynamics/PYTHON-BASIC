"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

import pytest

import sys
import unittest
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/julitorresma/PycharmProjects/PYTHON-BASIC/practice/2_python_part_2')
from task_classes import Homework, Teacher, Student

import pytest

@pytest.fixture
def student():
    return Student('Vladislav', 'Popov')
@pytest.fixture
def teacher():
    return Teacher('Dmitry', 'Orlyakov')
@pytest.fixture
def homework(teacher):
    return teacher.create_homework('Learn functions', 1)

def verify_name(first_expected, last_expected, first_name, last_name):
    assert first_expected == first_name
    assert last_expected == last_name
def verify_homework_date_logic(created, deadline):
    assert created <= deadline

def test_name_student(student):
    verify_name('Popov','Vladislav',student.first_name,student.last_name)
def test_name_teacher(teacher):
    verify_name('Orlyakov','Dmitry',teacher.first_name,teacher.last_name)
def test_create_homework(homework):
    #print("Created:",homework.created,type(homework.created))
    #print("Deadline:", homework.deadline, type(homework.deadline))
    verify_homework_date_logic(homework.created,homework.deadline)

