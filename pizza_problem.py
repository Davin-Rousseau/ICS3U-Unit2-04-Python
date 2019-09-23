#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on September 2019
# This proogram calculates the cost of pizza
# with user giving diameter (inches) of pizza

import pizza_constants


def main():
    # This function calculates the cost of pizza

    # input
    diameter = int(input("Enter the diameter of the pizza you would " +
                         "like (inch): "))

    # process
    sub_total = pizza_constants.LABOR + pizza_constants.RENT + \
        (diameter * pizza_constants.COST_PER_INCH)
    total = sub_total + (sub_total * pizza_constants.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is: ${1:,.2f}"
          .format(diameter, total))


if __name__ == "__main__":
    main()
