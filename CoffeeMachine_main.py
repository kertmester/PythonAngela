import CoffeeMachine_data as data
from CoffeeMachine_data import menu
from CoffeeMachine_data import resources
from CoffeeMachine_data import choice_dict
from CoffeeMachine_data import title
import time

VALID_COINS = ["Dollar","Half dollar","Quarter","Dime","Nickel","Penny"]

in_coins_ok = False

out_change = []
resources_left = resources.copy()
enough_resources = True
ready_to_make_coffee = False



def check_money(cost,paid,drink):
    """function for checking if coins inserted is enough for chosen beverage"""
    if cost <= paid:
        print(f"Thank you! {drink} coming up!\n")
        return True
    else:
        print("Not enough coins inserted!\n")
        return False

def calculate_change(cost,paid):
    """this function calculates the change"""
    rem = 0
    # calculateing the remainder:
    rem = paid-cost
    change = []

    #dollar
    coin = int(rem/1)
    rem = (rem%1)*100
    change.append(coin)

    #half_dollar
    coin = int(rem/50)
    rem = rem%50
    change.append(coin)

    #quarter
    coin = int(rem/25)
    rem = rem%25
    change.append(coin)

    #dime
    coin = int(rem/10)
    rem = rem%10
    change.append(coin)

    #nickel
    coin = int(rem/5)
    rem = rem%5
    change.append(coin)

    #penny
    coin = int(rem/1)
    rem = rem%1
    change.append(coin)
    return change

    # Penny: One - cent coin.
    # Nickel: Five - cent coin.
    # Dime: Ten - cent coin.
    # Quarter: Twenty - five - cent coin.
    # Half - dollar: Fifty - cent coin, no longer minted for circulation but still legal tender.
    # Dollar coin: One - dollar coin, no minted for circulation but still legal tender.

def check_resources(resources_to_check, menu_to_check, drink_to_check):
    """prints if resources are enough for chosen beverage"""
    nr_of_insufficient_resources = 0
    for res_key in resources_to_check:
        if res_key in menu_to_check[drink_to_check]["ingredients"]:
            if resources_to_check[res_key] < menu_to_check[drink_to_check]["ingredients"][res_key]:
                print(f"Not enough {res_key}")
                nr_of_insufficient_resources += 1
    if nr_of_insufficient_resources > 0:
        return False
    return True


print("\n"*10)

# TODO: this has to be changed !!!!!!
#while program_finished = True:

while True:
    print(title)
    print('\N{Hot Beverage}'*5)
    drink_not_chosen = True
    while drink_not_chosen:
        want_to_insert_coins = True
        # ask what customer would like to drink
        in_drink_letter = input("What would you like to drink? \n(e)spresso\n(l)atte\n(c)appuccino\n\n(r)esources\n(f)ill up resources\n").lower()
        if in_drink_letter == 'r':
            print("These are my rosources:")
            print(resources_left)
        elif in_drink_letter == 'f':
            resources_left = resources
            print("These are my rosources:")
            print(resources_left)

        else:
            drink_not_chosen = False
        # get drink name
    choice_drink_name = choice_dict[in_drink_letter]

    # get price of drink
    out_price = menu[choice_drink_name]["cost"]

    print(f"Aaah, lovely! A fine {choice_drink_name}. Great choice!")

    # get ingredients required
    current_ingredients = data.menu[choice_drink_name]["ingredients"]

    # check if resources is sufficient for ingredients

    enough_resources = check_resources(resources_left,data.menu,choice_drink_name)

    if enough_resources:

        while want_to_insert_coins:
            in_coins = float(input(f"\n Please insert {out_price} $\n$"))
            in_coins_ok = check_money(out_price, in_coins, choice_drink_name)

            if in_coins_ok:
                print("Here is your change:\n")
                out_change = calculate_change(out_price, in_coins)
                # give change
                for i in range(1, len(out_change) + 1):
                    print(f"{VALID_COINS[i - 1]}: {out_change[i - 1]}")
                # change resources
                for res_key in resources_left:
                    resources_left[res_key] -= current_ingredients[res_key]
                want_to_insert_coins = False
                print("Preparing coffee",end=" ")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)

                print(f"Enjoy your {choice_drink_name}!!!\n")
            else:
                wtic = input("Do you want to choose another beverage? y/n ").lower()
                if wtic == 'y':
                    want_to_insert_coins = False














