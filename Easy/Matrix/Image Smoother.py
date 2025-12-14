# https://leetcode.com/problems/image-smoother/description/?envType=problem-list-v2&envId=matrix
img = [[1,1,1],[1,0,1],[1,1,1]]

rows , cols = len(img) ,len(img[0])
res= [[0]*cols for _ in range(rows)]
for r in range(rows) :
    for c in range(cols):
        total=0
        cnt=0
        for i in range(r-1 , r+2):
            for j in range(c-1 , c+2):
                if(i<0 or i ==rows or j<0 or j==cols):
                    continue
                total+=img[i][j]%256  # %256 to take only the old_value to use it with neighbours 
                cnt+=1
        img[r][c]=img[r][c]^(total//cnt)<<8 # old_value XOR new_value
for  r in range(rows): # for return only the new value from the number --> number now contain [new_value][old_value] 
        for c in range(cols):
            img[r][c]=img[r][c] >>8
print(img)

# Another Soultion wihtout bitwise 

# rows , cols = len(img) ,len(img[0])
# res= [[0]*cols for _ in range(rows)]
# for r in range(rows) :
#     for c in range(cols):
#         total=0
#         cnt=0
#         for i in range(r-1 , r+2):
#             for j in range(c-1 , c+2):
#                 if(i<0 or i ==rows or j<0 or j==cols):
#                     continue
#                 total+=img[i][j]
#                 cnt+=1
#         res[r][c]=total//cnt

# print(res)




