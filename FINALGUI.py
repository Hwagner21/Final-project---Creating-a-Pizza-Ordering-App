
menu = {'Cheese': 15.00, 'Peperoni': 16.00, 'Sausage': 17.00, 'Chicken': 18.00}
def get_order():
    currentOrder = []
    while True:
        print("What woud you like today?")
        order = input()
        if order in menu:
            currentOrder.append(order)
        else:
            print("That is unavailable.")
        if is_order_complete(): return currentOrder
def is_order_complete():
    print("Would you like anything else?")
    choice = input()
    if choice == "no": return True
    elif choice == "yes": return False
    else:
        raise Exception("Invalid input")
def output_order(orderList):
    print("Your order is:")
    for order in orderList:
        print(order)
def main():
    order = get_order()
    output_order(order)
    print("Enjoy!")

if __name__=="__main__": main()