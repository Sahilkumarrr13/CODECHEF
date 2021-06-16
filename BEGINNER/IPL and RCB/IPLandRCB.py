T=int(input())
for i in range(T):
    x,y=map(int,input().split())
    if x<=1 or x<=y:
        print("0")
    else:
        print(x-y)  
