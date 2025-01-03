import art;
import functions;
import menu;

# print(art.logo);

machine

user_coffee = input("\nWhat would you like (Espresso/Latte/Cappuccino): ")

resource = menu.resources;

functions.check_resource(user_coffee);


if user_coffee == 'report':
    functions.report();






