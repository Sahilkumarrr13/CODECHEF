T=int(input())
for i in range(T):
    xa,xb,Xa,Xb=map(int,input().split())
    k=Xa//xa
    l=Xb//xb
    print(k+l)
