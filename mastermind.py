
import random

digit=["1","2","3","4","5","6","7","8","9"]
random.shuffle(digit)
cell_1=digit[0]
random.shuffle(digit)
cell_2=digit[0]
random.shuffle(digit)
cell_3=digit[0]
random.shuffle(digit)
cell_4=digit[0]

while True:

	print("input 4 digits (type exit to exit):")
	a=input()
	if a.upper()=='EXIT':
		print("bye")
		break
	if a==cell_1:
		print("ok")

#print(cell_1)
#print(cell_2)
#print(cell_3)
#print(cell_4)
