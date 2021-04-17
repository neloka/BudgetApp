class Budget:
  def __init__(myBudget):
    myBudget.food = 30
    myBudget.clothing = 20
    myBudget.entertainment = 0

  def depositFunds(myBudget, category, amount):

    if category == "food":
      myBudget.food += amount
      print('Your food budget is ', myBudget.food)

    elif category == 'clothing':
       myBudget.clothing += amount
       print('Your clothing budget is ', myBudget.clothing)

    elif category == 'entertainment':
        myBudget.entertainment += amount
        print('Your entertainment budget is ', myBudget.entertainment)

  def WithdrawFunds(myBudget, category, amount):

    if category == "food":

      if amount > myBudget.food:
        print('insufficient funds')
      else:
        myBudget.food -= amount
        print('Your food budget is ', myBudget.food)

    elif category == 'clothing':

      if amount > myBudget.food:
        print('insufficient funds')
      else:
        myBudget.clothing -= amount
        print('Your clothing budget is ', myBudget.clothing)

    elif category == 'entertainment':

      if amount > myBudget.food:
        print('insufficient funds')
      else:
        myBudget.entertainment -= amount
        print('Your entertainment budget is ', myBudget.entertainment)

  def transferFunds(myBudget, categoryFrom, categoryTo, amount):
    if categoryFrom == 'clothing':
      if myBudget.clothing > amount:
        myBudget.clothing -= amount
        if categoryTo == 'food':
          myBudget.food += amount
          print('Your food budget is ', myBudget.food)
        elif categoryTo == 'entertainment':
          myBudget.entertainment += amount
          print('Your entertainment budget is ', myBudget.entertainment)
      else:
        print('insufficient funds')

    elif categoryFrom == 'food':
      if myBudget.food > amount:
        myBudget.food -= amount
        if categoryTo == 'clothing':
          myBudget.clothing += amount
          print('Your clothing budget is ', myBudget.clothing)
        if categoryTo == 'entertainment':
          myBudget.entertainment += amount
          print('Your entertainment budget is ', myBudget.entertainment)
      else:
        print('insufficient Funds')

    elif categoryFrom == 'entertainment':  
      if myBudget.food > amount:
        myBudget.food -= amount
        if categoryTo == 'clothing':
          myBudget.clothing += amount
          print('Your clothing budget is ', myBudget.clothing)
        if categoryTo == 'food':
          myBudget.food += amount
          print('Your food budget is ', myBudget.food)
      else:
        print('insufficient Funds')

# budg = Budget()

# print('1. food')
# print('2. clothing')
# print('3. entertainment')

# category = input('Which of these categories do you want to deposit in : ')
# amount = int(input("how much do you want to deposit : "))

# budg.depositFunds(category, amount)
# budg.WithdrawFunds('clothing', 40)
# budg.transferFunds('food', 'entertainment', 40)
      