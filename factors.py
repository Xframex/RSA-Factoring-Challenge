#!/usr/bin/env python3

def factorize(number):
    factors = []
    div = 2
    while number > 1:
        while number % div == 0:
            factors.append(div)
            number //= div
        div += 1
    return factors

if __name__ == "__main__":
    print("This script should be imported and used as a function.")
