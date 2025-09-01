#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if len(sys.argv) < 2:
    print("Usage: python3 factorial.py <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Please provide an integer.")
    sys.exit(1)

if n < 0:
    print("Please provide a non-negative integer.")
    sys.exit(1)

f = factorial(n)
print(f)
