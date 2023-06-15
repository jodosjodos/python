num1=int(input("enter first number : "))
num2=int(input("enter the second number :"))
operator =input("enter operation u want to do : ")

result=0;
name=""
if operator == "+" :
 result=num1+num2
 name="sum"
#  print("additon")

elif operator == "-" :
 result=num1 - num2
 name="difference"
#  print("substraction")


elif operator == "*" :
 name="product "
 result=num1 * num2
#  print("mutliplication")


elif operator == "/" :
 name="quotient"
 result=num1 / num2
#  print("division")

elif operator == "%" :
 name="remainder"
 num1 % num2
#  print("find remainder") 

else :
  print("enter valid operator")

print("the  " + str(name)  + " between "+ str(num1) + " and "  + str(num2) +" is " + str(result))