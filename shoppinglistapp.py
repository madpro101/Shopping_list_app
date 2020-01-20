# make a list to hold our items 
shopping_list = []

def display_function():
    # print out the list
    print("here is your list my guy")
    for item in shopping_list:
         print(item)
def help_function():
    # print out instructions on how to use the app
    print("Enter DONE to stop adding new items")
    print("Enter SHOW to view items that you have already added in the list")
    print("What would you like to pick up at the store?")
def add_function(new_item):
       # adding new item to list 
    shopping_list.append(new_item)
    print("Added {} to shopping list. The list now has {} items ".format(new_item, len(shopping_list)))
    
help_function()

while True:
    # ask for new items
    new_item = input("> ")
    # be able to quit the app
    if new_item=="DONE":
        break
    elif new_item =="SHOW":
         display_function()
         continue
    elif new_item == "HELP":
        help_function()
        continue
    add_function(new_item)

help_function()
    
         
  
 
 




    
