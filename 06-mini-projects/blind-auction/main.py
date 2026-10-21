
# Blind Auction
# Mini Projects
# Concepts: Dictionaries, Functions, Parameters, while Loops, for Loops, Conditionals
# A blind auction program that collects bids and determines the highest bidder.

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}
should_continue = True

print("Welcome to the Blind Auction!")

while should_continue:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))

    bids[name] = price

    other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no': "
    ).lower()

    if other_bidders == "no":
        should_continue = False
        find_highest_bidder(bids)
    elif other_bidders == "yes":
        print("\n" * 100)
    else:
        print("Invalid response. Ending the auction.")
        should_continue = False
        find_highest_bidder(bids)
