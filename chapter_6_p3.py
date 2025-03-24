a= "make a lot of money "
b= "click this "
c= "buy now"
d= "subscribe this "

name = " kaisa he bhai  "
'''if name.find(" make a lot of money " ) != -1 :
    print(" spam message ")

else:
    print ( " not spam ")'''

if ( (a in name ) or ( b in name) or ( c in name) or ( d in name )):
    print ( " spam message ")

else: 
    print(" not spam ")
