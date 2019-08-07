n1=int(input())
l1=list(map(int,input().split()))
i=1
sum1=0
while(i<n1):
	for x1 in l1[:i]:
		if(x1<l1[i]):
			sum1+=x1
	i+=1
print(sum1)
