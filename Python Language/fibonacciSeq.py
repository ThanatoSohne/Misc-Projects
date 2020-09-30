# -*- coding: utf-8 -*-
"""
Fibonacci Finder!

General idea:
User inputs a number and the function created 
checks whether the number belongs to the 
Fibonacci sequence or not.

Libraries used: math, termcolor
"""

import math
from termcolor import colored as cl

def fibNum(n):
    goldenRatio = 1.61803
    #https://en.wikipedia.org/wiki/Fibonacci_number
    #Used the formula concerning golden ratio to create a 
    #comprehension list to hold the Fibonacci sequence and see if 
    #n is part of that sequence
    seq = [round(((goldenRatio ** i) - (1-goldenRatio)**i)/math.sqrt(5)) for i in range(1001)]
    if int(n) in seq:
        print(cl("The number you gave is a part of the Fibonacci sequence!", "blue"))
    else:
        print(cl("Sorry! That number is not a part of the Fibonacci sequence!", "red"))
    del seq
    
def main():
    
    n = input("Wilkommen! Hello! I am a Fibonacci guesser! I can tell " +
              "if a number you input is part of the famed Fibonacci sequence. " +
              "So, please input a number now: ")
    #n = input()
    fibNum(n)

main()