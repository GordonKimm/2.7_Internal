""" This Program is a Pizza menu system where the user will be able
to order food and drinks obtain it as takeway or delivery.
"""








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