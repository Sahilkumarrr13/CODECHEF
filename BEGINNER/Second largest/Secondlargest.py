n=int(input())
for i in range(n):
	l=list(map(int,input().split()))
	l.sort()
	print(l[1])
