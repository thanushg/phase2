n,m=map(int,input().split())
matrix=[]
for i in range(n):
    row =[]*n
    matrix.append(row)

print(matrix)
for i in range(m):
    u,v =map(int,input().split())
    martix[u][v]=1
    matrix[u][v]=1

print(matrix)
    
