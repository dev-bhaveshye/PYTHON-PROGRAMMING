import random


user = str(input("enter your move :"))


    


print("the computer move is : ", end="")
computer = (random.choice(["snake", "water" ,"gun"]))
print(computer)

if  (user == "snake" and computer == "snake" ):
    print("tie! ")
elif  (user == "water" and computer == "snake" ):
    print(" computer wins! ")
elif  (user == "gun" and computer == "snake" ):
    print(" user wins! ")
elif  (user == "snake" and computer == "gun" ):
    print("computer wins! ")
elif  (user == "water" and computer == "gun" ):
    print(" computer wins! ")
elif  (user == "gun" and computer == "gun" ):
    print("tie! ")
elif  (user == "snake" and computer == "water" ):
    print(" user wins! ")
elif  (user == "water" and computer == "water" ):
    print(" tie! ")
elif  (user == "gun" and computer == "water" ):
    print("computer! ")
else:
    print("wrong move , check your move !")
    
      




