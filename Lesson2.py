points = float(input('What are your points?'))
if points >= 0 and points <= 50:
    print('You do not qualify')

elif points > 50 and points <= 500:
    print('50GB free data')

elif points > 500 and points <= 1000:
    print('Free smartphone')

elif points > 1000 and points <= 1500:
    print('Free laptop')

elif points > 1500 and points <= 10000:
    print('You win a new car')
    if points >= 5500:
        print('Toyota')
    else:
        print('Nissan')

else: # No other condition
    print('Invalid... points must be 0 to 10000')

# else works if points entered are out of conditions set
# elif works for multiple conditions
# Nested statements  is an if else inside another one
