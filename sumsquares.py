l=[1,11,10,2]
def sumsquare(l):
    odd=0
    even=0
    for i in l:
        if i%2==0:
            even+=i**2
        else:
            odd+=i**2
    l=[odd,even]
    return(l)
print(sumsquare(l))
