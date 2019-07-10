n1=int(input())
k2=[]
for i in range(0,n1):
  l=input()
  k2.append(l)
m1=[]
for i in zip(*k2):
  if(i.count(i[0])==len(i)):
    m1.append(i[0])
  else:
    break
print(''.join(m1))
