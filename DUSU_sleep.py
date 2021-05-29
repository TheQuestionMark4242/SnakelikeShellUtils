import argparse
import time
my_parser = argparse.ArgumentParser(description = 'Suspend shell for specified time')
my_parser.add_argument('time', help = 'Time to sleep for')
args = my_parser.parse_args()
if(args.time[-1]=='m'):
    timer = 60*int(args.time[:-1])
elif(args.time[-1]=='h'):
    timer = 3600*int(args.time[:-1])
elif(args.time[-1]=='s'):
    timer = int(args.time[:-1])
else:
    timer = int(args.time)

time.sleep(timer)
    

