"""
Main.py - A simple console application for managing a store's inventory and processing orders.
"""
import sys  # Importing sys for sys.exit usage
import store
import products
import promotions

def display_menu():
    """Displays the main menu of the store application."""
    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Check if a product exists in the store")
    print("5. Compare with another store")
    print("6. Quit")

def handle_choice(choice, store_object):
    """
    Handles the user's menu choice.

    Args:
        choice: The user's menu choice.
        store_object: The store object to perform actions on.
    """
    if choice == "1":
        list_all_products(store_object)
    elif choice == "2":
        show_total_amount(store_object)
    elif choice == "3":
        make_an_order(store_object)
    elif choice == "4":
        check_product_existence(store_object)
    elif choice == "5":
        compare_with_dummy_store(store_object)
    elif choice == "6":
        exit_program()

def list_all_products(store_object):
    """Lists all products available in the store."""
    print("------")
    print("All products in store:")
    print(store_object)
    print("------")

def show_total_amount(store_object):
    """
    Shows the total value of all products in the store.

    Args:
        store_object: The store object to calculate the total value of.
    """
    total_value = store_object.get_total_value()
    print(f"Total value of the store: ${total_value}")

def make_an_order(store_object):
    """
    Initiates the order making process, allowing the user to specify products and quantities.

    Args:
        store_object: The store object to order from.
    """
    print("------")
    print("When you want to finish order, enter empty text.")
    shopping_list = collect_shopping_list(store_object)
    total_price = store_object.order(shopping_list)
    print(f"********\nOrder made! Total payment: ${total_price}\n")

def collect_shopping_list(store_object):
    """
    Collects a shopping list from the user, consisting of product names and quantities.
    This function now also checks if the requested amount of a product is available in the store.

    Args:
        store_object: The store object to find products in.

    Returns:
        A list of tuples, each containing a product object and a quantity, ensuring the quantity does not exceed what is available in the store.
    """
    shopping_list = []
    while True:
        product_name = input("Which product do you want? ")
        if product_name == "":
            break
        amount_str = input("What amount do you want? ")
        if amount_str == "":
            break

        try:
            amount = int(amount_str)
            product = store_object.find_product(product_name)
            if product:
                if amount <= product.quantity:
                    shopping_list.append((product, amount))
                    print(f"{amount} of {product_name} added to list!")
                else:
                    print(f"Sorry, only {product.quantity} of {product_name} available.")
            else:
                print("Product not found in the store")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    return shopping_list

def check_product_existence(store_object):
    """
    Checks if a given product exists in the store.

    Args:
        store_object: The store object to check for product existence.
    """
    product_name = input("Enter the name of the product to check: ")
    if product_name in store_object:
        print("The product exists in the store")
    else:
        print("The product does not exist in the store")

def compare_with_dummy_store(store_object):
    """
    Compares the total value of the store's inventory with that of a dummy store.

    Args:
        store_object: The store object to compare.
    """
    dummy_store = store.Store([products.Product(product_id='1', name="dummy", price=0, quantity=0)])
    if store_object > dummy_store:
        print("The store has a higher total value than the dummy store")
    else:
        print("The store has a lower total value than the dummy store")

def exit_program():
    """Exits the program."""
    print("Exiting the program. Goodbye!")
    sys.exit()  # Using sys.exit for proper exit

def start(store_object):
    """
    Starts the store application.

    Args:
        store_object: The store object to manage and interact with.
    """
    while True:
        display_menu()
        choice = input("Please choose a number: ")
        handle_choice(choice, store_object)

if __name__ == "__main__":
    # Initialization of the store with products and promotions, and starting the application
    product_list = [
        products.Product(product_id='1', name="MacBook Air M2", price=1450, quantity=100),
        products.Product(product_id='2', name="Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product(product_id='3', name="Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct(product_id='4', name="Windows License", price=125),
        products.LimitedProduct(product_id='5', name="Shipping", price=10, quantity=250, max_purchase=1)
    ]

    second_half_price = promotions.SecondHalfPricePromotion("second half price")
    third_one_free = promotions.BuyTwoGetOneFreePromotion("Buy 2 Get 1 Free")
    thirty_percent = promotions.PercentageDiscountPromotion("30% Discount", 30)

    product_list[0].promotion = second_half_price
    product_list[1].promotion = third_one_free
    product_list[3].promotion = thirty_percent

    best_buy = store.Store(product_list)
    start(best_buy)
