#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if args[2] not in "+-*/":
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            a = int(args[1])
            b = int(args[3])
            operations = {"+": add, "-": sub, "*": mul, "/": div}
            s = "{:d} {:s} {:d} = {:d}"
            print(s.format(a, args[2], b, oparations[args[2]](a, b)))
            sys.exit(0)
