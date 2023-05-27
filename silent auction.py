#from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("WELCOME TO THE PYTHON SILENT AUCTION!")

continue_auction=True
bids = {}

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for i in bidding_record:
    bid_amount = bidding_record[i]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = i
    if bid_amount==highest_bid:
      print(f"A tie has occured,all of the participants have the same bid.")
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while continue_auction:
  name=input("what's your name? :")
  bid=int(input("what's your bid? :Rupees"))
  dict={"name":name,"bid":bid}
  ask=input("are there any other bidders?type 'yes' to continue. type 'no' to exit\n").lower()
  bids[name] = bid
  if ask=="yes":
    clear()
  elif ask=="no":
    continue_auction=False
    find_highest_bidder(bids)
  else:
    print("enter a valid response")
