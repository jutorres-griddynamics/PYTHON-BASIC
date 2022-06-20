"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os, os.path

with open('files/result.txt', 'w') as f:
    pass
f.close()

list = os.listdir("/Users/julitorresma/PycharmProjects/PYTHON-BASIC/practice/2_python_part_2/files") # dir is your directory path
directoryLen = len(list)

print(directoryLen)
listNumbers = []
for i in range(1,directoryLen):
    with open("files/file_"+str(i)+".txt") as opened_file:
        for line in opened_file:
            listNumbers.append(int(line))  # Adding all numbers to python list as integers

with open('files/result.txt', 'w') as f:
    string = ""
    for i in range(len(listNumbers)):
        string += str(listNumbers[i])
        if i != len(listNumbers)-1:
            string+= ", "
    f.write(string)
