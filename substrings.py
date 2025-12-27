def substring(s,ans):
    #base case
    if len(s)==0:
        print((ans))
        return
    #include
    substring(s[1:],ans+s[0])
    #exclude
    substring(s[1:],ans)
substring("abc","")