import menu;

resources = menu.resources;

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
            print('okay')
        else:
            print("\nSorry there is not enough water.")
    
    elif user_choice == 'latte':
        if water > 200 and coffee > 24 and milk > 150:
            print("okay")
        else:
            print("\nSorry there is not enough water.")