n=int(input())
for i in range(n):
	j=int(input())
	k=j**(1/2)
	a=int(k)
	if k-a>=0.5:
		print(a+1)
	else:
		print(a)
