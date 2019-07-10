x=int(input())
count=0
li=list(map(int,input().split(" ")))
for i in range(0,x-2,1):
       
       for j in range(1,x-1,1):
               
               for k in range(2,x,1):
                       if(li[i]<li[j] and li[j]<li[k]):
                               count=count+1
print(count)
