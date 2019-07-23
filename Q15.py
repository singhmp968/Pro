n1 = int(input())
l1 = list(map(int,input().split()))
l1 = [bin(x) for x in l1]
l1.sort(reverse=True)
l1 = [int(x,2) for x in l1]
for x in l1:
    print(x)
