# https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=stack

s = "()[]{}"
stack=[]
map={')':'(', '}':'{', ']':'['}
res=True
if len(s)==1:
    res=False
for char in s:
    if char in map.values():
        stack.append(char)
    else:
        if not stack or stack.pop()!=map[char]:
            res=False
if stack:
    res=False
print(res)
    


