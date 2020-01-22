import os 
# make a list to hold our items 
shopping_list = []
# function to clear the screen 
def clear_screen():
    os.system("cls" if os.name =='nt' else "clear")

def display_function():
    clear_screen()
    # print out the list
    print("here is your list my guy")
    index = 1
    for item in shopping_list:
         print("{}. {}".format(index, item))
         index += 1
    print("-"*20)
    
def help_function():
    clear_screen()
    # print out instructions on how to use the app
print("Enter DONE to stop adding new items")
print("Enter SHOW to view items that you have already added in the list")
print("What would you like to pick up at the store?")
    

def add_function(new_item):
     display_function()
     if len(shopping_list):
        position = input("Where should I add {}\n"
                         "Press Enter to add item at the end of the list\n "
                         "> ".format(new_item))
     else:
        position = 0 
        
     try: 
        position = abs(int(position))
     except ValueError:
        position = None
     if position is not None:
        shopping_list.insert(position-1, new_item)
     else:
        shopping_list.append(new_item)
    # adding new item to list 
 
     display_function()
    
    
   

while True:
    # ask for new items
    new_item = input("> ")
    # be able to quit the app
    if new_item.upper() == "DONE" or new_item.upper() =="QUIT":
        break
    elif new_item.upper() =="SHOW":
         display_function()
         continue
    elif new_item.upper() == "HELP":
        help_function()
        continue
    else:
        add_function(new_item)

help_function()
    
         
  
 
 




    
