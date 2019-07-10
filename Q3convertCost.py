a,b=input().strip().split(" ")
co=0
if (len(a)==len(b)):
    co=0
elif (a==b):
        co=0
len1=abs(len(a)-len(b))
for i in range(len(a)):
        if(a[i]!=b[i]):
                len1=len1+1
print(len1)
