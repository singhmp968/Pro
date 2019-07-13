"""def buildTree(li,tree,start,end,treeNode):
    if(start==end):
        tree[treeNode]=li[start]
        return
    mid=(start+end)/2
    buildTree(li,tree,start,mid,2*treeNode)
    buildTree(li,tree,mid+1,end,2*treeNode)
    tree[treeNode]=tree[2*treeNode] + tree[2*treeNode+1]
    return tree
li=[1,2,3,4,5,6,7,8,9]
x=[]
li1=int(2*len(li))
buildTree(li,x,0,8,1);
for i in range(1,li1,1):
    print(x[i],end=" ")"""
a,b=input().split()
p=list(map(int,input().split()))
for i in range(int(b)):
    u,v=input().split()
    sum=0
    for z in range(int(u)-1,int(v)):
        sum=sum+p[z]
    print(sum)
    continue
