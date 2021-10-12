# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("x", type=int, help="the base")
# parser.add_argument("y", type=int, help="the exponent")
# parser.add_argument("-v", "--verbosity", action="count", default=0)
# args = parser.parse_args()
# answer = args.x**args.y
# if args.verbosity >= 2:                 # (PS C:\Users\user\PycharmProjects\pythonProject\pythonProject> python .\argsparser.py 10 20 -v -v -v)
#     print("Running '{}'".format(__file__))
# if args.verbosity >= 1:                 # (PS C:\Users\user\PycharmProjects\pythonProject\pythonProject> python .\argsparser.py 10 20 -v)
#     print("{}^{} == ".format(args.x, args.y), end="")
# print(answer)

"""python3 prog.py 4 2
16
python3 prog.py 4 2 -v
4^2 == 16
python3 prog.py 4 2 -vv
Running 'prog.py'
4^2 == 16"""








import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
print(args.x**args.y)


"""$ python3 prog.py 4 2
4^2 == 16
$ python3 prog.py 4 2 -q
16
$ python3 prog.py 4 2 -v
4 to the power 2 equals 16
$ python3 prog.py 4 2 -vq
usage: prog.py [-h] [-v | -q] x y
prog.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
$ python3 prog.py 4 2 -v --quiet
usage: prog.py [-h] [-v | -q] x y
prog.py: error: argument -q/--quiet: not allowed with argument -v/--verbose"""








# import argparse
#
# parser = argparse.ArgumentParser(description="calculate X to the power of Y")
# group = parser.add_mutually_exclusive_group()
# group.add_argument("-v", "--verbose", action="store_true")
# group.add_argument("-q", "--quiet", action="store_true")
# parser.add_argument("x", type=int, help="the base")
# parser.add_argument("y", type=int, help="the exponent")
# args = parser.parse_args()
# answer = args.x**args.y
#
# if args.quiet:
#     print(answer)
# elif args.verbose:
#     print("{} to the power {} equals {}".format(args.x, args.y, answer))
# else:
#     print("{}^{} == {}".format(args.x, args.y, answer))