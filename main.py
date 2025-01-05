from market import Market

if __name__ == "__main__":
    MarketObj = Market()
    Continue = 1
    Cart = []
    while Continue:
        if Continue == 1:
            MarketObj.DisplayProduct()
            Continue+=1
            print("\n")
        if Continue == 2:
            option = int(input("1. Add/Remove from Cart\t2. Proceed to Shipment\n"))
            if option == 1:
                print("Enter the Product id,Product Qt: ")
                var = input()
                prodct = list(map(int,var.split(',')))
                MarketObj.CheckProduct(prodct[0],prodct[1])
                Cart.append(prodct)
                print("Item Successfully added to the cart\n")
            elif option == 2:
                if len(Cart)!=0: 
                    Continue = 0
                else: 
                    print("You cannot procced with Empty Card!\n")
            else:
                print("Please input Valid option\n")
    for products in Cart:
        MarketObj.SellProduct(products[0],products[1])

    
    MarketObj.BillDisplay()
