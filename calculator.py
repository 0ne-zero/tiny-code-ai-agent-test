"""
A simple command-line calculator that can add and subtract two numbers.
"""

def add(x, y):
    """
    This function adds two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    This function subtracts the second number from the first.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The difference between x and y.
    """
    return x - y

if __name__ == "__main__":
    # Display menu to the user
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")

    while True:
        # Get user's choice
        choice = input("Enter choice(1/2): ")

        # Check if the choice is a valid option
        if choice in ('1', '2'):
            try:
                # Get numbers from user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # Handle non-numeric input
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                # Perform addition
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                # Perform subtraction
                print(num1, "-", num2, "=", subtract(num1, num2))
            
            # Ask if the user wants to do another calculation
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
              break # Exit the loop
        else:
            # Handle invalid choice
            print("Invalid Input")
