"""#3 A text file contains a header line, few comments
lines followed by actual lines of data. Write a python
program to create a function skip_header() that skips
the header and all the comment lines and prints only
actual lines of data.
"""

def skip_header(txt):
    print("".join([i for i in txt[1:] if '#' not in i]).strip())

file=open("p7_3.txt","r")
text=file.readlines()
skip_header(text)
file.close()