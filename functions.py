"""
This module contains functions for the festival planner app options.

"""

import utils

# display the options menu
def display_menu():
    print("\nMENU\nChoose an action:")
    print("1. Add a new festival")
    print("2. View all festivals")
    print("3. Remove a festival")
    print("4. Show countdown to a festival")
    print("5. Show total amount spent on festival tickets")
    print("6. Quit the application")
    print("---------------\n")
    return

# add a festival
def add_festival(festivals):
    # festival name
    name = input("Enter the name of the festival: ")

    # festival location
    location = input("Enter the location of the festival: ")

    # festival dates
    while True:
        print("Enter the starting date of the festival:")
        date = utils.get_date()
        print("Enter the ending date of the festival:")
        ending_date = utils.get_date()

        if not utils.is_valid_date_range(date, ending_date):  # check if the start date is before the end date
            print("\nInvalid date range. Please try again.")
        else:
            break

    # festival artists
    artists = []
    while True:
        artist = input("Enter an artist (or press enter to finish): ")
        if artist == "":
            break
        artists.append(artist)

    # festival price
    price = input("Enter the price in dollars of the festival (or press enter to skip): ")
    if not price.isdigit():
        # if the price is not a number or the user pressd enter, price is set to 0
        price = 0
    else:
        price = int(price)

    # create a dictionary with the festival info and add the festival to the list
    festivals.append({"name": name, "location": location, "date": date, "ending_date": ending_date, "artists": artists, "price": price})
    print("\nFestival added successfully!")
    return

# show the list of all festival
def view_festivals(festivals):
    print("List of festivals:")
    if not festivals:
        print("\nNo festivals to show.")
        return
    
    #print festival info
    for festival in festivals:
        print(f"Name: {festival['name']}")
        print(f"Location: {festival['location']}")
        print(f"From: {utils.get_format_date(festival['date'])}")
        print(f"To: {utils.get_format_date(festival['ending_date'])}")
        print(f"Artists: {', '.join(festival['artists'])}")
        print(f"Price: {festival['price']}")
        print("---------------")
    return

# remove a festival by entering the festival name
def remove_festival(festivals):
    if not festivals:
        print("There are no festivals.")
        return
    name = input("Enter the name of the festival to remove: ")
    for festival in festivals:  
        if festival['name'] == name:
            festivals.remove(festival)
            print(f"\nFestival {name} removed successfully!")
            return
    print("\nFestival not found.")
    return

# inform the user that the app is quitting
def quit_app():
    print("Goodbye!")
    return

# show the number of days until the festival starts
def countdown_to_festival(festivals):
    festival_name = input("Enter the name of the festival: ")

    for festival in festivals:
        if festival["name"] == festival_name:
            festival_date = festival["date"]
            # get the current date
                # since using external libraries is not allowed, I get the current date directly from the user
            print("Enter the current date:")
            current_date = utils.get_date()

            days_until_festival = utils.calculate_days_until_festival(current_date, festival_date)

            if days_until_festival < 0: # check if the festival has already passed
                print("\nFestival has already passed.")
            else:
                print(f"\nThere are {days_until_festival} days until {festival_name}.")
            return
    print("\nFestival not found.")

# calculate and show the total cost of all festival tickets
def calculate_total_ticket_cost(festivals):
    total_cost = 0
    for festival in festivals:
        festival_cost = festival["price"]
        total_cost += festival_cost
    print(f"\nTotal cost of all festival tickets: ${total_cost:.2f}")