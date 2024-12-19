import functions

festivals = []

while True:
    functions.display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        functions.add_festival(festivals)
    elif choice == "2":
        functions.view_festivals(festivals)
    elif choice == "3":
        functions.remove_festival(festivals)
    elif choice == "4":
        functions.countdown_to_festival(festivals)
    elif choice == "5":
        functions.calculate_total_ticket_cost(festivals)
    elif choice == "6":
        functions.quit_app()
        break
    else:
        print("Invalid choice. Please try again.")