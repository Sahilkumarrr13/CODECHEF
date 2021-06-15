n=int(input())
for i in range(n):
	x=int(input())
	j=1;fact=1
	while j<x+1:
		fact=fact*j
		j+=1
	print(fact)
