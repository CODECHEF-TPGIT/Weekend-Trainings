M=int(input())
books=list(map(int,input().split()))
n=int(input())
k=[]
for i in range(0,n):
    j=int(input())-1
    k.append(books.pop(j))
print(*k,sep="\n")
    
