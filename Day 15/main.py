import art;
import functions;
import menu;

print(art.logo);


while functions.machine_status:
    user_coffee = input("\nWhat would you like (Espresso/Latte/Cappuccino): ")

    if functions.check_resource(user_coffee):
        functions.processCoins(user_drink=user_coffee);
        functions.reduce_resource(user_drink=user_coffee);







