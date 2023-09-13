

#Declare constants
POB = 10.50 

#Make class
class BananaBungaloo:
    def __init__(self):
        pass

    def get_number_of_bananas(self):
        if self._bananas > 0:
            return self._bananas
        else:  
            print("No bananas?")
            return 0
        
    def get_price(self): 
        return self._price

    #TODO:Calculate price
    def calc(self, bananas):   
        self._bananas = bananas
        self._price = POB * bananas
        
   