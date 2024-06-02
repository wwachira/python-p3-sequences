#!/usr/bin/env python3

def print_fibonacci(length):
    a, b = 0, 1 
    for _ in range(length):
        print(a, end='')
        a,b = b, a+b
        print()
print_fibonacci(9)
    