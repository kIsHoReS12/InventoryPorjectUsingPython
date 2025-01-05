import inventory
class Market(inventory):
    def __init__(self):
        self.Confirm= 0
    
    def check(self,item_id,item_qt):
        inv = inventory(item_id,item_qt)
        if (inv.id>=1 and inv.id<=15):
            if (inv.stock >= inv.qt):
                self.Confirm = 1
            else:
                if inv.stock == 0:print(f"{inv.name} is out of stock")
                else:print(f"Please Enter your quantity with avaiable stock for {inv.name}")                                  #15 24 310
        else:
            print("Please Enter the correct Item ID!!")
    def Sell(self,item_id,item_qt):
        if self.check == 1:
            inv = inventory(item_id,item_qt)
            if (inv.id>=1 and inv.id<=15):
                if (inv.stock >= inv.qt):
                    inventory.item_sell(item_id,item_qt)
                else:
        print("")
