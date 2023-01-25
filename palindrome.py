def ispalindrome(s):
    return s==s[::-1]
s=input("enter the value")
ans=ispalindrome(s)
if ans:
    print(" It is Palindrome")
else:
    print("It is not a palindrome")
