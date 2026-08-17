# 17.	Create two 3 × 3 matrices using nested lists and perform matrix addition.

m1=[
    [2,3,4],
    [4,6,8],
    [7,8,3]
]
m2=[
    [4,2,7],
    [3,5,7],
    [1,4,8]
]

    
print("Addition is :")
result=[]
for i in range(3):
    row=[]
    for j  in range(3):
        row.append(m1[i][j]+m2[i][j])
    result.append(row)
    
for row in result:
    print(row)               