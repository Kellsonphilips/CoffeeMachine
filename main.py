from item import MENU, resources

profit_all = 0


# TODO: 4 Check if coffee machine still have enough resources
def is_ingredient_sufficient(order_ingredient):
    """Return True if there is enough resources to serve a user or False if there is not enough resources"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 5 Process coin
def coin_processing():
    """ Return total amount imputed by user"""
    print("Please, insert coins.")
    quarter = int(input("How many quarters?: "))
    quarters = quarter * 0.25
    dime = int(input("How many dimes?: "))
    dimes = dime * 0.10
    nickle = int(input("How many nickles?: "))
    nickles = nickle * 0.05
    pennie = int(input("How many pennies?: "))
    pennies = pennie * 0.01
    total = quarters + dimes + nickles + pennies
    return total


# TODO: 6 Check if transactions is successful
def processing_transaction(money_received, drink_cost):
    """Return False if money is insufficient or True if payment is accepted"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit_all
        profit_all += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 7 Make coffee
def make_coffee(drink_name, order_ingredients):
    """How to deduct the required ingredients from our resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️, enjoy your drink.")


machine_is_on = True

# TODO: 1 Ask users to chose the type of coffee they want
while machine_is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO : 2 Enable the coffee maintainers to be able to turn of the coffee machine with a prompt "off"
    if user_choice == "off":
        machine_is_on = False
    # TODO: 3 print reports for users selected options
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit_all}")
    else:
        drink = MENU[user_choice]
        if is_ingredient_sufficient(drink["ingredients"]):
            payment = coin_processing()
            processing_transaction(payment, drink["cost"])
            make_coffee(user_choice, drink["ingredients"])
