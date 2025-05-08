#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Fix: decrement n to prevent infinite loop
    return result

if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Error: Factorial is only defined for non-negative integers.")
        else:
            print(factorial(num))
    except ValueError:
        print("Error: Please provide a valid integer.")
else:
    print("Usage: ./factorial.py <integer>")
