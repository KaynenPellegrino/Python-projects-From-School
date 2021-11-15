

'''
The task is broken down into three sections.
Section 1 - User Input
Section 2 - loop through the grocery list
Section 3 - provide output to the console
'''

grocery_item = {} #defines empty dictionary

grocery_history = [] #defines empty list

stop = 'go'

while stop != 'Q': #While loop created so long as stop doesn't equal Q

    item_name = input('Item name: ')
    quantity = input('Quantity purchased: ')
    cost = input('Price per item: ')
    
    grocery_item['name'] = item_name
    grocery_item['number'] = int(quantity)
    grocery_item['price'] = .2f(cost)
    
    grocery_history.append(grocery_item.copy())
    stop = input("Would you like to enter another item? \nType 'c' for continue or
                 'q' to quit:")

grand_total = 0

for index, item in enumerate(grocery_history):
    item_total = item['number'] * item['price']
    grand_total += item_total
    
    print('%d %s @ $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total))
    
    item_total = 0
   
print('Grand total: $%.2f' % grand_total)