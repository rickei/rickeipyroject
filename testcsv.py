import csv
import sys

f = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(f,delimiter=' ')
    for row in reader:
        print (row)
finally:
    f.close()
