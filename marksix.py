# randomly generate 6 numbers from 1..49 (marksix) 

import random
a=list(range(1,50))
b=list(range(0,6))
random.shuffle(a)
for i in range(0,6):
	b[i]=a[i]

b.sort()
#for i in range(0,6):
#	print(b[i])

print(b)
