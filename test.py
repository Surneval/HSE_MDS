# Ask users to input information about the ticket

try:
    ticketPrice = int(input("Please enter the ticket price\n"))
    numberTransfers = int(input("Please enter the number of transfers\n"))

except (ValueError, TypeError):
    print("Error. Type a number\n")

finally:
    ticketPrice = int(input("Please enter the ticket price\n"))
    numberTransfers = int(input("Please enter the number of transfers\n"))

refund = input("Enter 'yes' if ticket is refundable, 'no' - if not")
if refund.lower() != "yes" and refund.lower() != "no":
    print("You enetered incorrect values, please try again\n")
    refund = input("Enter 'yes' if ticket is refundable, 'no' - if not")

luggage = input("Enter 'yes' if luggage is included, 'no' - if not")
if luggage.lower() != "yes" and luggage.lower() != "no":
    print("You enetered incorrect values, please try again\n")
    luggage = input("Enter 'yes' if ticket is refundable, 'no' - if not")

# Main program algorythm checks characteristics from input and determines the category

price1 = 200  # price bellow this limit we can consider as one of 'the best offer' factors
price2 = 250  # price over this limit we can consider as one of 'the worst offer' factors
transfer1 = 0  # number of transfers considered to be one of 'the best offer
transfer2 = 1
transfer3 = 2
best = 'the best'
good = 'good enough'
bad = 'bad'
other = 'other'

if ticketPrice < price1 and (numberTransfers == transfer1 or numberTransfers == transfer2) and refund.lower() == 'yes' and luggage.lower() == 'yes':
    print(f"You have a ticket of {best} category!")
elif (ticketPrice >= price1 and ticketPrice <= price2) and (numberTransfers == transfer1 or numberTransfers == transfer2 or numberTransfers == transfer3) and (refund.lower() == 'yes' or refund.lower() == 'no') and (luggage.lower() == 'yes' or luggage.lower() == 'no'):
    print(f"You have a ticket of {good} category!")
elif ticketPrice > price2 and numberTransfers > transfer3 and (refund.lower() == 'yes' or refund.lower() == 'no') and (luggage.lower() == 'yes' or luggage.lower() == 'no'):
    print(f"You have a ticket of {bad} category!")
else:
    print('You have a ticket of other category')
