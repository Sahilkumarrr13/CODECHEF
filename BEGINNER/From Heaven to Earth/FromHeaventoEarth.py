t=int(input())
while(t):
    n,v1,v2=map(int,input().split())
    if(2**0.5)/v1<2/v2:
        print("Stairs")
    else:
        print("Elevator")
    t=t-1
