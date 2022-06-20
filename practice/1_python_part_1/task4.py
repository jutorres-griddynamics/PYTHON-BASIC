"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:

    newList = []
    for i in range(len(ints)):#iterate thru array range
        if i !=0:
             newList.append(pow(ints[i],2) - (pow(ints[i-1],2)-ints[i-1]))
        else: newList.append(pow(ints[i],2))
    print(newList)
calculate_power_with_difference([1, 2, 3])