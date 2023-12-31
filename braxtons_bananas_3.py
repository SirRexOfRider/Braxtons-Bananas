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
        self.menu_items = ["Banana Bread $", "Banana smoothie $", "Banana $"]
        self.menu_price = [5.00,3.50,10]

        self.cart = []

    def get_menu_items(self) -> list:
        return self.menu_items
    
    def get_menu_prices(self) -> list:
        return self.menu_price
    
    def display_menu(self) -> str:
        """Display menu items and prices"""
        for n in range(3):
            print(f"{self.menu_items[n]}{self.menu_price[n]}")

    #TODO:Get int input from user
    def get_input(self):  
        self.bananas = int(input("How many bananas?: "))   

    #TODO:Calculate price
    def calc(self):   
        self.price = POB * self.bananas
        
    #TODO:Print cost
    def display(self):
        print(f"Price of bananas: ${self.price:,.2f}")

#Create object
bungaloo = BananaBungaloo()

bungaloo.get_menu_items()
bungaloo.get_menu_prices()
bungaloo.display_menu()
