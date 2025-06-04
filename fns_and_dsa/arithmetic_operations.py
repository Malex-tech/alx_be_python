# arithmetic_operations.py

def perform_operation(num1: float, num2: float, perform_operation: str):
    """
    Performs a basic arithmetic operation on two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        perform_operation (str): The operation to perform.
                                 Accepts 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float or str: The result of the arithmetic operation,
                      or an error message for invalid input or divide-by-zero.
    """
    perform_operation = perform_operation.strip().lower()

    if perform_operation == 'add':
        return num1 + num2
    elif perform_operation == 'subtract':
        return num1 - num2
    elif perform_operation == 'multiply':
        return num1 * num2
    elif perform_operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is undefined."
        return num1 / num2
    else:
        return "Error: Invalid operation. Choose from add, subtract, multiply, or divide."