n = int(input("enter a number: "))
factorial = 1
for i in range(n,0,-1):
    factorial *= i
print("Factorial: ", factorial)
