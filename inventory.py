import json

class Inventory:
    def __init__(self,id=None,qt=None):
        self.id = id
        self.qt = qt
        with open("stock.json","r") as file:
            stock_data = json.load(file)
            for stock in stock_data:
                if stock["id"] == self.id:
                    self.price = stock["price"]
                    self.stock = stock["stock"]
                    self.name = stock["name"]

    def items_sell(self,id=None,qt=None):
            
            with open('stock.json', 'r+') as file:
                stock_data = json.load(file)
                for stock in stock_data:
                    if stock["id"] == id:
                        stock["stock"] -= self.qt
                file.seek(0)
                json.dump(stock_data,file,indent=4)
                
    
    def display_items(self):
        with open("stock.json","r") as file:
            display_data = json.load(file)
            for data in display_data:
                print(f"Name: {data['name']} * AvaiableQt: {data['stock']} * Price/Qt: {data['price']}")
                
