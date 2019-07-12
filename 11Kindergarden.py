x=int(input())
if(x%2==0):
    pair=x//2
    p1=pair*(x-1)
    print(p1)
elif x%2!=0:
    print(x*(x//2))
    
