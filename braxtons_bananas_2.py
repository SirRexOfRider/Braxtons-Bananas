"""
Name:braxtons_bananas_2
V.2
Author:Rex
Date:8/31/23
Purpose: Agile development/POS
"""
#Define main
def main():
    
    #Call functions
    bananas = get_input()
    price = calc(bananas)
    display(price)

#TODO:Get int input from user
def get_input():  
    bananas = int(input("How many bananas?: "))    
    return bananas

#TODO:Calculate price
def calc(bananas):   
    POB = 10.00      
    price = POB * bananas
    return price

#TODO:Print cost
def display(price):
    print(f"Price of bananas: ${price:,.2f}")
    


if __name__ == "__main__":
    main()




