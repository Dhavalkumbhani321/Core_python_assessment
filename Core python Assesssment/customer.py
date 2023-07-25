import fruit_manager
 
 

def add_transaction_to_log(transaction_details):
    with open('transaction_log.txt', 'a') as file:
        file.write(json.dumps(transaction_details) + '\n')

def buy_fruit():
    fruit_name = input("Enter the fruit name: ")
    quantity = int(input("Enter the quantity to buy: "))

    if fruit_manager.update_fruit_stock(fruit_name, quantity):
        price = fruit_manager.load_fruit_stock()[fruit_name]['price']
        total_amount = price * quantity
        print(f"Total amount to pay: {total_amount}")

        transaction_details = {
            'fruit': fruit_name,
            'quantity': quantity,
            'total_amount': total_amount
        }
        add_transaction_to_log(transaction_details)

def main():
    while True:
        print("WELCOME TO FRUIT MARKET")
        
        print("1). Manager")
        print("2). Customer")
        
        print("\n--- Fruit Market Manager---")
        print("1. Add Fruit Stock")
        print("2. View Fruit Stock")
        print("3. Update Fruit Stock")
        

        choice = input("Enter your choice :\n")
        
        

        if choice == '1':
            
            print("ADD FRUIT STOCK")
            fruit_name = input("Enter the fruit name: ")
            quantity = int(input("Enter the quantity (in kg): "))
            price = float(input("Enter the price: "))
            print(("Do you want to perform more operation : press y for yes and n for no :"))
            fruit_manager.add_fruit_stock(fruit_name, quantity, price)
            
        elif choice == '2':
            fruit_manager.view_fruit_stock()
           
        elif choice == '3':
            buy_fruit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()