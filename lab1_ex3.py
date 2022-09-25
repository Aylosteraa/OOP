import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--expression", type=str, default=None)
args = parser.parse_args()

if args.expression is None or not (args.expression[-1].isdigit()):
    sys.exit("False None")

for i in range(len(args.expression)):
    if not (args.expression[i] in ('+', '-') or args.expression[i].isdigit()):
        sys.exit("False None")
    if args.expression[i] in ('+', '-'):
        if args.expression[i + 1] in ('+', '-'):
            sys.exit("False None")

print(True, eval(args.expression))
