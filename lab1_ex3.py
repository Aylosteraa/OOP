import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--expression", type=str, default=None)
args = parser.parse_args()

if args.expression is None:
    sys.exit("False None")
sign_num = ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
boo_l = True
for i in range(len(args.expression)):
    boo_l = args.expression[i] in sign_num
    if boo_l is False:
        sys.exit("False None")
    if args.expression[i] == '+' or args.expression[i] == '-':
        if args.expression[i+1] == '+' or args.expression[i] == '-':
            sys.exit("False None")
print(boo_l, eval(args.expression))
