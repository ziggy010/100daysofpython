
# try:    
#     age = int(input("Enter your age: "))

# except:
#     print("Please enter your age in number. ")
#     age = int(input("Enter your age: "))

# if age > 18:
#     print(f"You can drive at age {age}");



def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print([number])

fizz_buzz(15)