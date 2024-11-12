n=int(input('Please enter the number of rows: '))
for row in range(n):
    for col in range(row+1):
        print('*',end=' ')
    print()