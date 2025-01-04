from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu();
coffee_maker = CoffeeMaker();
money_machine = MoneyMachine();

machine_status = True;

while machine_status:

    user_choice = input(f"What would you like ({menu.get_items()}): ")

    if user_choice == "off":
        machine_status = False;
    elif user_choice == "report":
        coffee_maker.report();
        money_machine.report();
    else:
        user_drink_details = menu.find_drink(user_choice);

        is_resource_available = coffee_maker.is_resource_sufficient(user_drink_details);

        if is_resource_available:
            txn_successful = money_machine.make_payment(user_drink_details.cost);
            if txn_successful:
                coffee_maker.make_coffee(user_drink_details);
            else:
                machine_status= False;
        else:
            machine_status = False;
    