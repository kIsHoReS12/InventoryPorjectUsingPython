import json

class Inventory:
    def __intit__(self,id,qt):
        self.id = id
        self.quantity = qt
        with open("stock.json","r") as file:
            stock_data = json.load(file)
            for stock in stock_data:
                if stock["id"] == self.id:
                    self.price = stock["price"]
                    self.stock = stock["stock"]
                    self.name = stock["name"]

    def items_sell(self):
        if self.stock >=self.qt: 
            with open('stock.json', 'w') as file:
                stock_data = json.load(file)
                for stock in stock_data:
                    if stock["id"] == id:
                        stock["stock"] -= self.qt
                json.dump(stock_data,file,indent=4)
                file.close()

            



    