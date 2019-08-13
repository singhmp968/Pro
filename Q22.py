n=int(input())
l1=list(map(int,input().split()))
a1=l1[1:n:2]
a2=l1[0:n:2]
if(sum(a1)>=sum(a2)):
    print(sum(a1))
else:
    print(sum(a2))
