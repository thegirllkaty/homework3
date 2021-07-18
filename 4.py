x = int(input('Enter A: '))
y = int(input('Enter B: '))
if x < y:
    for i in range(x, y+1):
        print(i)
else:
    for j in range(x, y-1, -1): # у-1 элемент идущий после последнего
        print(j)