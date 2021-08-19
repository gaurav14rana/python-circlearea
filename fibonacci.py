fibNumbers = int(input("Enter the Number:"))
num1 = 0
num2 = 1
total = num1 + num2
print(num1)
while total < fibNumbers:
    print(total)
    total = num1 + num2
    num1 = num2
    num2 = total
