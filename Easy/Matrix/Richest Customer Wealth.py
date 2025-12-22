# https://leetcode.com/problems/richest-customer-wealth/description/?envType=problem-list-v2&envId=matrix
accounts = [[1,5],[7,3],[3,5]]
mx=0
# for  i in range(len(accounts)):
#     totalmx=sum(accounts[i])
#     mx=max(mx,totalmx)
# print(mx)
print( max(sum(mx) for mx in accounts) )
