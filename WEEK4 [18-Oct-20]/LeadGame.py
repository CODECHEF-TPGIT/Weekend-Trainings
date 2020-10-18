W=1
lead=0
p1=0
p2=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    diff=0
    p1+=a
    p2+=b
    if p1>p2:
        diff=p1-p2
    else:
        diff=p2-p1
    if diff>lead:
        lead=diff
        if p1>p2:
            W=1 
        else:
            W=2
print(W, lead)
