import argparse
import operator
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument("operation", type=str)
parser.add_argument("integers", type=int, nargs='+')
args = parser.parse_args()

if args.operation in dir(operator):
    x = getattr(operator, args.operation)
elif args.operation in dir(math):
    x = getattr(math, args.operation)
else:
    sys.exit("Error! This operation can't be calculated.")
if len(args.integers) == 1:
    res = x(args.integers[0])
else:
    res = args.integers[0]
    for i in range(1, len(args.integers)):
        res = x(res, args.integers[i])
print(res)
