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

def divide(x, y):
    """Divides two numbers and returns the quotient.
    Args:
        x (float): The numerator.
        y (float): The denominator.
    Returns:
        float: The quotient of x and y.
    Raises:
        ValueError: If the denominator is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    """Runs a simple calculator program allowing addition, subtraction, and division.
    The user can perform multiple calculations until they choose to exit.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")

    while True:
        choice = input("Enter choice(1/2/3): ")

        if choice in ('1', '2', '3'):
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
            elif choice == '3':
                try:
                    print(num1, "/", num2, "=\n", divide(num1, num2))
                except ValueError as e:
                    print(e)
            
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    calculator()