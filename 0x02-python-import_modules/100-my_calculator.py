#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        s = "{:d} {:s} {:d} = {:d}"
        if args[2] == "+":
            print(s.format(int(a), argv[2], int(b), add(int(a), int(b))))
            exit(0)
        elif args[2] == "-":
            print(s.format(int(a), argv[2], int(b), sub(int(a), int(b))))
            exit(0)
        elif args[2] == "*":
            print(s.format(int(a), argv[2], int(b), mul(int(a), int(b))))
            exit(0)
        elif args[2] == "/":
            print(s.format(int(a), argv[2], int(b), div(int(a), int(b))))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
