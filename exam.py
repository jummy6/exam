# This part of the program allows you to enter a product and add it to a list
product = []
new_product = []

def enter_product():
    x = input('Enter a product')
    return x

def add_product(product):
    y = enter_product()
    product.append(y)
    add_another_product()


def display_product():
    print(product)


def add_another_product():
    z = input('enter Y to add another or N to exit')
    if z == 'Y':
        add_product(product)
    elif z == 'N':
        display_product()
    else:
        print('invalid input')  
        add_another_product()
add_product(product)

#This part of the program converts uppercase to lower case
def to_lower_case():
    x = 0
    while x < len(product):
        y = product[x].lower()
        new_product.append(y)
        x = x+1
to_lower_case()

# This part of the program allows users to search for a products of their interest.
def search_product():
    x = input('search for a product')
    y = x.lower()
    z = 0
    if y in new_product[z]:
        count_item = new_product.count(y)
        total = len(new_product)
        print('Number of', y, 'is: ', count_item)
        print('Total item in product is: ', total)
    else:
        print('item not found')
    
search_product()

def to_lower_case():
    x = 0
    while x < len(product):
        y = product[x].lower()
        new_product.append(y)
        x = x+1
to_lower_case()
