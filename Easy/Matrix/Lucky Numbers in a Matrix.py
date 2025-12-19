# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/?envType=problem-list-v2&envId=matrix
matrix = [[3,7,8],[9,11,13],[15,16,17]]
min_in_rows = [min(row) for row in matrix]
max_in_cols = [max(col) for col in zip(*matrix)]
print(list(set(min_in_rows) & set(max_in_cols)))
