#!/usr/bin/env python3

def happy_new_year():
    for i in range(10):
        print(10 - i)
    print("Happy New Year!")

def square_integers(int_list):
    tmp = [x**2 for x in int_list]
    return tmp

def fizzbuzz():
    for i in range (100):
        n = i + 1
        if (n % 3 == 0):
            if (n % 5 == 0):
                print("FizzBuzz")
            else:
                print("Fizz")
        elif (n % 5 == 0):
            print("Buzz")
        else:
            print(n)
        
    pass
