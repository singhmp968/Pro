a,b=input().strip().split(" ")
co=0
len1=abs(len(a)-len(b))

if(a==b):
        print(0)
else:
    for i in range(len(a)):
        if len(b)==0 and a[i] in b:
            break

            if(a[i]!=b[i]):
                    len1=len1+1
print(len1)
