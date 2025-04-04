""" This Program is a Pizza menu system where the user will be able
to order food and drinks obtain it as takeway or delivery.
"""

import time
Pizzas = [{"name": "Meatlovers", "ingredients": "Pepperoni, sausage, bacon, ham, ground beef","price" : 13.99},
          {"name": "BBQ Chicken", "ingredients": "Grilled chicken, BBQ sauce, red onions, cilantro", "price" : 12.99 }, 
          {"name": "Buffalo Ranch", "ingredients": "Spicy buffalo chicken, ranch drizzle, red onions", "price" : 12.99},
          {"name": "🍕 THE GOLDEN SUPREME", "ingredients": "Handcrafted 24K Gold-Infused Dough Stuffed with imported Italian buffalo mozzarella & white truffle butter Organic San Marzano tomatoes, slow-cooked for 12 hours infused with Iranian saffron & 100-year-aged balsamic vinegar Beluga Caviar-Topped Burrata Aged Parmigiano-Reggiano (36 months) Japanese A5 Wagyu Beef – Seared & thinly sliced Maine Lobster Medallions – Butter-poached to perfection A bottle of Dom Pérignon Champagne", "price" : 1499.99}
]
Cart = []
def get_name():
    name = input("Enter your name: ")
    return name


def order_selection():
    while True:
        print("\nIs this order for:")
        print()
        selection_choice = input("Please select an option:\n1 - Delivery\n2 - Pickup\nYour choice: ")
        if selection_choice == '1':
            print("\nYou have selected delivery")
            user_address = input("Enter your delivery address: \n")
            try:
                user_phone_number = int(input("Enter your phone Number: \n"))
                print(f"\nYour order will be delivered to {user_address}")
                print(f"\nContact Number: {user_phone_number}")
                return "Delivery", user_address, user_phone_number
            except ValueError:
                print("\nThis is a invalid input please only enters numbers with your phone number")
        
        elif selection_choice == '2':
            print("You have chosen pickup")
            print()
            try:
                user_phone_number = int(input("Enter your phone number: "))
                print(f"\nContact Number: {user_phone_number}")
                return "Pickup", user_phone_number
            except ValueError:
                print("\nThis is a invalid input please only enters numbers with your phone number\n")
        else:
            print("\nPLEASE ENTER ONLY DISPLAYED NUMBERS\n")





"""This function arranges the list above me in a tidy form for the customers to see """
def arranged_list():
    if not Pizzas:
        print("Are no avaliable pizzas")
    for pizza in Pizzas:
        print("--" * 30)
        print(f"Pizza: {pizza['name']}") #pizza[0] refers to the first element in the pizza entry so it calls the first element of the list into the function#
        time.sleep(0.75)
        print()
        print(f"ingredients: {pizza['ingredients']}")
        time.sleep(0.75)
        print()
        print(f"Price: {pizza['price']}$")
        time.sleep(0.75)
        print("--" * 30)
        print()

"""This function will allow the user to make their own pizza
That will allow them to choose their own crust, cheese, 2 toppings
and at the end of the function it will ask if they would like extra toppings"""

def build_pizza():
    print("\n🍕 Let's make a custom Pizza!")
    while True:
        new_pizza_name = input("Enter the name of your pizza: ").strip()
        if new_pizza_name:
            break
    while True:
        new_pizza_ingredients = []
        print("\nMeat: \n1. Bacon\n2. Ground beef\n3. Chicken\n4. Salami\n5. Anchovies ")
        new_meat = input("Enter the number that corresponds to your selection: ").strip()
        meat_options = {
        '1': "Bacon",
        '2': "Ground beef",
        '3': "Chicken",
        '4': "Salami",
        '5': "Anchovies"
        }
        if new_meat in meat_options:
            selected_meat = meat_options[new_meat]
            new_pizza_ingredients.append(selected_meat)
            print(f"You selected {selected_meat}.")
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")
    while True:
        print("\nMeat: \n1. Mozzarella\n2. Parmesan\n3. Cheddar\n4. Feta\n5. Brie")
        new_cheese = input("Enter the number that corresponds to your selection: ").strip()
        cheese_options = {
        '1': "Mozzarella",
        '2': "Parmesan",
        '3': "Cheddar",
        '4': "Feta",
        '5': "Brie"
        }
        if new_cheese in cheese_options:
            selected_cheese = cheese_options[new_cheese]
            new_pizza_ingredients.append(selected_cheese)
            print(f"You selected {selected_cheese}.")
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")
            while True:
        print("\nMeat: \n1. Mozzarella\n2. Parmesan\n3. Cheddar\n4. Feta\n5. Brie")
        new_cheese = input("Enter the number that corresponds to your selection: ").strip()
        cheese_options = {
        '1': "Tomatoes",
        '2': "Bell Peppers",
        '3': "Cheddar",
        '4': "Feta",
        '5': "Brie"
        }
        if new_cheese in cheese_options:
            selected_cheese = cheese_options[new_cheese]
            new_pizza_ingredients.append(selected_cheese)
            print(f"You selected {selected_cheese}.")
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")
        while True:
            print("\nChoose a size:")
            print("1. Small - $7.00")
            print("2. Medium - $10.00")
            print("3. Large - $15.00")
            size_choice = input("Enter the number for your pizza size: ").strip()
            if size_choice == '1':
                new_price = 7.00
                size = "Small"
                break
            elif size_choice == '2':
                new_price = 10.00
                size = "Medium"
                break
            elif size_choice == '3':
                new_price = 15.00
                size = "Large"
                break
            else:
                print(" Invalid choice. Please enter 1, 2, or 3.")
    new_pizza = {
        "name": new_pizza_name,
        "ingredients": new_pizza_ingredients,
        "price": new_price,
        "size": size
    }
    Pizzas.append(new_pizza)
    print(f"\n Name: {new_pizza_name}\n Size: {size}\n Price: ${new_price:.2f}\n")







def display_menu():
    while True:
        print("\n🔥 PIZZA MENU 🔥")
        print()
        print("1. MENU")
        print()
        print("2. 🍕 BUILD YOUR OWN PIZZA ")
        print()
        print("3.")
        print()
        print("4. Add new student")
        print()
        print("5. ")
        print()
        choice = input("Enter your choice: " )

        if choice == '1':
             arranged_list()
        elif choice == '2':
            build_pizza()
        elif choice == '3':
            show_endorsed_students()
        elif choice == '4':
            add_new_student()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")

input("Enter to start Order: ")
print()
time.sleep(0.75)
user_name = get_name()
time.sleep(1.5)
order_selection()
time.sleep(0.75)
display_menu()