import argparse
import sys

parser = argparse.ArgumentParser(description="Arithmetic operation")
parser.add_argument("operation", type=str)
args = parser.parse_args()

op = ['+', '-', '*', '/']
for i in args.operation:
    boo_l = i in op or i.isdigit()
    if boo_l is False:
        sys.exit("Error! This operation can't be calculated.")
 print(eval(args.operation))

