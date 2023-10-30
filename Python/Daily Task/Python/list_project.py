# list project

flag = True
# creating product
product = []

# product_price list
product_price = []

while flag:
    menu = """
                        Prass 1 for product manager
                        prass 2 for customer
                        press 3 for exit
        """
    print(menu)

    user_choice = int(input("Enter your choice : "))

    if user_choice == 1 :
     
        # While loop - repeatation
        status = True

        while status :
            name = input("Enter product name : ")
            # add data in product list
            product.append(name)
            price = int(input("Enter product price : "))
            # add data in product_price list
            product_price.append(price)
            # print(product)
            # print(product_price)
            choice = input("do you want to add more product : press y foe yes and press n for no :")
            # print("product : ", product)
            if choice =='y' or choice=='Y':
                status = True
            else:
                status = False

    elif user_choice == 2:
        print("CUSTOMER PANEL")
        # print("------>>>",product)
        # print("====>>>",product_price)
        # Display product with price
        for i in range(0,len(product)):
            print(f"{product[i]} Rs. {product_price[i]}")

    else: 
        print("THANK YOU FOR USING THIS APPLACTION")
        flag = False