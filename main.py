import market

if __name__ == "__main__":
    Market = market()
    Continue = 1
    Cart = []
    while Continue:
        if Continue == 1:
            Market.DisplayProduct()
            Continue+=1
            print("\n\n")
        if Continue == 2:
            print("1. Add/Remove from Cart\t2. Proceed to Shipment")
            option = input()
            if option == 1:
                print("Enter the Product id,Product Qt: ")
                var = input()
                prod = list(map(int,var.split(',')))
                Market.CheckProduct(prod[0],prod[1])
                Cart.append[prod]
                print("Item Successfully added to the cart\n")
            elif option == 2:
                if len(Cart)!=0: 
                    Continue = 0
                else: 
                    print("You cannot procced with Empty Card!\n")
            else:
                print("Please input Valid option\n")
    for products in Cart:
        Market.SellProduct[products[0],products[1]]
    Market.BillDisplay()
