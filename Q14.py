a,b=map(int,input().split())
li=list(map(int,input().split()))[:a]
res=[]
while(b):
    x=list(map(int,input().split()))
    res.append(x)
    b=b-1
print(res)    
for i in res:
    ans=0
    for j in range(i[0]-1,i[1]):
       ans=ans^li[j]
    print(ans)
