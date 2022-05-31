# importing nse from nse tools
from nsetools import Nse
import random 
import time

# creating a Nse object
nse = Nse()

scrip = input("enter the name of stock : ")

# getting quote of the sbin
quote = nse.get_quote(scrip)

i=5

while i>0:

    # printing company name
    print(quote['companyName'])

    # printing buy price
    print("Buy Price : " + str(quote['buyPrice1']))


    print("Average Price: " + str(quote["averagePrice"]))

    random_wait_time = random.randrange(5.0, 6.0)
    print(random_wait_time)
    time.sleep(random_wait_time)
    