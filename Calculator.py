print ("Calculator")

print ("1.Addition")
print ("2.Subtraction")
print ("3.Multiplication")
print ("4.Division")

sym = input("Choose one of them: ")

if sym == "1":
    num = eval(input("Enter a list of numbers: "))
    print (sum(num))

elif sym == "2":
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    print (num1-num2)

elif sym == "3":
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    print (num1*num2)

else:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    print (num1/num2)

