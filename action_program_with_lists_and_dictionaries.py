import action_program_with_lists_and_dictionaries_logo
from replit import clear
print(action_program_with_lists_and_dictionaries_logo.logo)

switch = True

bidding_log = []
def add_new_bid(name, bid):
    new_bidder = {}
    new_bidder["name"] = user_name
    new_bidder["bid"] = user_bid
    bidding_log.append(new_bidder)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = " "
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")


while switch:

    user_name = input("What is your name?: ") #keyDictionary
    user_bid = int(input("What is your bid?: ")) #valueDictionary
    add_new_bid(name=user_name, bid=user_bid)

    stop_button = input("Do you want to continue bidding? type yes, if not type no")
    if stop_button == "no":
        switch = False
        find_highest_bidder(bidding_log)
    elif stop_button == "yes":
        clear()