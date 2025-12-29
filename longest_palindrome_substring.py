s="madam"
def palindrome(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
def palindrome_substring(input):
    ans=""
    for i in range(len(input)):
        res=""
        for j in range(i,len(input)):
            res+=input[j]
            if palindrome(res):
                if len(res)>len(ans):
                    ans=res
    return ans
print(palindrome_substring("bababd"))

