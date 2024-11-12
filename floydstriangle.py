n=int(input('Please enter the number of rows: '))
num=1
for rows in range(n):
    for column in range(rows+1):
        print(num,end=' ')
        num+=1
    print()