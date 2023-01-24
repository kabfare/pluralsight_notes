menu=['Knackered Spam', 'Pip pip Spam', 'Squidgy Spam', 'Smashing Spam']
menu_prices={'Knackered Spam': 0.5, 'Pip pip Spam': 1.5, 'Squidgy Spam': 2.5, 'Smashing Spam': 3.5}

orders=[]


while (True):
    order=input('What would you like to order? (Q to Quit)\n')
    if order == 'Cheeky Spam':
        print("Sorry, we're all out of that!")
        continue #pops program back up to start of loop
    if order.upper()=='Q':
        break
    #Find the order and add it to the list if it exists
    found=menu_prices.get(order)
    if found:
        orders.append(order)
    else:
        print("Menu item doesn't exist\n")
    order=input('Anything else? (Q to Quit)\n')
print(orders)