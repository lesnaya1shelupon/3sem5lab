# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# open the newfile.txt in read mode. causes error if no such file exists.
with open("newfile1.txt", "x") as fileptr:
    print(fileptr)
    if fileptr:
        print("File created successfully")
