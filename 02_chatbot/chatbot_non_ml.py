'''Basic Non ML chat bot! with multiple items (dictionary'''
print("Welcome to Basic Non ML chat bot application with multiple items! \n"
     "improvements: \n"
     "1) storing the username and not overwriting it \n"
     "2) case insentivity for product entered by user \n"
     "3) exiting with bye for how_many rather than user \n"
     "4) improved menu interface")
print("in next update: multiple items in cart and bill generation")
products = {
    "apple" : 25,
    "orange" : 15}
your_name = None
while(True):
    user = input("You : ")
    if "hello" in user.lower() or "hi" in user.lower() or "hey" in user.lower() or "how are you" in user.lower():
        print("Bot : Hi Sir/Madam, could you help enter your name")
        your_name = input("your name : ")
        print('Bot : Hi ', your_name,'!, how can i help you today! :)'
              ' please enter product you want to buy from these ')
        for product, price in products.items():
            print(f"{product} - ${price}")
        product_entered = input("enter the product : ").lower()
        if product_entered in products:
            print("Bot: cost of ", product_entered,"is ", products[product_entered]," rupees per piece, how many do you want")
            how_many = input("how_many : ")
            while(True):
                if how_many.isdigit():
                    print("Bot: cost of ", how_many," ", product_entered,"s would be", products[product_entered] * int(how_many),
                          " rupees in total")
                    break
                elif "bye" in how_many.lower() or "end" in how_many.lower() or "." in how_many.lower():
                    if your_name:
                        print("Bye ", your_name)
                        break
                    else:
                        print("Bye user")
                        break
                else:
                    print("sorry i couldn't understand, could you please try again")
                    how_many = input("how_many : ")
    elif "bye" in user.lower() or "end" in user.lower() or "." in user.lower():
        if your_name:
            print("Bye ", your_name)
            break
        else:
            print("Bye user")
            break
    else:
        print("sorry i couldn't understand, could you please try again")
