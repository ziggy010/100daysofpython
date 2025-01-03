import art;

print(art.logo);

first_number = int(input("\nWhat's the first number: "));

def calc(number1, given_operation, number2,):
    """takes 2 number as arguments and return the result according to the given operation"""
    if given_operation == "+":
        return number1 + number2;
    elif given_operation == "-":
        return number1 - number2;
    elif given_operation == "*":
        return number1 * number2;
    elif given_operation == "/":
        return number1 / number2;


repeat_calculation = True;

while repeat_calculation:
    operation = input("\n+\n-\n*\n/\nPick and operation: ");
    second_number = int(input("\nWhat's the next number?: "));

    result = calc(first_number, operation, second_number);
    print(f"{first_number} {operation} {second_number} = {result}");

    to_repeat = input(f"\nType 'y' to continue with {result}, or type 'n' to start a new calculation: ")

    if to_repeat == 'y':
        first_number = result;
    else:
        repeat_calculation = False;












