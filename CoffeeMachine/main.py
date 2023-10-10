MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 400,
    "milk": 200,
    "coffee": 100,
}

def check_resource(coffee_type):
    """return True if resources is enough, or False if insufficient."""
    materials = list(MENU[coffee_type]["ingredients"].keys())
    for ingredient in materials:
        if resources[ingredient] < MENU[coffee_type]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True
    
def count_money(quarter, dime, nickle, penny):
    """return total money amount paid from a user."""
    money = 0.25 * quarter + 0.1 * dime + 0.05 * nickle + 0.01 * penny
    return money

def resource_report():
    """print current resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def resource_update(coffee_type, money):
    """update resources after a transaction."""
    for item in list(MENU[coffee_type]["ingredients"].keys()):
        resources[item] -= MENU[coffee_type]["ingredients"][item]
    resources["money"] += MENU[coffee_type]["cost"]
    return resources

def coffee_machine():
    """A virtual coffee machine program."""
    resources["money"] = 0
    continue_service = True
    
    while continue_service:
        user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
        if user_input == "report":
            resource_report()
        elif user_input == "off":
            return
        elif user_input in list(MENU.keys()):
            if check_resource(user_input):
                print("Please insert coins.")
        
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                money = count_money(quarters, dimes, nickles, pennies)
                
                change = money - MENU[user_input]["cost"]
                if change < 0:
                    continue_service = False
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    resource_update(user_input, money)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {user_input}. Enjoy!☕")
            else:
                return

    coffee_machine()

if __name__ == "__main__":
    coffee_machine()        
