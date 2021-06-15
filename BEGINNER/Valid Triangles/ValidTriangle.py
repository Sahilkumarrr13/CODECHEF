n=int(input())
for i in range(n):
	A,B,C= map(int,input().split())
	if A+B+C==180:
		print("YES")
	else:
		print("NO")
