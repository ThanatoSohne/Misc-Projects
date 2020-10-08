# -*- coding: utf-8 -*-
"""
The Self-Taught Programmer by Cory Althoff

Chapter 4 (Functions) Challenge
"""

def squareThis(n):
    """
    Objective: Write a function that takes a number
               as an input and returns that number squared.
    Returns n**2
    :param n: int.
    :return: int n squared
    """
    
    return n**2

def printThis(stn):
    """
    Objective: Create a function that accepts a string as a parameter 
               and prints it.
    Returns print(n)
    :param n: string.
    :return print(n)
    """
    
    if type(stn) == str:
        print(stn)
    else:
        print("Need a string")

def openFunction(x, y, z, a=2, b=3):
    """
    Objective: Write a function that takes 3 required parameters
               and 2 optional parameters.
    Returns sqr + cubed + sqroot
    :library: math
    :param x: int.
    :param y: int.
    :param z: int.
    :return: int (x**2)+(y**3)+(math.sqrt(z))
    """
    
    import math
    
    sqr = x**2
    cubed = y**3
    sqroot = math.sqrt(z)
    
    return sqr + cubed + sqroot

"""
Objective for divThis() and multiThis():
    Write two functions wherein the first function
    should take an integer as a parameter and return the
    result of the integer divided by 2. The second function
    should take an int as a parameter and return the result
    of the int multiplied by 4. Call the first function,
    save the result as a variable, and pass it as a parameter
    to the second function.
"""
def divThis(n):
    """
    Returns n divided by 2
    :param n: int.
    :return: n/2
    """
    
    return n/2

def multiThis(n):
    """
    Returns n multiplied by 4
    :param n: int.
    :return: n*4
    """
    
    return n*4

def convertStr(strn):
    """
    Objective: Write a function that converts a string to a float
               and returns the result. Use exception handling to catch
               the exception that could occur.
    Converts a string to float
    :param strn: str.
    :return: float(strn)
    """
    
    return float(strn)

def main():
    
    num = 30
    #Quote from Pablo Neruda
    quote = "You can cut all the flowers but you cannot keep Spring from coming"
    
    print(squareThis(num))
    printThis(quote)
    print(int(openFunction(num, 4, 5)))
    
    numNew = divThis(num)
    print(multiThis(numNew))
    
    try: 
        convertStr(quote)
    except ValueError:
        print("Cannot print")
        
main()
    
    

