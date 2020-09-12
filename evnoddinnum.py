n=list(map(int,input().split()))
c=0
c1=0
for i in range(len(n)):
    if n[i]%2==0:
        c=c+1
    else:
        c1=c1+1
print("Even ",c)

print("odd ",c1)
