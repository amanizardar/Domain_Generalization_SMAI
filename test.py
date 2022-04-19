from sys import flags
from arg_reader import parser as my_parser

flags = my_parser()

print(flags.inner_loops)