# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:28:13 2020

The Self-Taught Programmer by Cory Althoff

Chapter 3 (Introduction to Programming) Challenges
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from termcolor import colored as cl
import random as rn

def taskOne():
    #Print three different strings
    #I added a bit more to this task by pulling three different 
    #quotes from GoodReads
    goodReads = "https://www.goodreads.com/quotes"
    goodClient = req(goodReads)
    quote_parse = soup(goodClient.read(), "lxml")
    goodClient.close()
    
    #Hold quotes into list from main page 
    hold = quote_parse.find_all("div", {"class": "quoteText"})
    
    #String one prints a random quote with its author
    strOneRn = rn.randrange(30)
    strOneQte = hold[strOneRn].text.strip().split("\n")[0]
    strOneAthr = hold[strOneRn].text.strip().split("\n")[3].strip()
    string_one = strOneQte + " ~ " + strOneAthr.strip() 
    
    #String two prints a random quote with its author
    strTwoRn = rn.randrange(30)
    strTwoRan = rn.randint(0,30) if strTwoRn == strOneRn else strTwoRn
    strTwoQte = hold[strTwoRan].text.strip().split("\n")[0]
    strTwoAthr = hold[strTwoRan].text.strip().split("\n")[3].strip()
    string_two = strTwoQte + " ~ " + strTwoAthr.strip() 

    #String three prints a random quote with its author
    strThreeRn = rn.randrange(30)
    strThreeRan = rn.randint(0,30) if strThreeRn == (strTwoRn or strOneRn) else strThreeRn 
    strThreeQte = hold[strThreeRan].text.strip().split("\n")[0]
    strThreeAthr = hold[strThreeRan].text.strip().split("\n")[3].strip()
    string_three = strThreeQte + " ~ " + strThreeAthr.strip() 
    
    print("This task prints out three strings, or rather three quotes.\n" )
    print(cl(string_one + "\n", "cyan"))
    print(cl(string_two + "\n", "green"))
    print(cl(string_three, "blue"))
    
    del hold

def taskTwo():
    """
    Write a program that prints a message if a variable
    is less than 10, and a different message if a variable
    is greater than or equal to 10.
    """
    
    strLess = "Books are a uniquely portable magic. ~ Stephen King"
    strGrtTen = """\tMemories warm you up from the inside. 
                But they also tear you apart. ~ Haruki Murakami"""
    
    pick = input("Please pick a number from 0 to 20 to get a quote: ")
    
    checker = [str(i) for i in range(0,21)]
    
    if pick in checker:
        print(cl(strLess,"cyan") if int(pick) < 10 else cl(strGrtTen, "green"))
    else:
        print(cl("Please try again!\n", "red"))
        taskTwo()
    
    del checker
    
def taskThree():
    """
    Write a program that prints a message if a variable is less than 
    or equal to 10, another message if a variable is greater than 10
    but less than or equal to 25, and another message if a variable is
    greater than 25.
    """
    
    value = input("Please choose a number from 0 to 50: ")
    checkr = [str(i) for i in range(0, 51)]
    
    if value in checkr:
        if int(value) <= 10:
            print(value + "? That's a nice choice!")
        elif int(value) > 10 and int(value) <= 25:
            print("Did you choose " + value + "? Wonderful!")
        elif int(value) > 25:
            print("Picking a really high number, huh?")
    else:
        print("Please try again!")
        taskThree()
    
    
def taskFour():
    #Create a program that divides two variables and prints the remainder
    
    print(cl("Choose two numbers and we shall return the " +
             "remainder from its division.","magenta"))
    
    num_one = input("Choose a dividend: ")
    num_two = input("Now, choose a divisor: ")
    
    remainder = int(num_one) % int(num_two)
    print("\n")
    print(num_one + " divided by " + num_two + " returns a remainder of " + str(remainder))
    
    
def taskFive():
    #Create a program that takes two variables, divides them, and prints
    #the quotient
    
    print(cl("Choose two numbers and we shall return the " +
         "quotient from its division.","magenta"))
    
    num_one = input("Choose a dividend: ")
    num_two = input("Now, choose a divisor: ")
    
    quotient = int(num_one) / int(num_two)
    print("\n")
    print(num_one + " divided by " + num_two + " returns a quotient of " + str(quotient))

    

def taskSix():
    """
    Write a program with a variable 'age' assigned to an integer 
    that prints different strings depending on what integer 'age' is
    """
    
    quote_one = """The timeless in you is aware of life's timelessness.
    And knows that yesterday is but today's memory and tomorrow is today's dream.
    ~ Khalil Gibran"""
    quote_two = "What happens when people open their hearts? They get better. ~ Haruki Murakami"
    quote_three = "You only live once, but if you do it right, once is enough. ~ Mae West"
    quote_four = """I've learned that people will forget what you said, 
    people will forget what you did, but people will never forget 
    how you made them feel.
    ~ Maya Angelou"""
    quote_five = """Non est ad astra mollis e terris via.
    (There is no easy way from the earth to the stars)
    ~ Seneca"""
    
    age = input("How old are you? ")
    
    if int(age) <= 10:
        print(cl("Life has yet begun for you!", "cyan"))
    elif int(age) > 10 and int(age) <= 20:
        print(cl(quote_one + "\n", "magenta"))
    elif int(age) > 20 and int(age) <= 40:
        print(cl(quote_two + "\n", "blue"))
    elif int(age) > 40 and int(age) <= 60:
        print(cl(quote_three + "\n", "green"))
    elif int(age) > 60 and int(age) <= 80:
        print(cl(quote_four + "\n", "magenta"))
    elif int(age) > 80:
        print(cl(quote_five + "\n", "cyan"))

def main():
    
    #Let the user pick a task which will 
    #return that task's solution
    
    print(cl("Welcome! This program prints out the solutions " +
             "of the challenges section in Chapter Three "+
             "of Cory Althoff's The Self-Taught Programmer. ", "blue"))

    task = input(cl("Please choose a task by typing" + 
                    "in a number from 1 to 6: ", "blue"))
    
    check = [str(i) for i in range(1,7)]
    
    if task in check:
        print(cl("Thank you for choosing a task! The solution will now print.",
                 "magenta"))
        if task == check[0]:
            taskOne()
        elif task == check[1]:
            taskTwo()
        elif task == check[2]:
            taskThree()
        elif task == check[3]:
            taskFour()
        elif task == check[4]:
            taskFive()
        elif task == check[5]:
            taskSix()
    else:
        print(cl("Please choose a number between 1 to 6!", "red"))
        main()
        
        
main()
