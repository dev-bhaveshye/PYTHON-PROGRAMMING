n=int(input("enter a number"))

for i in range (2,n):

    if(n%i==0):
        print(f"{n}is a not prime number")
        break
else:
    print("number is prime")