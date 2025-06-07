from products import Product
from store import Store

def start(store: Store):
    while True:
        print("\n--- Welcome to Best Buy ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            print("\nAvailable Products:")
            products = store.get_all_products()
            idx = 1
            for product in products:
                print(f"{idx}. {product.show()}")
                idx += 1

        elif choice == '2':
            print(f"\nTotal quantity in store: {store.get_total_quantity()}")

        elif choice == '3':
            shopping_list = []
            products = store.get_all_products()
            print("\nEnter product numbers and quantities (leave blank to finish):")

            idx = 1
            for product in products:
                print(f"{idx}. {product.show()}")
                idx += 1

            while True:
                product_input = input("Product number (or Enter to finish): ").strip()
                if not product_input:
                    break
                try:
                    product_index = int(product_input) - 1
                    if product_index < 0 or product_index >= len(products):
                        print("Invalid product number.")
                        continue
                    quantity_input = input("Quantity: ").strip()
                    quantity = int(quantity_input)
                    shopping_list.append((products[product_index], quantity))
                except ValueError:
                    print("Invalid input. Please enter numbers.")

            try:
                total = store.order(shopping_list)
                print(f"\n✅ Order successful! Total cost: ${total}")
            except Exception as e:
                print(f"\n❌ Order failed: {e}")

        elif choice == '4':
            print("Thank you for shopping with us. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

def main():
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)

    start(best_buy)

if __name__ == "__main__":
    main()











# def main():
#     product_list = [
#         Product("MacBook Air M2", price=1450, quantity=100),
#         Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#         Product("Google Pixel 7", price=500, quantity=250),
#     ]
#
#     best_buy = Store(product_list)
#
#     products = best_buy.get_all_products()
#
#     print("Total quantity in store:", best_buy.get_total_quantity())
#
#     order_total = best_buy.order([
#         (products[0], 1),  # MacBook Air M2
#         (products[1], 2)   # Bose QuietComfort Earbuds
#     ])
#
#     print(f"Order cost: {order_total} dollars.")
#
# if __name__ == "__main__":
#     main()
#



# def main():
#     bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
#     mac = Product("MacBook Air M2", price=1450, quantity=100)
#
#     print(bose.buy(50))
#     print(mac.buy(100))
#     print(mac.is_active())
#
#     print(bose.show())
#     print(mac.show())
#
#     bose.set_quantity(1000)
#     print(bose.show())
#
#
# if __name__ == "__main__":
#     main()
