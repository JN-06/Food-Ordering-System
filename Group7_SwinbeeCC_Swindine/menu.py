#menu module
#menu.py

import tkinter

def gui():
#The tkinter function
#Choose the dine in or take away option at the beginning of the program
    
    r = tkinter.Tk()
    r.title("Swindine")
    #Program and restaurant's name

    w = tkinter.Label(r,text="Welcome to Swindine Restaurant. Please choose an option below.")
    w.pack()

    option = ["Dine In","Take Away"]
    #Provide two option to choose

    value = tkinter.StringVar(r)

    value.set("Option selection")

    question = tkinter.OptionMenu(r,value,*option)
    question.pack()
    

    def ans():
        print("Option choosen: {}".format(value.get()))
        return None

    submit = tkinter.Button(r,text="Submit",command=ans)
    submit.pack()

    w2 = tkinter.Label(r,text="\nAfter press submit, click exit and continue.\n")
    w2.pack()
    #Remind customer press exit and continue after submit to end this
    
    w3 = tkinter.Label(r,text="If you did not submit either one, means Dine In.\n")
    w3.pack()
    #If customer forgot to choose an option, it will means Dine In
    #Customer can change the option at counter or reopen the program
    
    eac = tkinter.Button(r, text="Exit and continue", command=r.destroy)
    eac.pack()

    r.mainloop()


def rice_menu():
#Showing the rice menu we provided
    
    print("Here are the rice we provided.")
    print()
    print("Please select the option below")
    print("""
~~~~~~~~~~RICE MENU~~~~~~~~~~~
[A01]Nasi Lemak\t\tRM10.8
[A02]Chicken Rice\tRM 9.5
[A03]Biryani\t\tRM 8
[A04]Nasi Kerabu\tRM 8.3
[A05]Nasi Kandar\tRM 8.6
[A06]Nasi Goreng\tRM 6.9
""")

def noodle_menu():
#Showing the noodle menu we provided
    
    print("Here are the noodle we provided")
    print()
    print("Please select the option below")
    print("""
~~~~~~~~~~NOODLE MENU~~~~~~~~~~~
[B01]Kolo Mee\t\tRM 5.3
[B02]Laksa\t\tRM 6
[B03]Char Kway Teow\tRM 8
[B04]Hakka Mee\t\tRM 5.7
[B05]Fried Noodles\tRM 6
[B06]Lor Mee\t\tRM 6
[B07]Curry Mee\t\tRM 7.8
[B08]Rojak Mee\t\tRM 7
[B09]Mee Goreng\t\tRM 8.5
[B10]Hokkien Mee\tRM 8
[B11]Pan Mee\t\tRM10.5
[B12]Wonton Noodles\tRM 6.8
""")

def dessert_menu():
#Showing the dessert menu we provided
    
    print("Here are the dessert we provided")
    print()
    print("Please select the option below")
    print("""
~~~~~~~~~~DESSERT MENU~~~~~~~~~~~
[C01]Roti Canai\t\tRM 3
[C02]Cendol\t\tRM 5.3
[C03]Satay\t\tRM 6
[C04]Rojak\t\tRM 8
[C05]Roti Jala\t\tRM 3
[C06]Lok-Lok\t\tRM 1
""")

def coffee_menu():
#Showing coffee menu we provided
    
    print("Here are the coffee we provided")
    print()
    print("Please select the option below")
    print("""
~~~~~~~~~~COFFEE MENU~~~~~~~~~~~
[BP1]Americano\t\tRM 9
[BP2]Latte\t\tRM 8
[BP3]White coffee\tRM 5.5
[BP4]Caffe Macchiato\tRM 9.8
[BP5]Caffe Mocha\tRM10.9
[BP6]Green Tea Latte\tRM 9.9
[BP7]Mocha Latte\tRM 8.7
[BP8]Espresso\t\tRM 3
[BP9]Cappuccino\t\tRM10
""")

def tea_menu():
#Showing tea menu we provided
    
    print("Here are the tea we provided")
    print()
    print("Please select the option below")
    print("""
~~~~~~~~~~TEA MENU~~~~~~~~~~~
[BX1]Chinese Tea\tRM 4
[BX2]Black Tea\t\tRM 4
[BX3]Jasmine Green Tea\tRM 5.6
[BX4]Honey Lemon\tRM 6.5
[BX5]Iced Lemon Tea\tRM 3.5
[BX6]Oolong Tea\t\tRM 9.9
""")

def payment_method():
#Showing the paying method we provided
    
    print("Here are the payment method we provided")
    print()
    print("Please select an option below")
    print("""
$$$$$$$PAYMENT METHOD$$$$$$$
[Q]Cash
[S]Online Payment
""")

def payment_online():
#Showing the online paying method we provided
    
    print("Please pay the total amount through the option below")
    print("After the payment done, please show the evidence to the counter")
    print("""
[T1]TNG eWallet\t    Phone number:010-1233123 (Swindine Sdn.Bhd.)
[T2]Sarawak Pay\t    Phone number:010-1233123 (Swindine Sdn.Bhd.)
[T3]Debit Card\t    Maybank    :123456789123 (Swindine Sdn.Bhd.)
[T4]Credit Card\t    Proceed at counter
""")

def gift():
#Showing the benefit we provided for the VIP member\
    
    print("Welcome become a VIP membership, you can gain some benefits.")
    print("""
^^VIP MEMBERSHIP BENEFITS^^
1. Discount
2. Gift (Collect point)
3. Delivery service
""")
    print()
    print("Here are the small gift provided")
    print("The points are adding up through your purchase.")
    print("(According to the total amount after discount.)")
    print()
    print("You must show your history points to the counter.")
    print("The staff will help you to add up the points.")
    print("""
50  point -- Free one Dessert (Lok Lok)
80  point -- Free one Coffee (Espresso)
100 point -- Free one Dessert
150 point -- Free one Tea
200 point -- Free one Food (Rice or Noodle)
300 point -- Free a recycle bag
400 point -- Free a cup
500 point -- Free a bottle
""")
    print()
    print("If you want to join, come and make an order!")
