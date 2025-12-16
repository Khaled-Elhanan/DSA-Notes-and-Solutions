matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
res = all(matrix[i - 1][:-1] == matrix[i][1:] for i in range(1, len(matrix)))
print(res)


