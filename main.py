#!/usr/bin/env python3
from factors import factorize

def main():
    input_numbers = [
        4, 12, 34, 128, 1024, 4958, 1718944270642558716715,
        9, 99, 999, 9999, 9797973, 49, 239809320265259
    ]

    for number in input_numbers:
        factors = factorize(number)
        factor_str = " * ".join(map(str, factors))
        print(f"{number} = {factor_str}")

if __name__ == "__main__":
    main()
