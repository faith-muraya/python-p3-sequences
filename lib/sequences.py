#!/usr/bin/env python3

def print_fibonacci(length):
    fib_seq = []
    if length >= 1:
        fib_seq.append(0)
    if length >= 2:
        fib_seq.append(1)
    if length >= 3:
        a, b = 0, 1
        for _ in range(length-2):
            fib_seq.append(a + b)
            a, b = b, a + b
    print(fib_seq)