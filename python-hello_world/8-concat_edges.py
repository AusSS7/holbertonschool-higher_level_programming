#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
str1,str2,str3 = str.split(',')
str = str3.replace("language that combines remarkable power with very clear syntax", "with python")
print(str)
