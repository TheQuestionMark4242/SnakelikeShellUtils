import argparse

my_parser = argparse.ArgumentParser(description = 'Shell utility to create a new file')
my_parser.add_argument('file', help = 'Name of file to be created', metavar = 'File Name')
args = my_parser.parse_args()
with open(args.file, 'w') as fp:
    pass






