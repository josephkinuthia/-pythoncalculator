# 1. addition
# 2. subtraction
# 3. multiplication
# 4. division

print("select an operation to perform")

print("#1.addition")
print("#2.subtraction")
print("#3.multiplication")
print("#4.division")

operation = input ("enter operator")

if operation == "+" :
   num1 = float(input("enter first number :"))
   num2 = float(input("enter second number :"))

elif operation == "-" :
    num1 =float(input("enter first number :"))

    num2 =float( input("enter first number :"))
    print("the sum is +str(int( num1) - int(num2)")
elif operation == "*" :
    num1 =float( input("enter first number :"))
    num2 =float(input("enter first number :"))
    print("the sum is +src(int(num1) * int(num2)")
elif operation == "/" :
    num1 =float( input("enter first number :"))
    num2 =float( input("enter first number :"))
    print("the sum is  + src(int(num1)/ int(num2)"))

else:
    print("invalid entry")















