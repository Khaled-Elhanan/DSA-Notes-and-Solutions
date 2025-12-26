#https://leetcode.com/problems/minimum-penalty-for-a-shop/description/?envType=daily-question&envId=2025-12-26
customers = "YYNY"
mx=0
score= 0
hour=-1
for i , k in enumerate(customers):
    score+=1 if k=="Y" else -1
    if score>mx :
        mx, hour= score , i
print(mx+1)