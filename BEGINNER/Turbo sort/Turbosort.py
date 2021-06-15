n=int(input())
li=[]
for i in range(n):
	j=int(input())
	li.append(j)
li.sort()
i=0
while i<len(li):
	print(li[i])
	i+=1
