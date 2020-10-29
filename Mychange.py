#cashier enters the price
price = input("What is the cost? Use format 00.00")
#make decimal
price = float(price)
#produce 100x integer
price = price * 100
#make integer
price = int(price)
#get cash received amount and assign variable
CashTendered = input("What is the amount you would like to pay? 00.00")
#make decimal
CashTendered = float(CashTendered)
#produce 100x integer
CashTendered = CashTendered * 100
#make integer
CashTendered = int(CashTendered)
#print both values for visualization of subtraction
print(CashTendered)
print(price)
#create variable for change due from subtraction
ChangeDue = CashTendered - price
#print change due
print(ChangeDue)
#divide by 20 x 100 for units on 20$
#flor division and modulus for units of Twenties to pay out and remainder to update ChangeDue
Twenties = ChangeDue // 2000
ChangeDue = ChangeDue % 2000

#exactly the same for 10's with obvious changes will I will no longer be addressing in my code
#I hope that is ok it changes relative to the denominations in all of the following
Tens = ChangeDue // 1000
ChangeDue = ChangeDue % 1000

#same process
Fives = ChangeDue // 500
ChangeDue = ChangeDue % 500

#same process I was told to save the function for my blackbelt
Ones = ChangeDue // 100
ChangeDue = ChangeDue % 100

#same now for coins
Quarters = ChangeDue // 25
ChangeDue = ChangeDue % 25

#same
Dimes = ChangeDue // 10
ChangeDue = ChangeDue % 10

#same
Nickels = ChangeDue // 5
ChangeDue = ChangeDue % 5
#remainder of Change Due must be [0,4] and is assigned directly to pennies to return
Pennies = ChangeDue
#print values to return
print("Please. Give the customer the following bills and coins")
print("Twenties: ", Twenties)
print("Tens:  ", Tens)
print("Fives:  ", Fives)
print("Ones:  ", Ones)
print("Quarters:  ", Quarters)
print("Dimes:  ", Dimes)
print("Nickels:  ", Nickels)
print("Pennies:  ", Pennies)
