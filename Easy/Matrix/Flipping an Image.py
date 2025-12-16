image = image = [[1,1,0],[1,0,1],[0,0,0]]

# flat=[1 if x==0 else 0 for row in image for x in row]
# x=[flat[i:i+len(image[0])][::-1] for i in range(0,len(flat), len(image[0]))]
# print(x)


#  Second Solution using bitwise XOR 
# ~i --> mean   -(i+1) =-1 , -2 , -3 , ... 

for row in image:
    for i in range(0,len(row)+1//2):
        row[i],row[~i]=row[~i]^1 , row[i]^1
print(image)