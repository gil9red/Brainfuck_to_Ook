import argparse
import os
import sys

__author__ = 'ipetrash'

table = {
    '>': "Ook. Ook?",
    '<': "Ook? Ook.",
    '+': "Ook. Ook.",
    '-': "Ook! Ook!",
    '.': "Ook! Ook.",
    ',': "Ook. Ook!",
    '[': "Ook! Ook?",
    ']': "Ook? Ook!",
}


def create_parser():
    parser = argparse.ArgumentParser(description="Brainfuck converter in Ook!")
    parser.add_argument("bf_file_name", type=str, help="Brainfuck file name")
    parser.add_argument("-out", type=str, help="Ook! file name. Default save in dir the bf_file_name.")
    parser.add_argument("-print", action="store_true", help="Output Ook! source code")
    return parser


def main(args):
    bf_file_name = os.path.normpath(args.bf_file_name)
    dir_name, file_name = os.path.split(bf_file_name)
    file_base_name, file_extension = os.path.splitext(file_name)
    ook_file_name = os.path.join(dir_name, file_base_name + ".Ook!")  # Default file name Ook!

    if args.out:  # If exist -out
        ook_file_name = args.out

    if os.path.exists(bf_file_name):
        bf_source = open(bf_file_name).read()
        ook_commands = []
        for bf_op in bf_source:
            ook_op = table.get(bf_op)
            if ook_op:
                ook_commands.append(ook_op)

        ook_source = ' '.join(ook_commands)
        if args.print:
            print('\n"'+ ook_source + '\n"')

        if not os.path.exists(os.path.dirname(ook_file_name)):
            os.makedirs(os.path.dirname(ook_file_name))

        f = open(ook_file_name, "w")
        f.write(ook_source)
        f.close()
    else:
        print("File name '%s' not exist!" % bf_file_name)
        return 1

    return 0


if __name__ == '__main__':
    parser = create_parser()

    if len(sys.argv) is 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        print("Return: %d" % main(args))