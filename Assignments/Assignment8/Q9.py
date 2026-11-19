def palindromme(d):
    original=d
    rev=0
    
    while(d>0):
        num=d%10
        rev=rev*10+num
        d=d//10
    if(rev==original):
        print("Palindrome")
    else:
        print("Not palindrome")
    
d=121
palindromme(d)

