print("Welcome to the online auction")

bidders = {}


def auction(in_put, bid):
    bidders[in_put] = bid


another_bidder = False

while not another_bidder:
    name = input("What is you name? ")
    amount = input("What's your bid? ")
    auction(in_put=name, bid=amount)
    add = input("Are there another bidders? Type 'yes' or 'no' ")
    if add == "no":
        another_bidder = True

highest_bid = 0
for bid in





