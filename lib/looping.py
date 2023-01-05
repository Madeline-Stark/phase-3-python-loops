#!/usr/bin/env python3

def happy_new_year():
    # code goes here
    i = 10
    while i >= 1:
        print(i)
        i -=1
    print("Happy New Year!")
    # using a while loop that outputs numbers starting at 10 and counting down to 1. 
    # After reaching 1, print out "Happy New Year!"
    pass

def square_integers(int_list):
    # code goes here
    squared_elements = [el * el for el in int_list]
    return squared_elements
    # takes one argument, a list of integers 
    # and returns the list of squared elements.
    pass

def fizzbuzz():
    # code goes here
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
    # prints the numbers from 1 to 100. 
    # For multiples of three, print "Fizz" instead of the number 
    # and for the multiples of five print "Buzz". 
    # For numbers which are multiples of both three and five, print "FizzBuzz".
    pass
