'''Basic Non ML chat bot! with multiple items (dictionary)'''
print("Welcome to Basic Non ML chat bot application with multiple items!")
products = {
    "apple" : 25,
    "orange" : 15}
while(True):
    user = input("You : ")
    your_name = None
    if "hello" in user.lower() or "hi" in user.lower() or "hey" in user.lower() or "how are you" in user.lower():
        print("Bot : Hi Sir/Madam, could you help enter your name")
        your_name = input("your name : ")
        print('Bot : Hi ', your_name,'!, how can i help you today! :)'
              ' please enter product you want to buy from these ')
        i = 1;
        for x in products:
            print(i,") ", x)
            i=i+1
        product_entered = input("enter the product : ")
        if product_entered in products:
            print("Bot: cost of ", product_entered,"is ", products[product_entered]," rupees per piece, how many do you want")
            how_many = input("how_many : ")
            while(True):
                if how_many.isdigit():
                    print("Bot: cost of ", how_many," ", product_entered,"s would be", products[product_entered] * int(how_many),
                          " rupees in total")
                    break
                elif "bye" in user.lower() or "end" in user.lower() or "." in user.lower():
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
