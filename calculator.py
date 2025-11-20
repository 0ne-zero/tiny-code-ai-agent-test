def add(x, y):
    """Adds two numbers and returns the sum.
    Args:
        x (float): The first number.
        y (float): The second number.
    Returns:
        float: The sum of x and y.
    """
    return x + y
def subtract(x, y):
    """Subtracts two numbers and returns the difference.
    Args:
        x (float): The first number.
        y (float): The second number.
    Returns:
        float: The difference of x and y.
    """
    return x - y
def calculator():
    """Runs a simple calculator program allowing addition and subtraction.
    The user can perform multiple calculations until they choose to exit.
    """
    print("Select operation:")
    print("2. Subtract")

    while True:
        choice = input("Enter choice(1/2): ")

        if choice in ('1', '2'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                break
        else:
            print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    calculator()
