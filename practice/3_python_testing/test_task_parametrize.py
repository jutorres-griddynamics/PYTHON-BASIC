"""
Write a parametrized test for two functions.
The functions are used to find a number by ordinal in the Fibonacci sequence.
One of them has a bug.

Fibonacci sequence: https://en.wikipedia.org/wiki/Fibonacci_number

Task:
 1. Write a test with @pytest.mark.parametrize decorator.
 2. Find the buggy function and fix it.
"""
import pytest
@pytest.mark.parametrize("index,expected",  [(1, 1), (2, 1),(3, 2), (4,3), (5, 5),(6, 8),(7, 13)])
def test_eval(index,expected):
    assert fibonacci_1(index) == expected
    assert fibonacci_2(index) == expected

def fibonacci_1(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b

def fibonacci_2(n):
    #3
    fibo = [0, 1]#1,1
    for i in range(2, n+1):
        print("Hola")
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[n]

number = 5