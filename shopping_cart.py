print("\nWelcome to INSTAMART!\n")

def Shopping_cart():
    product = {
    "Coffee": 80,
    "Tea": 50,
    "Pizza": 480,
    "Sandwich": 180,
    "Burger": 350,
    "Dosa": 130,
    "Meals": 65
    }
    
    product_list = list(product.keys())

    for item in product_list:
        print(f"{item}: {product[item]}")

    user_cart = []

    print("\nEnter items one by one. Type 'EXIT' when you are finished.")

    while True:
        selection = input("What would you like to buy: ").strip().capitalize()
        if selection == "Exit":
            break   
        if selection in product:
            try:
                qty = int(input(f"How many {selection}s do you want? "))
                if qty > 0:
                    user_cart.append({"name": selection, "qty": qty})
                    print(f"added {qty}{selection}(S) to your cart.")
                else:
                    print("quantity must be atleast 1.")
            except ValueError:
                print("Invalid input! Please enter a number for quantity.")
        else:
            print(f"Error: '{selection}' is not available in our menu, please try again.")

    Total = 0
    print("\n-----YOUR FINAL CART-----\n")

    if not user_cart:
        print("Your cart is empty!")
    else:
        for entry in user_cart:
            name = entry["name"]
            qty = entry["qty"]
            price_per_item = product[name]
            subtotal = price_per_item * qty
            
            print(f"- {name} (x{qty}): {subtotal}")
            Total += subtotal

    print(f"\nTOTAL BILL: {Total}")

Shopping_cart()
            
