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
        pass

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

#While loop
while True:
    #Call functions
    bungaloo.get_input()
    bungaloo.calc()
    bungaloo.display()



