for _ in range(int(input())):
    R,S=map(int,input().split())
    while 1:
        if R==S:
            print(R+S)
            break
        elif R>S:
            R-=S
            continue
        elif S>R:
            S-=R
            continue
