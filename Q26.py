n1=input()
l1=list(map(int,input().split()))
for i in range(len(l1)):
	for j in range(len(l1)):
		if(l1[j]>l1[i]):
