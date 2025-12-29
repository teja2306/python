s=[3,5,6,1,10,7]
target=70
def binary_search(s,target):
    low=0
    high=len(s)-1
    while low<=high:
        mid=(low+high)//2
        if s[mid]==target:
            return "found"
        elif s[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return "not found"
print( binary_search(s,target))