s=["brown","brain","bring"]
w=s[0]
for word in s[1:]:
    i=0
    j=0
    while i<len(w)and j<len(word) and w[i]==word[j]:
        i+=1
        j+=1
    w=w[:j]
    if w=="": 
        break
print([w])