import os 
# make a list to hold our items 
shopping_list = []
# function to clear the screen 
def clear_screen():
    os.system("cls" if os.name =='nt' else "clear")

def show_list():
    clear_screen()
    # print out the list
    print("Here is your list")

    for index, item in enumerate(shopping_list, start = 1):
         print("{}. {}".format(index, item))
        
         
    print("-"*20)
    
def show_help():
    clear_screen()
    # print out instructions on how to use the app
print("Enter DONE to stop adding new items")
print("Enter SHOW to view items that you have already added in the list")
print("Enter REMOVE to delete item from your list")
print("What would you like to pick up at the grocery store?")
    
def remove_from_list():
     show_list()
     item_to_remove = input("What would you like to remove?\n> ")
     try:
         shopping_list.remove(item_to_remove)
     except ValueError: 
        pass
     show_list() 

def add_function(new_item):
     show_list()
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
 
     show_list()
    
    
   

while True:
    # ask for new items
    new_item = input("> ")
    # be able to quit the app
    if new_item.upper() == "DONE" or new_item.upper() =="QUIT":
        break
    elif new_item.upper() =="SHOW":
         show_list()
         continue
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == "REMOVE":
        remove_from_list()
    else:
        add_function(new_item)

show_help()
    
         
  
 
 




    
