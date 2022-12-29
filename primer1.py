# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# open the file1.txt in append mode. Create a new file if no such file exists.
with open("file1.txt", "w") as fileptr:

    # appending the content to the file
    fileptr.write(
        "Python is the modern day language. It makes things so simple.\n"
        "It is the fastest-growing programing language"
    )
