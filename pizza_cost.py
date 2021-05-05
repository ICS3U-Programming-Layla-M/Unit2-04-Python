#!/usr/bin/env python3
# Created by: Layla Michel
# Created on: May 5, 2021
# This program calculates and displays the total
# cost of a pizza using user input.

import constants


def main():
    # Ask the user for the diameter size
    global diameter
    print("This will calculate the total cost for a pizza.")
    diameter = float(input("Enter the diameter size (inches): "))
    calc_total()


def calc_total():
    # Calculate the subtotal, tax and total
    subtotal = constants.LABOUR_COST + constants.RENT_COST\
     + constants.ING_COST * diameter
    tax = subtotal * constants.HST
    total = subtotal + tax

    # Display the total
    print("The total cost (with HST) is: ${:,.2f}". format(total))


if __name__ == "__main__":
    main()
