import argparse

my_parser = argparse.ArgumentParser(description = 'Output Text in Terminal')
my_parser.add_argument('filename1', help = 'First filename')
my_parser.add_argument('-n', action = 'store_true',
                       help = 'Line Number Flag')
args = my_parser.parse_args()
f = open(args.filename1)
if (args.n):
    line_number = 1
    line = f.readline()
    while(line):
        print('    ', line_number, line, end = '')
        line_number+=1
        line = f.readline()
else:
    line = f.readline()
    while(line):
        print(line, end = '')
        line = f.readline()
    
