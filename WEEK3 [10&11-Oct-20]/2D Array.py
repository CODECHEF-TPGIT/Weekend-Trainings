values=[]
sum_of_T=[]
for i in range(6):
    rval=list(map(int,input().split()))
    values.append(rval)
for i in range(0,4):
    current_row=values[i]
    for j in range(0,4):
        temp=0
        nval=j+1 
        temp=values[i][j]+values[i][j+1]+values[i][j+2]+values[i+1][nval]+values[i+2][nval]
        sum_of_T.append(temp)
print(max(sum_of_T))
