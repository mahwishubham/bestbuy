import store
import products
import promotions


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
        print("4. Check if a product exists in the store")
        print("5. Compare with another store")
        print("6. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("------")
            print("All products in store:")
            print(store_object)
            print("------")

        elif choice == "2":
            total_value = store_object.get_total_value()
            print(f"Total value of the store: ${total_value}")

        elif choice == "3":
            print("------")
            print("When you want to finish order, enter empty text.")
            shopping_list = []
            while True:
                product_name = input("Which product do you want? ")
                if product_name == "":
                    break

                amount = input("What amount do you want? ")
                if amount == "":
                    break

                try:
                    product = store_object.find_product(product_name)
                    if product:
                        shopping_list.append((product, int(amount)))
                        print("Product added to list!")
                    else:
                        print("Product not found in the store")
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
            total_price = store_object.order(shopping_list)
            print(f"********\nOrder made! Total payment: ${total_price}\n")

        elif choice == "4":
            product_name = input("Enter the name of the product to check: ")
            product = products.Product(product_name, 0, 0)  # dummy product to check
            if product in store_object:
                print("The product exists in the store")
            else:
                print("The product does not exist in the store")

        elif choice == "5":
            # for simplicity, let's compare with a dummy store here
            dummy_store = store.Store([products.Product("dummy", 0, 0)])
            if store_object > dummy_store:
                print("The store has a higher total value than the dummy store")
            else:
                print("The store has a lower total value than the dummy store")

        elif choice == "6":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, max_purchase=1)
    ]

    second_half_price = promotions.SecondHalfPricePromotion()
    third_one_free = promotions.BuyTwoGetOneFreePromotion()
    thirty_percent = promotions.PercentageDiscountPromotion(percent=30)

    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)
