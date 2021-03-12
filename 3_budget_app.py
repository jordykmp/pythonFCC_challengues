#From README3

class Category:  
 #Initializing category
  def __init__(self, name):
    self.name = name
    self.ledger = []

  # when print() is called to show the total budget
  def __str__(self):
    return print_budget(self)  

  def deposit(self, amount, *description): 
    #Method to deposit a certain amount with optional description
    if type(description) == tuple:
      description = ''.join(description)     
    self.ledger.append({"amount": amount, "description": description})
    
  def transfer(self, amount, category):
    #Method to transfer money from one category to another
    if self.check_funds(amount): #checking funds
      self.withdraw(amount, "Transfer to %s" % category.name)
      category.deposit(amount, "Transfer from %s" % self.name)
      return True
    else:
      return False

  def withdraw(self, amount, *description):
    #Method to withdraw some amount with optional description
    if type(description) == tuple:
      description = ''.join(description)
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    #Method to returns current balance
    sum = 0.0 
    for obj in self.ledger:
      sum = sum + float(obj["amount"])
    return round(sum, 2)

  def check_funds(self, amount):
    #Method to check available funds for certain amount
    if self.get_balance() >= amount:
      return True
    else:      
      return False

  # sum of all deposits for chart function
  def get_budget_total(self):
    budget_total = 0.00
    for items in self.ledger:
      if items["amount"] > 0:
        budget_total = budget_total + float(items["amount"])
    return budget_total

  # sum of all withdrawals for chart function
  def get_budget_spent(self):
    budget_spent = 0.00
    for items in self.ledger:
      if items["amount"] < 0:
        budget_spent = budget_spent - float(items["amount"])
    return budget_spent

# creates budget printout row by row 
# concatenates rows to 1 string with line breaks and 
# returns it
def print_budget(self):
  budget_rows = []

  # create category title with title centered
  # surrounded by defined characters
  line_characters = 30
  line_filler_char = "*"

  title_name_length = len(self.name)
  title_padding = floor(
      (line_characters-title_name_length) / 2
    )
  title_extra_chars = line_characters - title_name_length - title_padding*2

  title = line_filler_char * title_padding + self.name + line_filler_char * title_padding + line_filler_char * title_extra_chars + "\n"

  budget_rows.append(title)  

  # create ledger entries 
  for items in self.ledger:
    # format desc to be presentable
    description = ''.join(items["description"]) # remove garbage around desc
    description = description[0:23] # max 23 chars

    # format amount to present
    amount = format(items["amount"], '.2f') # 2 decimal precision  
    amount = amount[0:7] # max 7 chars

    # calculate empty space in a row between desc & amount
    entry_empty_space = line_characters - len(description) - len(amount)

    # add complete row 
    budget_rows.append(description + " " * entry_empty_space + amount + "\n")

  # total amount of money in ledger
  budget_rows.append("Total: " + str(self.get_balance()))

  # concatenate all rows to 1 string and return it 
  return concatenate_rows_to_string(budget_rows)

def create_spend_chart(categories):
  # Creating lists
  list_of_categories = []
  list_of_category_name_lengths = []
  list_of_budget_spent = []
  chart_rows = []

  # collect data for the bar chart
  for val in categories:
    list_of_categories.append(val.name)
    list_of_category_name_lengths.append(len(val.name))
    list_of_budget_spent.append(val.get_budget_spent())
  
  # title row
  chart_rows.append("Percentage spent by category\n")

  # percentage rows
  for row in reversed(range(0,110,10)):
    # create bar chart row
    temporal_row = " "
    for i in range(0,len(list_of_categories),1):
      spent_percentage = round_down(floor(
        (list_of_budget_spent[i]/sum(list_of_budget_spent))*100
      ), 10)

      if row <= spent_percentage:
        temporal_row = temporal_row + "o  "
      else:
        temporal_row = temporal_row + "   "

    chart_rows.append(str(row).rjust(3, " ") + "|" + temporal_row + "\n")

  # spacer row
  chart_rows.append("    -" + "---" * len(list_of_categories) + "\n")

  # vertical category name rows
  for i in range(0,longest_str_in_list(list_of_categories),1):
    temporal_row = "     "
    for j in range(0,len(list_of_categories),1):
      if list_of_category_name_lengths[j] > i:
        temporal_row = temporal_row + list_of_categories[j][i:i+1] + "  "
      else:
        temporal_row = temporal_row + "   "

    chart_rows.append(temporal_row + "\n")

  # Last line removed
  return concatenate_rows_to_string(chart_rows).rstrip("\n")

def longest_str_in_list(list):
  longest = 0
  for val in list:
    if len(val) > longest:
      longest = len(val) 
  return longest

def concatenate_rows_to_string(rows):
  formatted_strings = ""
  for row in rows:
    formatted_strings = formatted_strings + row
  return formatted_strings

# math.floor implementation
def floor(n):
  return int(n - (n % 1))

# Rounding function to be used on chart to aprox each 10
def round_down(n, divisor):
    return n - (n % divisor)
