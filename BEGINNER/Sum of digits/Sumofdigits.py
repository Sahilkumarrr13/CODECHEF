n=int(input())
for i in range(n):
	j=input()
	l=[]
	for x in range(len(j)):
		l.append(int(j[x]))
	print(sum(l))
