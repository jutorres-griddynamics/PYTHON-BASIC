"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""
import codecs

def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words

words = generate_words()
string = ""
for i in range(len(words)):
    string += str(words[i])
    if i != len(words) - 1:
        string += "/"
file = codecs.open("file1", "w", "utf-8")
file.write(string)
file.close()

string = ""
for i in range(len(words)-1,-1,-1):
    string += str(words[i])
    if i != 0:
        string += "-"
file = codecs.open("file2", "w", "cp1252")
file.write(string)
file.close()