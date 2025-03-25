""" This Program is a Pizza menu system where the user will be able
to order food and drinks obtain it as takeway or delivery.
"""
Pizzas = [["Meatlovers", "Pepperoni, sausage, bacon, ham, ground beef", 13.99]
          ["BBQ Chicken", "Grilled chicken, BBQ sauce, red onions, cilantro", 12.99 ] 
          ["Buffalo Ranch", "Spicy buffalo chicken, ranch drizzle, red onions", 12.99]
          ["🍕 THE GOLDEN SUPREME", "Handcrafted 24K Gold-Infused Dough\nStuffed with imported Italian buffalo mozzarella & white truffle butter\nOrganic San Marzano tomatoes, slow-cooked for 12 hours\nnfused with Iranian saffron & 100-year-aged balsamic vinegar\nBeluga Caviar-Topped Burrata\nAged Parmigiano-Reggiano (36 months)"]
]







def display_menu():
    while True:
        print("\n🔥 PIZZA MENU 🔥")
        print("1. 🍕 BUILD YOUR OWN PIZZA")
        print("2. ")
        print("3. Show students who have earned an endorsement")
        print("4. Add new student")
        print("5. Exit")
        print("6.")
        print("7.Checkout ")
        print("8. ")
        choice = input("Enter your choice: " )

        if choice == '1':
            show_all_students()
        elif choice == '2':
            show_passed_students()
        elif choice == '3':
            show_endorsed_students()
        elif choice == '4':
            add_new_student()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")
display_menu()