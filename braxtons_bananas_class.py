

#Declare constants
POB = 10.50 

#Make class
class BananaBungaloo:
    def __init__(self):
        self._bananas = 0
        self.menu_items = ["Banana Bread $", "Banana smoothie $", "Banana $", "Gormet Banana Sauce $"]
        self.menu_price = [5.00,3.50,10,10]

        self.cart = []


    @property
    def name(self):
        return self._bananas

    @name.setter
    def name(self,bananas):
        self._banana = bananas

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
        
   