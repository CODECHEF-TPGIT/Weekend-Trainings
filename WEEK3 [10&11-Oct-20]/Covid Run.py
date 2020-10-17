for _ in range(int(input())):
    N,K,X,Y=map(int,input().split())
    pattern=[]
    next_city=X
    pattern.append(next_city)
    while 1:
        next_city = (next_city+K)%N
        if next_city == X:
            break
        else:
            pattern.append(next_city)
    if Y in pattern:
        print("YES")
    else:
        print("NO")
