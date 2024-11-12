n=int(input('Please enter the amount of rows: '))
for row in range(n+1):
    print(' '*(n-row),end=' ')
    for column in range(1,row+1):
        print('*',end=' ')
    print()
for row in range(n-1,0,-1):
    print(' '*(n-row),end=' ')
    for column in range(1,row+1):
        print('*',end=' ')
    print()