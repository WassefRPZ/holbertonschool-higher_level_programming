#!/usr/bin/python3
import calculator_1


def main():
    a = 10
    b = 5

    result = (a + b)
    print("{} + {} = {}".format(a, b, result))

    result = (a - b)
    print("{} - {} = {}".format(a, b, result))

    result = (a * b)
    print("{} * {} = {}".format(a, b, result))

    result = (a // b)
    print("{} // {} = {}".format(a, b, result))


if __name__ == "__main__":
    main()
