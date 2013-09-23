#!/usr/bin/env python2
#brainfuck to hue converter

import sys

filename = sys.argv[1]

BF_File_To_Convert = open(filename, "r").read()

import re
new_filename = re.sub('\.bf$', '', filename)

Hue_File = open(new_filename+".hue", 'a')
x = 0
for char in BF_File_To_Convert:
    if char == "]":
        x = x + 1
        Hue_File.write(str(x) + " HUE ")
    elif char == ">":
        x = x + 1
        Hue_File.write(str(x) + " hue ")
    elif char == "<":
        x = x + 1
        Hue_File.write(str(x) + " huE ")
    elif char == "+":
        x = x + 1
        Hue_File.write(str(x) + " hUe ")
    elif char == "-":
        x = x + 1
        Hue_File.write(str(x) + " hUE ")
    elif char == ".":
        x = x + 1
        Hue_File.write(str(x) + " Hue ")
    elif char == ",":
        x = x + 1
        Hue_File.write(str(x) + " HuE ")
    elif char == "[":
        x = x + 1
        Hue_File.write(str(x) + " HUe ")
    else:
        pass

