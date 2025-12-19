# https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/description/
nums = [1,1]
k = 2
# nums_for_max=nums.copy()
# nums_for_min=nums.copy()

# max_ls=[];min_ls=[]
# for i in range(k):
#         x=max(nums_for_max)
#         max_ls.append(x)
#         nums_for_max.remove(x)
# for i in range(k):
#         x=min(nums_for_min)
#         min_ls.append(x)
#         nums_for_min.remove(x)
# print(abs(sum(max_ls)-sum(min_ls)))

# Second and More Optimized Solutions
nums.sort
print(abs(sum(nums[-k:]) - sum(nums[:k])))
