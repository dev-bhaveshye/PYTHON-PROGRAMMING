marks1= int(input("enter marks of subject 1"))
marks2= int(input("enter marks of subject 2"))
marks3= int(input("enter marks of subject 3"))
 
total_marks = 300

total_percentage =((marks1 + marks2 + marks3 )/ total_marks) *100 

print (total_percentage)
 
sub1_per=(marks1/100)*100
print("subject 1 pecentage:", sub1_per)

sub2_per=(marks2/100)*100
print("subject 2 pecentage:", sub2_per)

sub3_per=(marks3/100)*100
print("subject 3 pecentage:", sub3_per)

if (total_percentage>= 40 and sub1_per>=33 and sub2_per>=33 and sub3_per>=33):
    print("you are pass ")

else:
    print("yur are failed ")