import json

def load_fruit_stock():
    try:
        with open('fruit_stock.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_fruit_stock(fruit_stock):
    with open('fruit_stock.json', 'w') as file:
        json.dump(fruit_stock, file)

def add_fruit_stock(fruit_name, quantity, price):
    fruit_stock = load_fruit_stock()
    if fruit_name in fruit_stock:
        fruit_stock[fruit_name]['quantity'] += quantity
        fruit_stock[fruit_name]['price'] = price
    else:
        fruit_stock[fruit_name] = {'quantity': quantity, 'price': price}
    save_fruit_stock(fruit_stock)

def view_fruit_stock():
    fruit_stock = load_fruit_stock()
    print("Fruit Stock:")
    print("{:<15} {:<10} {:<10}".format("Fruit", "Quantity", "Price"))
    print("-" * 35)
    for fruit, details in fruit_stock.items():
        quantity = details['quantity']
        price = details['price']
        print("{:<15} {:<10} {:<10}".format(fruit, quantity, price))

def update_fruit_stock(fruit_name, quantity):
    fruit_stock = load_fruit_stock()
    if fruit_name in fruit_stock:
        if fruit_stock[fruit_name]['quantity'] >= quantity:
            fruit_stock[fruit_name]['quantity'] -= quantity
            save_fruit_stock(fruit_stock)
            return True
        else:
            print("Insufficient quantity in stock.")
            return False
    else:
        print("Fruit not found in stock.")
        return False