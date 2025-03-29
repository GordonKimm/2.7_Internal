""" This Program is a Pizza menu system where the user will be able
to order food and drinks obtain it as takeway or delivery.
"""
import time
Pizzas = [["Meatlovers", "Pepperoni, sausage, bacon, ham, ground beef", 13.99],
          ["BBQ Chicken", "Grilled chicken, BBQ sauce, red onions, cilantro", 12.99 ], 
          ["Buffalo Ranch", "Spicy buffalo chicken, ranch drizzle, red onions", 12.99],
          ["🍕 THE GOLDEN SUPREME", "Handcrafted 24K Gold-Infused Dough Stuffed with imported Italian buffalo mozzarella & white truffle butter Organic San Marzano tomatoes, slow-cooked for 12 hours infused with Iranian saffron & 100-year-aged balsamic vinegar Beluga Caviar-Topped Burrata Aged Parmigiano-Reggiano (36 months) Japanese A5 Wagyu Beef – Seared & thinly sliced Maine Lobster Medallions – Butter-poached to perfection A bottle of Dom Pérignon Champagne", 1499.99]
]
def arranged_list():
    for pizza in Pizzas:
        print("--" * 30)
        print(f"Pizza: {pizza[0]}")
        time.sleep(0.75)
        print()
        print(f"Ingredients: {pizza[1]}")
        time.sleep(0.75)
        print()
        print(f"Price: {pizza[2]}$")
        time.sleep(0.75)
        print("--" * 30)
        print()
    



def user_info ():
    print()
    user_name = input ("Enter your name: ")
    print()
    user_address = input ("Enter your address: ")
    print()
    while True:
        user_payment = input ("Would you like to do card or cash").upper()
        if user_payment == "card" or "cash" :
            print("Please enter card or cash instead of a invalid option")
        else:
            break






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
        print("6.")
        print()
        print("7.User Info ")
        print()
        print("8. ")
        print()
        choice = input("Enter your choice: " )

        if choice == '1':
             arranged_list()
        elif choice == '2':
            not_yet()
        elif choice == '3':
            show_endorsed_students()
        elif choice == '4':
            add_new_student()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")
        time.sleep(60)


display_menu()