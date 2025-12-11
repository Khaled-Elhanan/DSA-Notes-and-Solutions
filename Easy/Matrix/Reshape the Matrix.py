# https://leetcode.com/problems/reshape-the-matrix/description/?envType=problem-list-v2&envId=array
mat = [[1,2],[3,4]]
r = 1
c = 4

flat_matrix = [x for row in mat for x in row]
if len(flat_matrix)!=c*r:
    print(mat)
print([flat_matrix[c*i:(i+1)*c] for i in range(r)])