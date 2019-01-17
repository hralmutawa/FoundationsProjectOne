####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Frosting Sprinkles"
signature_flavors = ["red velvet", "bubble gum", "birthday cake"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    for key,value in menu.items():
        print("Item: %s \t Price: %.3f KWD" %(key, value))
    


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for cupcake in original_flavors:
        print(cupcake)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for signature_flavor in signature_flavors:
        print(signature_flavor)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in signature_flavors:
        return True
    elif order in original_flavors:
        return True
    elif order in menu:
        return True
    else: 
        return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    user_input = input("What is your order? or type 'exit' to checkout \n")

    while user_input.lower() != "exit": 
        if is_valid_order(user_input) == True:
            order_list.append(user_input)
            print("[%s] has been added to the cart" % user_input)
            user_input = input("What else? or type 'exit' to checkout \n")
        else:
            print("You blind? this isn't on the menu!")
            user_input = input("Please enter a valid flavor. or type 'exit' to checkout \n")
    

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        print("We can put that on a credit card")
    else:
        print("Cash only")


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for order in order_list:
        if order in signature_flavors:
            total = total + signature_price
        elif order in original_flavors:
            total += original_price
        else:
            total += menu[order]

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for order in order_list:
        print(order)
    x = get_total_price(order_list)
    print("%0.3f KWD" % x)
