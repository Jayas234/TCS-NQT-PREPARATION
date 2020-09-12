n=int(input())
c=0
c1=0
for i in range(0,n+1):
    if i%2==0:
        c=c+i
        #print(i)
    else:
        c1=c1+i
        #print(c1)
print("Sum of Even Numbers is",c)
print("Sum of Odd Numbers is",c1)


''' 1 2 3 4 5
1+3+5
2+4
'''
