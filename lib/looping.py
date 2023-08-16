#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 0
    while i < 10:
        i += 1
        return('Happy New Year!')
        

def square_integers(int_list):
    # code goes here!
    squared_list = [num * num for num in int_list]
    return squared_list
    

def fizzbuzz():
    # code goes here!
    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            return('FizzBuzz')
        elif num % 3:
            return('Fizz')
        elif num % 5:
            return('Buzz')
        else:
            return(num)
        

