#!/usr/bin/env python2
#hue interpreter v .2
#by Alan Laughter
#released under the GPL v.3

import sys, re
import getch
from find_words import find_words, buildbracemap

def build_instr(script):
    #This initializes the tape, reads the file and sets the pointer to 0
    contents = open(script).readlines()
    
    #this names the instruction set so the Find_Words fucntion can seperate them from garbled nonsense
    instr_set = ["hue", "huE", "hUe", "hUE", "Hue", "HuE", "HUe", "HUE"]
    
    strings = []
    
    #breaks each line into individual words by spaces
    for line in contents:
        #ignores all lines starting with #, note this means comments only work if the whole line starts with #
        #gonna fix this in .v2
        dingus = line.split('#')
        for String in dingus[0].split(" "):
            strings.append(String)
    
    instructions = []
    
    #breaks the words (which may be garbled nonsense) into individual instructions with Find_words and the instruction set
    #this was originally a point of great frustration, but I found a functional function (huehuehue) online (see the module for details)
    for String in strings:
        for instruction in find_words(String, words = instr_set):
            instructions.append(instruction)
    return instructions

def execute(filename):
    instructions = build_instr(filename)
    evaluate(instructions)

def evaluate(instructions):
    bracemap     = buildbracemap(instructions)

    tape = [0]
    pointer = 0

    #names the current executing instruction
    instr_num = 0

    #these variables make looping possible
    ignore = False
    HUe_list = []
    HUE_list = []
    
    while pointer < len(instructions):
        #breaks the main loop when it runs out of instructions
        if instr_num == len(instructions):
            break
        #assigns the current instruction
        instr = instructions[instr_num]
        #loops back to last iteration of HUe if not ignore
        if instr == "HUE": #  ] in BF
            if ignore:
                ignore = False
            else:
                num = instr_num
                del instr_num
                instr_num = HUe_list[len(HUe_list)-1]-1
                del num
        #increments the pointer to the next cell
        elif instr == "hue" and not ignore: # > in BF
            num = pointer
            del pointer
            pointer = num + 1
            del num
            if pointer == len(tape):
                tape.append(0)
        #decrements the pointer to the previous cell (doesn't check if pointer is < 0 need to fix that)
        elif instr == "huE" and not ignore: # < in BF
            num = pointer
            del pointer
            pointer = num - 1
            del num
            if pointer < 0:
                pointer = 0
        #adds 1 to the current cell
        elif instr == "hUe" and not ignore: # + in BF
            tape[pointer] = tape[pointer] + 1
            if tape[pointer] < 255:
                tape[pointer] == 0
        #subtracts 1 from the current cell
        elif instr == "hUE" and not ignore: # - in BF
            tape[pointer] = tape[pointer] - 1
            if tape[pointer] < 0:
                tape[pointer] == 255
        #prints the ascii equivelent of current cell
        elif instr == "Hue" and not ignore: # . in BF
            sys.stdout.write(chr(tape[pointer]))
            #print chr(tape[pointer]),
    
        #inputs character in current cell (doesn't work right)
        elif instr == "HuE" and not ignore: # , in BF
            tape[pointer] = ord(getch.getch())
            #tape[pointer] = ord(raw_input('')[0])
    
        #starts loop by adding current position to a list -HUe_list or ignoreing everything if current cell is 0
        elif instr == "HUe" and not ignore: # [ in BF
            if tape[pointer] > 0:
                ignore = False
                HUe_list.append(instr_num)
            else:
                ignore = True
                HUe_list.remove(HUe_list[len(HUe_list)-1])
    
        #del the old varibles so that the memory doesn't end up super full
        del instr
        num = instr_num
        del instr_num 
        instr_num = num + 1
        del num

def main():
  if len(sys.argv) == 2:
    execute(sys.argv[1])
    print("")
  else: print "Usage:", sys.argv[0], "filename"

if __name__ == "__main__": main()
