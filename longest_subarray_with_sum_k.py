s=[2,5,6,4,1,2,1,1,1]
k=6
res=[]
for i in range(len(s)):
    temp=[]
    for j in range(i,len(s)):
        temp.append(s[j])
        if sum(temp)==k:
            if len(temp)>len(res):
                res=temp[:]
print(res)