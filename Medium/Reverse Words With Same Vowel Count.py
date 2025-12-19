# https://leetcode.com/problems/reverse-words-with-same-vowel-count/description/

s = "cat and mice"
v=[ 'a', 'e', 'i', 'o','u']
words=s.split()
base_count=sum(1 for ch in words[0] if ch in v )

for i in range(1,len(words)):
    count=sum(1 for ch in words[i] if ch in v)
    if count==base_count:
        words[i]=words[i][::-1]
print(words)

    
    
            
       