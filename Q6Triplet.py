x=int(input())
c=0
li=list(map(int,input().split(" ")))
for i in range(0,x-2):
       
       for j in range(i+1,x-1):
               
               for k in range(j+2,x):
                       if(li[i]<li[j] and li[j]<li[k]):
                               c+=1
print(c)
