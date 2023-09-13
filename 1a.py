# Write a python program to find the best of two test average marks out of three test's marks accepted from the user

num1 = float(input("Enter 1st test marks: "))
num2 = float(input("Enter 2nd test marks: "))
num3 = float(input("Enter 3rd test marks: ")) 

if(num1 >= num2) and (num1 >= num3):
    if(num2 >= num3):
        print("The best of two test marks are", num1, num2)
        print("The average marks is", (num1 + num2)/2)
    else:
        print("The best of two test marks are", num1, num3)
        print("The average marks is", (num1 + num3)/2)
        
elif(num2 >= num1) and (num2 >= num3):
    if(num2 >= num1):
        print("The best of two test marks are", num2, num1)
        print("The average marks is", (num2 + num1)/2)
    else:
        print("The best of two test marks are", num2, num3)
        print("The average marks is", (num2 + num3)/2)
        
else:
    if(num1 >= num2):
        print("The best of two test marks are", num3, num1)
        print("The average marks is", (num3 + num1)/2)
    else:
        print("The best of two test marks are", num3, num2)
        print("The average marks is", (num3 + num2)/2)
