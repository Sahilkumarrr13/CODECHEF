n=int(input())
for i in range(n):
	x=input()
	l=len(x);li=[]
	for i in range(l):
		li.append(x[i])
	j=0
	sum=0
	while j<len(li):
		if li[j]=='4':
			sum+=1
		else:
			pass
		j+=1
	print(sum)
