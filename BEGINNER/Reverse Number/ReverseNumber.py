n=int(input())
for i in range(n):
	k=int(input())
	rev_num=0
	while k>0:
		remainder=k%10
		rev_num=rev_num*10 + remainder
		k=k //10
	print(rev_num)
