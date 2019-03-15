import time
import sys

#Module for duplicating console output to log file

#module attributes
attributes = {"Name":"loggger",
              "Type":"lib",
              "Description":"Logging to file module"}

#log file
filename = 'abnormal-{}.log'.format(time.strftime("%Y-%m-%d_%H-%M")) 

class Logger():
    """Class for duplicating <stream> to file."""
    def __init__(self, stream, file):
        self.stream = stream
        self.log = file

    def write(self, message):
        self.stream.write(message)
        self.log.write(message)
        self.flush()

    def flush(self):
        self.log.flush()
        pass

def init():
    """Create logger for stdout and stderr."""
    f = open(filename , encoding='utf-8', mode='a')

    sys.stdout = Logger(sys.stdout, f)
    sys.stderr = Logger(sys.stderr, f)
