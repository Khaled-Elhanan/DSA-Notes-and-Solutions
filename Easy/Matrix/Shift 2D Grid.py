# https://leetcode.com/problems/shift-2d-grid/description/?envType=problem-list-v2&envId=matrix


# grid = [[1,2,3],[4,5,6],[7,8,9]]
# k=1
# Output: [[9,1,2],[3,4,5],[6,7,8]]


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4


# flat=[x for row in grid for x in row]
# k = k % len(flat) 
# if k>=len(flat):
#     print(flat)
    
# else:
#     a=len(flat)
#     for i in range(k):
#         flat.insert(i,flat[-k+i])
#     res=[]    
#     for i in range(a):
#         res.append(flat[i])
#     res=[res[i:i+len(grid[0])] for i in range(0,len(res),len(grid[0]))]
#     print(res)

# Second and More Optimized Solutions


flat=[x for row in grid for x in row]
k=k%len(flat)
if k==0:
    print(grid)
else:
    flat=flat[-k:] + flat[:-k]
    res = [flat[i:i+len(grid[0])] for i in range(0, len(flat), len(grid[0]))]
    print(res)

