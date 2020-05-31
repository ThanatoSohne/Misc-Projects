# -*- coding: utf-8 -*-
"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print the word 'Fizz' instead of the number.
For multiples of five print the word 'Buzz' instead of the number.
For numbers that are a multiple of both three and five print the word
'FizzBuzz'.
"""
import PySimpleGUI as sg
from termcolor import colored as cl

# Add a touch of color
sg.theme('DarkBlue2') 
  
# All the stuff inside your window.
question = [ [sg.Text('Please enter the beginning of the desired number range.'),
             sg.InputText()],
            [sg.Text('Please enter the end of the desired number range.'), 
             sg.InputText()],
            [sg.Button('Ok')], [sg.Button('Cancel')]
        ]

def fizzBuzz(start,stop):
    
    #Create a file to hold the answer
    file = open('fizzBuzz.txt', "w")
    
    for i in range(int(start), int(stop) + 1):
        
        if (i%3 == 0) and (i%5 != 0):
            file.write('Fizz\n')
            print(cl('Fizz','red'))
        elif (i%5 == 0) and (i%3 != 0):
            file.write('Buzz\n')
            print(cl('Buzz','blue'))
        elif (i%3==0) and (i%5==0):
            file.write('FizzBuzz\n')
            print(cl('FizzBuzz','magenta'))
        elif (i%3!=0) and (i%5!=0):
            file.write(str(i))
            file.write('\n')
            print(str(i))
     
    file.close()   

def main():
    # Create the Window
    window = sg.Window('FizzBuzz', question)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        elif event in ('Ok'):
            fizzBuzz(values[0],values[1])
            window.close()
    
    window.close()

main()
