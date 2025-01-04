import menu;

resources = menu.resources;
menu = menu.MENU;
machine_status = True;

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_resource(user_choice):
    water = resources['water'];
    milk = resources['milk'];
    coffee = resources['coffee']
    money = resources['money']

    if user_choice == 'espresso':
        if water > 50 and coffee > 18:
            return True;
        else:
            print("\nSorry there is not enough resource.")
            machine_status = False;
    
    elif user_choice == 'latte':
        if water > 200 and coffee > 24 and milk > 150:
            return True;
        else:
            print("\nSorry there is not enough resource.")
            machine_status = False;

    
    elif user_choice == 'cappuccino':
        if water > 250 and coffee > 24 and milk > 100:
            return True;
        else:
            print("\nsorry there in not enough resource.")
            machine_status = False;
    elif user_choice == 'report':
        report();
        
    else:
        print("\nNot in the menu!")

def processCoins(user_drink):
        print("\nPlease insert coins.")
        no_of_quarters = int(input("\nHow many quarters: ")) * 0.25
        no_of_dimes = int(input("\nHow many dimes: ")) * 0.1
        no_of_nickles = int(input("\nHow many nickles: ")) * 0.05
        no_of_pennies = int(input("\nHow many pennies: ")) * 0.01
        cost = menu[user_drink]['cost'];

        total = round(((no_of_quarters + no_of_dimes + no_of_nickles + no_of_pennies) - cost), 2);

        if total >= 0:
            print(f"\nHere is ${total} in change.\nHere is your {user_drink} ☕️ Enjoy!")
            print('''
            .___________. __    __       ___      .__   __.  __  ___    ____    ____  ______    __    __     .______        ___      .______   ____    ____ 
|           ||  |  |  |     /   \     |  \ |  | |  |/  /    \   \  /   / /  __  \  |  |  |  |    |   _  \      /   \     |   _  \  \   \  /   / 
`---|  |----`|  |__|  |    /  ^  \    |   \|  | |  '  /      \   \/   / |  |  |  | |  |  |  |    |  |_)  |    /  ^  \    |  |_)  |  \   \/   /  
    |  |     |   __   |   /  /_\  \   |  . `  | |    <        \_    _/  |  |  |  | |  |  |  |    |   _  <    /  /_\  \   |   _  <    \_    _/   
    |  |     |  |  |  |  /  _____  \  |  |\   | |  .  \         |  |    |  `--'  | |  `--'  |    |  |_)  |  /  _____  \  |  |_)  |     |  |     
    |__|     |__|  |__| /__/     \__\ |__| \__| |__|\__\        |__|     \______/   \______/     |______/  /__/     \__\ |______/      |__|     
                                                                                                                                                
            
            ''')

        else:
            print("\nSorry that's not enough money. Money refunded. ")
            machine_status = False;

def reduce_resource(user_drink):

    if user_drink == 'espresso':
        resources['water'] -= menu[user_drink]['ingredients']['water'];
        resources['coffee'] -= menu[user_drink]['ingredients']['coffee'];
        resources['money'] += menu[user_drink]['cost'];

    else:
        resources['water'] -= menu[user_drink]['ingredients']['water'];
        resources['coffee'] -= menu[user_drink]['ingredients']['coffee'];
        resources['money'] += menu[user_drink]['cost'];
        resources['milk'] -= menu[user_drink]['ingredients']['milk'];
