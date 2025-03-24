a=int(input("enter value :-"))
b=int(input("enter value :-"))
c=int(input("enter value :-"))
d=int(input("enter value :-"))

if(a>b and a>c and a>d):
    print(a,"is greater than ", b , c ,d)

if(b>a and b>c and b>d):
    print(b,"is greater than ", a , c ,d)
if(c>a and c>b and c>d):
    print(c,"is greater than ", a , b ,d)
if(d>a and d>c and d>b):
    print(d,"is greater than ", a , b ,c)

else:
    print(" invalid ")