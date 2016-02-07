"""Tax and Tip Calculator- Author Damian Ali
This program will caculate tax by percentage as well as tip by
percentage, against what was paid for a meal (as an example)."""


print "Welcome to the taxes and tip calculator!"   #this line prints a welcome/achknowledgement of running of this program#

price=input('What is the price before tax? ')     #this line sets the variable price to accept any numerical input.#
tax=input('What are the taxes? (in %) ')          #this line sets the variable tax amount by percentage.#
tip=input('What do you want to tip? (in %) ')     #this line sets the variable tip amount to be given by percentage# 

price=price+(price*float(tax)/100)          #this line resets the variable price to calculate the sum of the original price and the tax calculated by percentage.#
price=price+(price*float(tip)/100)      #this line resets the variable price once again adding the past sum to the tip once calculated by percentage.#

print "The price you need to pay is: $%.6f." % price  #this line prints the total price calculated.#
