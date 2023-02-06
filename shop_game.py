#hello welcome, what's your name?
#how can I help you?
#list of items to buy
#how much money name has
#run through order
#purchase and view remaining money
#if not enough, state not enough money
#thank you come again

inventory=['(1) Health Potion', '(2) Mana Potion', '(3) Elixir']
inv_price={}
price=20
player_g=90


for item in inventory:
    inv_price[item]=price #"dictionary (inv_price) value (item) is assigned to key (price)"
    price=price+15
##print(inv_price)

def menu():
    for name, price in inv_price.items():
        print(name, ': ', price, 'g', sep='')


print("Hello! Welcome to The Shop!\n")
player_name=input("What's your name?\n")
#print()

def get_order():
    orders=[]
    while (True):
        order=input("Okay, "+ player_name+", what can I help you with? (Q) to Quit\n")
        if order.upper()=='Q':
            break
        elif order=='1':
            order=input('What else can I get you? (Q) to quit\n')
            orders.append('(1) Health Potion')
            pass
        elif order=='2':
            order=input('What else can I get you? (Q) to quit\n')
            orders.append('(2) Mana Potion')
            pass
        elif order=='3':
            order=input('What else can I get you? (Q) to quit\n')
            orders.append('(3) Elixir')
            pass
        else:
            print("We don't carry that...\n")
    return orders

def bill_total(orders, inv_price):
    total=0
    for order in orders:
        total+=inv_price[order]
    return total


def main():
    menu()
    print('G :', player_g, 'g')
    orders=get_order()
    total=bill_total(orders, inv_price)
    print("So, you ordered: ", orders, ". That'll be ", total, "g.", sep='')

main()

'''
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
'''