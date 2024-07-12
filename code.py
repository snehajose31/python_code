for i in range(0,4):
    for k in range(0,8):
        if k % 2 != 0:
            print(" ___",end='      ')
    print()
    for j in range(0,4):
        print("/ ",end='   ')
        print("\ ", end='   ')
    print()
    for j in range(0, 4):
        print("\ ", end='   ')
        print("/ ", end='   ')
    print()