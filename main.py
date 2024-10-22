def add(x, y):
  return x + y

def multiply(x, y):
  return x * y

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = add(num1, num2)
product = multiply(num1, num2)

print("Sum:", sum)
print("Product:", product)