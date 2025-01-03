import art;

print(art.logo);

def add(n1, n2):
    return n1 + n2;

def substract(n1,n2):
    return n1 - n2;

def multiply(n1, n2):
    return n1 * n2;

def divide (n1, n2):
    return n1 / n2;

calc_dict = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}

calculation = True;

while calculation:
    first_number = int(input("\nWhat's the first number?: "))

    same_calculation = True;

    while same_calculation:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        second_number = int(input("\nWhat's the next number?: "))
        result = calc_dict[operation](first_number, second_number);
        print(f"{first_number} {operation} {second_number} = {result}");

        user_choice = input(f"\nType 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")

        if user_choice == 'y':
            first_number = result;
        else:
            same_calculation = False;