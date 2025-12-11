# https://leetcode.com/problems/baseball-game/description/?envType=problem-list-v2&envId=array
ops=["5","2","C","D","+"]
stack=[]
for i in ops:
    if i not in "CD+":
        stack.append(int(i))
    else:
        if i=="C":
            stack.pop()
        elif i=="+":
            x=stack[-2]+stack[-1]
            
            stack.append(x)
        elif i=="D":
            y=2*stack[-1]
            
            stack.append(y)
print(sum(stack))



