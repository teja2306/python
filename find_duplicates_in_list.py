s=[1,4,2,5,8,4,8,2]
res=[]
freq={}
for num in s:
    freq[num]=freq.get(num,0)+1
for val in freq:
    if freq[val]>1:
        res.append(val)
# for num in s:
#     if s.count(num)>1:
#         if num not in res:
#             res.append(num)
print(res)