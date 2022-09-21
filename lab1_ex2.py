import argparse
import operator

parser = argparse.ArgumentParser()
parser.add_argument("operation", type=str)
parser.add_argument("integers", type=int, nargs='+')
args = parser.parse_args()

y = dir(operator)
if args.operation in y:
    x = getattr(operator, args.operation)
    res = args.integers[0]
    for i in range(1, len(args.integers)):
        res = x(args.integers[i], res)
    print(res)
else:
    print("Error! This operation can't be calculated.")

