# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# open the file1.txt in read mode. causes error if no such file exists.
with open("file1.txt", "r") as fileptr:
    # stores all the data of the file into the variable content
    content1 = fileptr.readline(14)
    content2 = fileptr.readline(47)
# prints the content of the file
print(content1)
print(content2)
