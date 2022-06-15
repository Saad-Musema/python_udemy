print("Welcome to the online auction")

bidders = {}


def auction(in_put, bid):
    bidders[in_put] = bid


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if int(bid_amount) > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


another_bidder = False

while not another_bidder:
    name = input("What is you name? ")
    amount = int(input("What's your bid? "))
    auction(in_put=name, bid=amount)
    add = input("Are there other bidders? Type 'yes' or 'no' ")
    if add == "no":
        another_bidder = True

find_highest_bidder(bidding_record=bidders)

# def find_highest_bid(bidding_record):
#     highest_bid = 0
#     for value in bidders[name]:
#         winner = ""
#         if int(bidders[name]) > highest_bid:
#             highest_bid = int(bidders[name])
#             winner = value
#


# print(f"The winner of the bid is {winner}")
