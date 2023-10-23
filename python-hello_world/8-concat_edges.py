#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
str = str.replace("language that combines remarkable power with very clear syntax", "with python")
str = str.split(',')
str = str[2:7]
print(str)
