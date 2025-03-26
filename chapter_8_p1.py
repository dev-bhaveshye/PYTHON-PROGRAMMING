def greatest(a,b,c):
    if ( a>b and a>c):
       return a 
    elif(b>c and b>a):
        return b 
    elif(c>a and c>b):
        return c 


print(greatest(4,25,6))
