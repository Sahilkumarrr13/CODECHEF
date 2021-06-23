n=int(input())
for i in range(n):
  j=input()
  if len(j)%2==0:
    s1=list(j[:int(len(j)/2)])
    s2=list(j[int(len(j)/2):])
    s1.sort();s2.sort()
    if s1==s2:
      print("YES")
    else:
      print("NO")
  else:
    s1=list(j[:int(len(j)/2)])
    s2=list(j[int(len(j)/2+1):])
    s1.sort();s2.sort()
    if s1==s2:
      print("YES")
    else:
      print("NO")
