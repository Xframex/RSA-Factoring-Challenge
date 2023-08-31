#!/usr/bin/env python3
import sys


def factorize(number):
    for div in range(2, number):
        if number % div == 0:
            return div, number // div
    return None, None


def main():
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    # Get the filename from command line arguments
    filename = sys.argv[1]

    try:
        # Open the file using a context manager
        with open(filename, "r") as stream:
            for line in stream:
                number = int(line.strip())
                p, q = factorize(number)
                if p is not None and q is not None:
                    print(f"{number} = {p} * {q}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
