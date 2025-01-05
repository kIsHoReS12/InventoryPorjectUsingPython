import inventory
import json 

class Market(inventory):
    def __init__(self):
        self.Confirm= 0
        self.CurrentOrders = []
    
    def DisplayProduct(self):
        inv = inventory()
        inv.display_items()
    
    def CheckProduct(self,item_id,item_qt):
        inv = inventory(item_id,item_qt)
        if (inv.id>=1 and inv.id<=15):
            if (inv.stock >= inv.qt):
                self.Confirm = 1
                self.CurrentOrders.append([inv.name,inv.qt,inv.price])
            else:
                self.CurrentOrders = []
                if inv.stock == 0:print(f"{inv.name} is out of stock")
                else:print(f"Please Enter your quantity with avaiable stock for {inv.name}")   
                return                          
        else:
            self.CurrentOrders = []
            print("Please Enter the correct Item ID!!")
            return 
    
    def SellProduct(self,item_id,item_qt):
        #if self.check == 1:
            inv = inventory(item_id,item_qt)
            inv.item_sell(item_id,item_qt)

    
    def BillDisplay(self):
        print("Item:\t    Qt:\t    Price")
        print()
        totalprice = 0
        for items in self.CurrentOrders:
            print(f"{items[0]}\t -  {items[1]}\t  -  {items[1]*items[2]}")
            totalprice+=items[1]*items[2]
        print(f"\t\tTOTAL PRICE = RS {totalprice}")
        with open("proft.json","w") as file:
            profit = json.load(file)
            profit["profit"] += totalprice
        print("Thank you, Please visit again !")
        
        
