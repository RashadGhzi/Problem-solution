# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number",
#                     type=int)
# args = parser.parse_args()
# print(args.square**2)




# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbosity", help="write verbose")
# args = parser.parse_args()
# if args.verbosity:                     # Command line access only write (--verbosity verbosity) in power shell admin
#     print("verbosity turned on")




# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbose", help="only write verbose",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:                        # Command line acces only write (--virbose) in power shell admin
#     print("verbosity turned on")


# How to access powershill admin:
# 1. cd ~
# 2. cd 'add your file now you are working on' example:cd .\PycharmProjects\
# 3.python 'add your progaramm name' example:python .\argsparser.py\





# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print("the square of {} equals {}".format(args.square, answer))
# else:
#     print(answer)





# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int,
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity == 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)





import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)





# import argparse
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







# import argparse
#
# parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group()
# group.add_argument("-v", "--verbose", action="store_true")
# group.add_argument("-q", "--quiet", action="store_true")
# parser.add_argument("x", type=int, help="the base")
# parser.add_argument("y", type=int, help="the exponent")
# args = parser.parse_args()
# print(args.x**args.y)


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