import os
import art;

print(art.logo);
print("\nWelcome to the secret auction program!\n")

auction_status = True;
bidders_data = {}
bidders_amount = [];

while auction_status:
    user_name = input("\nWhat is your name?: ");
    user_bid = int(input("\nWhat's your bid?: $"))
    other_biders = input("\nAre there any other bidders? Type 'yes' or 'no': ")
    bidders_data[user_name] = user_bid;

    if other_biders == "no":
        auction_status = False
    
    if other_biders == "yes":
        os.system('clear');

max_bid_amount = max(list(bidders_data.values()))
max_bid_person = "";

for name, bid in bidders_data.items():
    if bid == max_bid_amount:
        max_bid_person = name;


print(f"\nThe highest bidder is {max_bid_person} with ${max_bid_amount}!\n")









