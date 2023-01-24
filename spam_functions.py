menu={'Knackered Spam': 0.5, 'Pip pip Spam': 1.5, 'Squidgy Spam': 2.5, 'Smashing Spam': 3.5}

def print_menu(menu):
    for name, price in menu.items():
        print(name, ': $', format(price, '.2f'), sep='')

def get_order(menu):
    orders=[]
    order=input('What would you like to order? (Q to Quit)\n')

    while (order.upper() != 'Q'):
        #find the order#
        found=menu.get(order)
        if found:
            orders.append(order)
        else:
            print("Menu item doesn't exist\n")
        
        order=input('Anything else? (Q to Quit)\n')
    return orders

def bill_total(orders, menu):
    total=0

    for order in orders:
        total+=menu[order]
    
    return total

def main():
    menu={'Knackered Spam': 0.5, 'Pip pip Spam': 1.5, 'Squidgy Spam': 2.5, 'Smashing Spam': 3.5}
    print_menu(menu)
    order=get_order(menu)
    total=bill_total(order, menu)
    print('You ordered:', order, ' and your total is $', format(total,'.2f'), sep='')

main()

