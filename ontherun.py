# title and catalog formatted using format function
print('{:-<10}{:->28}{:-^20}'.format('', 'JAY Z AND BEYONCÉ', ''))
print('{:-<10}{:->30}'.format('', 'On The Run Tour'), end ='\n\n')
print('{:<8}{:<8}{:<10}'.format('SECTION', '', 'Price'))
print('{:<8}{:<8}{:<10}'.format('Platinum', '', '150.00 $'))
print('{:<8}{:<8}{:<10}'.format('Gold', '', '120.50 $'))
print('{:<8}{:<8}{:<10}'.format('Red', '', '80.75 $'))
print('{:<8}{:<8}{:<10}'.format('Green', '', '50.25 $'))

# separation border dash
print('\n' + '-' * 44)

# input each ticket value - prompts user for number of each ticket
numPlat = int(input('Enter number of Platinum Tickets: '+ ' ' * 9))
numGold = int(input('Enter number of Gold Tickets:'+ ' '*13))
numRed = int(input('Enter number of Red Tickets:' + ' '*14))
numGreen = int(input('Enter number of Green Tickets:'+ ' '*12))

# separation border dash
print('\n' + '-' * 44)

# price calculation using variables
subTotal = (numPlat * 150.00) + (numGold * 120.50) + (numRed * 80.75) + (numGreen * 50.25)
hst = (subTotal * 0.13)
serviceFees = (1.50 * (numPlat + numGold + numRed + numGreen))
total = (subTotal + hst + serviceFees)

# displays the price totals using format function
print('{:<28} ${:>10,.2f}'.format('SUBTOTAL:', '', subTotal))
print('{:<28} ${:>10,.2f}'.format('HST:', '', hst))
print('{:<28} ${:>10,.2f}'.format('SERVICE FEES:', '', serviceFees))
print('{:<28} ${:>10,.2f}'.format('TOTAL:', '', total))

# separation border dash
print('\n' + '-' * 44)

# payment method
print('How will You be Paying?\n')
print('1.', ' '*10, 'VISÀ\n')
print('2.', ' '*10, 'MasterCard\n')
print('3.', ' '*10, 'American Express\n')

payment = int(input('Enter Payment Method: '+ ' '*22))

# prompts user to enter name and details of ticket holder
your_name = input('Enter your name:'+' '*27)
creditCard = input('Enter your 16 digit Credit Card Number:'+ ' '*11)
expDate = input('Enter the expiry date (mm/yy):'+ ' '*21)

# Final Message
print('Thank you,', your_name, '!', 'Your order has been processed!')