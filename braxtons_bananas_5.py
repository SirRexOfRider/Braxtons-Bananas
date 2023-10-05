"""
Name:braxtons_bananas_3
V.3
Author:Rex
Date:8/31/23
Purpose: Agile development/POS
"""

#Declare constants
POB = 10.50

#Make class
class BananaBungaloo: 
    
    def __init__(self):
        #Initialize parallel lists for menu items and prices
        self.menu_items = ["Banana Bread $", "Banana smoothie $", "Banana $", "Gormet Banana Sauce $"]
        self.menu_price = [5.00,3.50,10,10]
        #Initialize a parallel cart to store the current quantity
        self.cart = [0,0,0,0]

    def get_menu_items(self) -> list:
        return self.menu_items
    
    def get_menu_prices(self) -> list:
        return self.menu_price
    
    def display_menu(self) -> str:
        """Display menu items and prices"""
        display = ""
        for n in range(len(self.menu_items)):
            display += f"{self.menu_items[n]}{self.menu_price[n]}\n"
        return display


#Create object
bungaloo = BananaBungaloo()

#Assign to variables for multiple interfaces



menu_items = bungaloo.get_menu_items()
menu_prices = bungaloo.get_menu_prices()
display_menu = bungaloo.display_menu()

print(display_menu)

