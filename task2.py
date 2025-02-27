def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = int(input("Enter choice (1/2/3/4): "))
            if choice in (1, 2, 3, 4):
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == 2:
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == 3:
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == 4:
        result = divide(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(f"{num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()