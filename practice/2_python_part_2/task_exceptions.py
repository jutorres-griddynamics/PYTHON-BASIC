"""
Write a function which divides x by y.
If y == 0 it should print "Division by 0" and return None
elif y == 1 it should raise custom Exception with "Deletion on 1 get the same result" text
else it should return the result of division
In all cases it should print "Division finished"
    >>> division(1, 0)
    Division by 0
    Division finished
    >>> division(1, 1)
    Division finished
    DivisionByOneException("Deletion on 1 get the same result")
    >>> division(2, 2)
    1
    Division finished
"""
import typing

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class zero_Division(Error):
    """Raised when zero division"""
    pass
class same_Result(Error):
    """Raised when trying to divide by 1"""
    pass

def division(x: int, y: int) -> typing.Union[None, int]:
    try:
        if y == 0:
            raise zero_Division
        elif y == 1:
            raise same_Result
        else:
            print(x/y)
            return x/y
    except zero_Division:
        print("Division by 0")
    except same_Result:
        print("Deletion on 1 get the same result")
division(1, 0)
division(1, 1)
division(2, 2)