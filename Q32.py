n1,m1=map(int,input().split())
l1=[]
for _ in range(n1):
	l1.append(sorted(list(map(int,input().split()))))
for i in range(n1-1):
	for j in range(m1):
		for k in range(n1-i):
			if(l1[i][j]>l1[i+k][j]):
				l1[i][j],l1[i+k][j]=l1[i+k][j],l1[i][j]
for i in l1:
	print(*i,sep=' ')
