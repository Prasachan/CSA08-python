def isIsomorphic(a,b):
    if(len(a) !=len(b)):
        return false
    x=[a.count(char1)for char1 in a]
    y=[b.count(char1)for char1 in b]
    return x==y
IP1=input("input 1")
IP2=input("input 2")
print(isIsomorphic(IP1,IP2))
