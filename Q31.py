def maxsum(l,count):
	if(len(l)==0):
		return count
	x1=maxsum(g[l[0]-1],count+l[0])
	y1=maxsum(l[1:],count)
	return max(x1,y1)

n1,m1=map(int,input().split())
g=[]
for _ in range(n1):
	g.append([])
for _ in range(m1):
	a1,b1=list(map(int,input().split()))
	g[a1-1].append(b1)
s=maxsum(g[0],1)
print(s)
