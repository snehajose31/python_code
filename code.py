value = input("Enter Two Number Separate by space")
num = value.split()
x = int(num[0])
y = int(num[1])
for i in range(0,x):
    for k in range(0,y+1):
        if k % 2 != 0:
            print(" ___",end='      ')
    print()
    for j in range(0,x):
        print("/ ",end='   ')
        print("\ ", end= '   'if j== x-1  else '___')
    print()
    for j in range(0, x):
        print("\ ", end='   ')
        print("/ ", end='   ')
    print()
for k in range(0,y+1):
    if k % 2 != 0:
        print(" ___",end='      ') 