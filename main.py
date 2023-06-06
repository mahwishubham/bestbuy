import store


def start(store_object):
    """
    Displays the menu and interacts with the Store object.

    Args:
        store_object (store.Store): The Store object to interact with.
    """
    while True:
        print("   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("------")
            print("All products in store:")
            products = store_object.get_all_products()
            for i, product in enumerate(products, start=1):
                print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            print("------")

        elif choice == "2":
            total_quantity = store_object.get_total_quantity()
            print(f"Total amount in store: {total_quantity}")

        elif choice == "3":
            print("------")
            print("When you want to finish order, enter empty text.")
            products = store_object.get_all_products()  # Retrieve the product list
            shopping_list = []
            while True:
                product_number = input("Which product # do you want? ")
                if product_number == "":
                    break

                amount = input("What amount do you want? ")
                if amount == "":
                    break

                try:
                    product_index = int(product_number) - 1
                    amount = int(amount)
                    if 0 <= product_index < len(products):
                        product = products[product_index]
                        shopping_list.append((product, amount))
                        print("Product added to list!")
                    else:
                        print("Invalid product number")
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
            total_price = store_object.order(shopping_list)
            print(f"********\nOrder made! Total payment: ${total_price}\n")

        elif choice == "4":
            break

        else:
            print("Invalid choice")


# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]
best_buy = store.Store(product_list)
start(best_buy)
