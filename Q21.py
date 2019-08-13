n1=int(input())
l1=list(map(int,input().split()))
a1=l1[:n1//2]
b1=l1[n1//2:]
if(sum(a1)//len(a1)==sum(b1)//len(b1)):
	print('yes')
	exit()
print('no')
