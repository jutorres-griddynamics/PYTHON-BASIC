"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""
import numpy as np

def remove_duplicated_words(line: str) -> str:
    listDuplicates =[]
    line = line.split()
    for i in line:
        if i not in listDuplicates:
            print(i, end=' ')
            listDuplicates.append(i)
    print()

remove_duplicated_words('cat cat dog 1 dog 2')
remove_duplicated_words('cat cat cat')
remove_duplicated_words('1 2 3')