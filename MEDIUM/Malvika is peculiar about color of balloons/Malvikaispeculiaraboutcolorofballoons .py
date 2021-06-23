n=int(input())
for i in range(n):
  j=input()
  a=j.count("a")
  b=j.count("b")
  if a==0 or b==0:
    print(0)
  elif a>b:
    print(b)
  else:
    print(a)
