TICKET_PRICE = 10

SERVICE_CHARGE = 2
tickets_remaining = 100

#show tickets remaining
# print("there are {} tickets available".format(tickets_remaining))

#personalized welcome message
def total_price (number_of_tickets):
    return (TICKET_PRICE * number_of_tickets) + SERVICE_CHARGE

user_name = input("Please enter your name ")
print("Welcome to our ticketing system {}".format(user_name))
while tickets_remaining >= 1:
    print('there are currently {} tickets remaining'.format(tickets_remaining))
    try:
        ticket_input = input("{} how many tickets would you like? ".format(user_name))
        if not ticket_input.isdigit():
            raise ValueError("Please enter a valid number.")
        
        ticket_request = int(ticket_input)

        if ticket_request > tickets_remaining:
            raise ValueError("That exceeds the number of tickets available.")
        
        if ticket_request == 0:
            raise ValueError("You seem to have not requested any tickets")
            
        ticket_cost = total_price(ticket_request) 
        print("{} tickets will cost you ${}".format(ticket_request, ticket_cost))

        answer = input("Would you like to continue with your purchase? (Y/N) ")

        if answer.lower() == "y":
            print("SOLD!!")
            print("{}, you have purchased {} tickets and the cost is ${} .".format(user_name, ticket_request, ticket_cost))
            tickets_remaining -= ticket_request
            break
        else:
            print("See you next time")
            break
    except ValueError as err:
        print("{}".format(err))
    

else:
    print('sorry there are no tickets remaining')