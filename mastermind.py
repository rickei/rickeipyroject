import random

digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
resultstr=""
random.shuffle(digit)
cell_1 = digit[0]
random.shuffle(digit)
cell_2 = digit[0]
random.shuffle(digit)
cell_3 = digit[0]
random.shuffle(digit)
cell_4 = digit[0]
cell = cell_1 + cell_2 + cell_3 + cell_4

while True:

    print("input 4 digits (type exit to exit):")
    a = input()
    if a.upper() == 'EXIT':
        print("bye")
        break

    if a[0] == cell[0]:
        resultstr += "o"
    else:
        if a[0] in cell:
            resultstr += "x"

    if a[1] == cell[1]:
        resultstr += "o"
    else:
        if a[1] in cell:
            resultstr += "x"

    if a[2] == cell[2]:
        resultstr += "o"
    else:
        if a[2] in cell:
            resultstr += "x"

    if a[3] == cell[3]:
        resultstr += "o"
    else:
        if a[3] in cell:
            resultstr += "x"

    print(resultstr)
# print(cell_1)
# print(cell_2)
# print(cell_3)
# print(cell_4)
