s=[2,0,2,1,1,3,0]

count_zero=0
count_one=0
count_two=0
for num in s:
    if num==0:
        count_zero+=1
    elif num==1:
        count_one+=1
    elif num==2:
        count_two+=1
print(([0]*count_zero+[1]*count_one+[2]*count_two))