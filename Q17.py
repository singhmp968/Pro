n,k=list(map(int,input().split()))
l1=list(map(int,input().split()))
ans="no"
for i in range(len(l1)):
               
               for j in range(i+1,len(l1)):
                   if(l1[i]+j==k):
                        ans="yes"
                        break
print(ans)
