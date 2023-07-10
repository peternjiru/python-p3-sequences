#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        fibonacci = []
    elif length == 1:
        fibonacci = [0]
    else:
        fibonacci = [0, 1]
        while len(fibonacci) < length:
            next_num = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(next_num)
    print(fibonacci)
