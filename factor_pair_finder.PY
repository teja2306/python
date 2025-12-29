s=40
import math
for i in range(1,int(math.sqrt(s))+1):
    if s%i==0:
        print(i)
        print(s//i)