import pyinputplus as pyip
import time
print('WELCOME TO GIUSMAHN STORES')
time.sleep(0.5)
# I created a price range of all the available items using Dict
prices = {'wheat': 9, 'white': 7, 'sourdough': 10,
          'chicken':5, 'turkey': 6, 'ham': 5, 'tofu': 5,
          'cheddar': 4, 'swiss': 3, 'mozzarella': 4,
          'mayo': 2, 'mustard': 3, 'lettuce': 2, 'tomato': 2}
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'],
                       prompt='What type of sandwinch would you like?: \n',
                       numbered=True) # I asked the user for preferred bread type using inputmenu
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
                         prompt='What type of protein would you prefer?: \n',
                         numbered=True) # I asked the user for preferred protein type using inputmenu
# I created a code asking the user if cheese is wanted using inputYesNo
answer = pyip.inputYesNo(prompt='Would you want cheese')
cheeseType = ''
if answer == 'yes':
    cheeseType = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'],
                                prompt='What cheese type do you want?: \n',
                                numbered=True)
mayo = pyip.inputYesNo(prompt='Do you want mayo in your sandwinch?(Y/N) \n')
mustard = pyip.inputYesNo(prompt='Do you want mustard in you sandwinch?(Y/N) \n')
lettuce = pyip.inputYesNo(prompt='Do you want lettuce in your sandwich?(Y/N) \n')
tomato = pyip.inputYesNo(prompt='do you want tomatoes in your sandwinch?(Y/N) \n')
# Using inputInt to ask for quantity and blockregex to prevent float,negative numbers and 0.
sandwinchQty = pyip.inputInt(prompt='how many sandwich would you like to order: \n',
                             blockRegexes=['[0|-|.]'])

# Using for loops to get their prices
totalAmount = 0
for item, price in prices.items():
    if bread == item:
        print('Here is your bill: \n'
              '%s= %s' %(item, price))
        totalAmount += price
    if protein == item:
        print('%s= %s' %(item, price))
        totalAmount += price
    if cheeseType == item:
        print('%s= %s' %(item, price))
        totalAmount += price

if 'yes' in mayo:
    print(f"mayo = {prices['mayo']}" )
    totalAmount += prices['mayo']
if 'yes' in mustard:
    print("mustard= {prices['mustard]}")
    totalAmount += prices['mustard']
if 'yes' in lettuce:
    print(f"lettuce= {prices['lettuce']}")
    totalAmount += prices['lettuce']
if 'yes' in tomato:
    print(f"tomato= {prices['tomato']}")
    totalAmount += prices['tomato']

# we get the total
print(f"sandwich cost x sandwich quantity ordered = {totalAmount}x{sandwinchQty} = "
              f"{totalAmount * sandwinchQty}")
overalAmount = str(totalAmount*sandwinchQty)


checkOut = pyip.inputYesNo(prompt='Do you want to check out now?: ')
if checkOut == 'yes':
    print(f"Your bill is " + overalAmount)
