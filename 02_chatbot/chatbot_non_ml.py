'''Basic Non ML chat bot!'''
print("Welcome to Basic Non ML chat bot application!")
while(True):
    user = input("You : ")

    if "hello" in user.lower() or "hi" in user.lower() or "hey" in user.lower():
        print("Bot : Hi Sir/Madam, could you help enter your name")
        your_name = input("your name : ")
        print('Bot : Hi ', your_name,'!, how can i help you today! :)'
              ' please enter "apple" if you want to buy those')
    elif "how are you" in user.lower():
        print('Bot: I am great, how can i help you today! :)'
              ' please enter "apple" if you want to buy those')
    elif "cost of apple" in user.lower() or "apple" in user.lower() or "cost" in user.lower():
        print("Bot: cost of apple is 25 rupees per piece, how many do you want")
        how_many = input("how_many : ")
        while(True):
            if how_many.isdigit():
                print("Bot: cost of apple ", how_many," would be", 25 * int(how_many),
                      " rupees in total")
                break
            else:
                print("sorry i couldn't understand, could you please try again")
    elif "bye" in user.lower() or "end" in user.lower() or "." in user.lower():
        if your_name:
            print("Bye ", your_name)
            break
        else:
            print("Bye user")
            break
    else:
        print("sorry i couldn't understand, could you please try again")
