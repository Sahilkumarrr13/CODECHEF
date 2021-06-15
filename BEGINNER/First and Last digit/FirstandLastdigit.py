n=int(input())
for i in range(n):
	j=input()
	l=len(j)
	j=int(j)
	first = j//10**(l-1)
	last = j%10
	print(first+last)
