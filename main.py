# Import Data
from data import MENU, resources


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
def select_drink():
    drink = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    # the machine. Your code should end execution when this happens

    if drink == "off":
        quit()

    # TODO: 3. Print report.”
    # a. When the user enters “report” to the prompt, a report should be generated that shows
    # the current resource values. e.g.
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5

    if drink == "report":
        report()

    else:
        check_resources_needed(drink)

    return drink


def report():

    print("here")
    # return resources_status

    # return f"Water: {water_in_machine} \nMilk: {milk_in_machine} \nCoffee: {coffee_in_machine} \nMoney: {money_in_machine} "


# TODO: 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

def check_resources_needed(drink):
    water_needed = MENU[drink]["ingredients"]["water"]
    milk_needed = MENU[drink]["ingredients"]["milk"]
    coffee_needed = MENU[drink]["ingredients"]["coffee"]
    cost = MENU[drink]["cost"]

    water_in_machine = resources["water"]
    milk_in_machine = resources["milk"]
    coffee_in_machine = resources["coffee"]
    money_in_machine = resources["money"]

    if water_needed > water_in_machine:
        print(f"Sorry there is not enough water.")
    elif milk_needed > milk_in_machine:
        print(f"Sorry there is not enough milk.")
    elif coffee_needed > coffee_in_machine:
        print(f"Sorry there is not enough coffee.")
    else:
        # TODO: 5. Process coins.
        # a. If there are sufficient resources to make the drink selected, then the program should
        # prompt the user to insert coins.
        # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
        # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        paid = (quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01)

        # TODO: 7. Check transaction successful?
        # a. Check that the user has inserted enough money to purchase the drink they selected.
        # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
        # program should say “Sorry that's not enough money. Money refunded.”.
        # b. But if the user has inserted enough money, then the cost of the drink gets added to the
        # machine as the profit and this will be reflected the next time “report” is triggered. E.g.
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
        # c. If the user has inserted too much money, the machine should offer change.
        if paid < cost:
            print(f"Sorry that's not enough money. Money refunded.")
        else:
            money_in_machine += cost
            print(money_in_machine)


select_drink()




# TODO: 8. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.


