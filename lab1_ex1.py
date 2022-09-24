import argparse

parser = argparse.ArgumentParser(description="Arithmetic operation")
parser.add_argument("int1", type=str)
parser.add_argument("operation", type=str)
parser.add_argument("int2", type=str)
args = parser.parse_args()

if args.operation in ('+', '-', '*', '/') and args.int1.isdigit() and args.int2.isdigit():
    if args.operation == '/' and args.int2 == '0':
        print("Error! Division by zero.")
    else:
        print(eval(args.int1 + args.operation + args.int2))
else:
    print("Error! This operation can't be calculated.")
