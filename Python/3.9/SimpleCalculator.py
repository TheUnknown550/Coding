#input viaribles
num1 = float(input("Please enter a number: "))
num2 = float(input("Please enter another number: "))

#input process viarible
print("1: Addition\n2:Subtraction\n3:Multiplication\n4:Division")
Cal = int(input("What do you want to do with these number"))

#Calculator Process
if Cal == 1:
    print("your answer is: ",num1+num2)
elif Cal == 2: 
    print("your answer is: ",num1-num2)
elif Cal == 3: 
    print("your answer is: ",num1*num2)
elif Cal == 4: 
    print("your answer is: ",num1/num2)
#user gave an unused syntax
else:
    print("Not a described number")