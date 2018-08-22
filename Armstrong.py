'''
Author: Chane van der Berg
Date: 13/05/2018

An Armstrong number is an n-digit number that is equal to the sum of
the nth powers of its individual digits.

Write a Python program to accept as input an integer from the user and
passes the integer to a function, Armstrong(), which determines whether
the number is an Armstrong number or not.

The Armstrong() function should accept an integer, determine whether
the number is an Armstrong number or not, and returns a 1 (true) or
0 (false) to the calling statement in the main program.

'''

def Armstrong(n):
    num = len(str(n))

    a = 0
    b = n
    while b > 0:
        c = b % 10
        a += c ** num
        b //= 10

    if n == a:
        print(str(n),"IS an armstrong number")
    else:
        print(str(n),"IS NOT an armstrong number")

n = int(input("Enter an integer number: "))
Armstrong(n)
