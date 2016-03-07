#!/usr/bin/python

# randomly generate 6 numbers from 1..49 (marksix) 
import random

MAXNUM=49
drawcount=6

drawpool=list(range(1,MAXNUM+1))
result=list(range(0,drawcount))
random.shuffle(drawpool)
for i in range(0,drawcount):
	result[i]=drawpool[i]

result.sort()

print(result)
