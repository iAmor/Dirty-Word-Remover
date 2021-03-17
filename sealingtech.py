import sys
import re

#checks for correctly formatted command line
if len(sys.argv) != 3:
    raise RuntimeError("Run program as: python sealingtech.py inputfile.txt configfile.txt")

#checks files exist
try:
    open(sys.argv[1], "r")
except:
    raise IOError("Input file not found")
try:
    open(sys.argv[2], "r")
except:
    raise IOError("Config file not found")

#takes the original and config files as inputs from the command line
original = sys.argv[1]
config = sys.argv[2]

#opens each file and reads each dirty word into a list
cfg = open(config)
dirty_list = cfg.read().split("\n")
cfg.close()

with open("out.txt", "w") as out, open(original, "r") as inp:
    for l in inp:
        l = l.split()
        flag = 0
        #checks each word in a line to see if it matches with any dirty word
        for i in range(len(l)):
            if (True in [bool(re.fullmatch(word, l[i])) for word in dirty_list]):
                continue
            else:
                #if not dirty, writes the word into the output file
                if i != 0 and flag == 1:
                    out.write(" ")
                out.write(l[i])
                flag = 1
        out.write("\n")
out.close()
inp.close()
