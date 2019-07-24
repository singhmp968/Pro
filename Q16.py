n=int(input())
l1=list(map(int,input().split()))
c=[1]*n
for i in range(n):
    if(i==0 and l1[i]>l1[i+1]):
        
        c[i]=c[i]+c[i+1]
    if i>0  and l1[i]>l1[i-1]:
        c[i]=c[i]+c[i-1]
s=sum(c)
print(s)
