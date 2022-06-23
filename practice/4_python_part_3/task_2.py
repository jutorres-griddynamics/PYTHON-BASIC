"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     #>>> math_calculate('log', 1024, 2)
     10.0
     #>>> math_calculate('ceil', 10.7)
     11
"""
import math
import pytest

class OperationNotFoundException(Exception):
    pass

@pytest.mark.parametrize("input,expected",  [(['log', 1024, 2],10.0), (['ceil', 10.7], 11)])
def test_eval(input,expected):
    arguments = []
    function = input[0]
    for i in range(1,len(input)):
        arguments.append(input[i])
    try:
        if len(arguments)>1:    calculation = math_calculate(function,arguments[0],arguments[1])
        else: calculation = math_calculate(function,arguments[0])
        assert calculation == expected
    except:
        with pytest.raises(OperationNotFoundException) as excinfo:
            assert excinfo.value.message == "Not found operation... (" + function+")"

def math_calculate(function: str, *args)-> int:
    string_Function = 'math.'
    if len(args)>1:
        string_Function += function + "(" +str(args[0])+","+str(args[1])+")"
    else:
        string_Function += function + "(" + str(args[0])+")"

    try:
        return eval(string_Function)
    except AttributeError:
        raise OperationNotFoundException("Not found operation... (" + function+")")


print(math_calculate('log', 1024, 2))

"""
Write tests for math_calculate function
"""
