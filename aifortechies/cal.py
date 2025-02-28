def add (a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide (a,b):
    if b ==0:
        return "error! Division by zero."
    return a/b
def calculator():
    print("select operation:")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input ("Enter choice (1/2/3/4):")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()


