# main method
def main():

    # prompt user for the amount of money they have
    cents = int(input("How much money do you have (in cents)? "))

    # display all the values
    print ("Dollars : " , dollars(cents))
    print ("Half Dollars: ", halfDollars(cents))
    print ("Dimes: ", dimes(cents))
    print ("Nickles: ", nickles(cents))
    print ("Pennies: ", pennies(cents))

# calculate the amount of dollars they have
def dollars(cents):
    return (cents/100)

# calculate the amount of half dollars they have
def halfDollars(cents):
    return (cents/50)

# calculate the amount of dimes they have
def dimes(cents):
    return (cents/10)

# calculate the amount of nickles
def nickles(cents):
    return (cents/5)

# calculate the amount of pennies
def pennies(cents):
    return (cents)
