import argparse

my_parser = argparse.ArgumentParser(description = 'Shell Utility to copy contents of a file to a new file')
my_parser.add_argument('source_file', help = 'File to be copied',
                       metavar = 'Source File')
my_parser.add_argument('target_file', help = 'File to copy contents to',
                       metavar = 'Target File')
args = my_parser.parse_args()

sf = open(args.source_file,'r')
tf = open(args.target_file,'w')

tf.write(sf.read())
sf.close
tf.close
