#printing module
#printing.py

import datetime

def register():
    print("*"*20,"Hello! Welcome to Swindine Restaurant","*"*20)
    print()
    print("Please register your name here.")
    name = str(input("Name: ")).title()
    #Register for the customer's name
    
    while True:
        id_num = str(input("Student ID: "))
        #Register for the customer's student ID
        
        if len(id_num) == 9:
            break
        else:
            print("Invalid input. Please try again")
            print()
        
    print()
    print("You have been register!",name,",", id_num)
    #It will record in the history while registered
    
    x = datetime.datetime.now()
    f = open('Swindine.txt','a')
    f.write("\n" + "Here is your register history." + " Date:" + \
            x.strftime("%c") + "\n\n")
    f.write("Student name: " + name + "\n")
    f.write("Student ID: " + id_num + "\n")

    f.close()       

def main_menu():
#Showing the main menu that can be choose
    
    print("Please choose an option below:")
    print("""
```````````Options```````````
[A]Order
[B]Payment
[C]History
[D]VIP Membership's Benefits
[E]Recommend and Quit
""")
    

def order():
#Showing the order menu that we provided
    
    print("Here is order page! You can choose your wanted menu")
    print()
    print("Please enter the option given:")
    print("""
[F]Food
[G]Drink
[H]Dessert
""")

def food():
#Showing the food that we provided
    
    print("Here is our food provided")
    print("Please enter the food option:")
    print("""
[R]Rice
[N]Noodle
""")

def drink():
#Showing the drink that we provided
    
    print("Here is our drink provided")
    print("Please enter the drink option:")
    print("""
[C]Coffee
[T]Tea
""")

def line():
#Print the line, look more clear and neatly
    
    print("-"*80)

def tq():
#Showing the thank you message for exit
    
    print("Thank you for coming! Hope you have a nice day :)")
    print()
    print("Bye!")

def invalid():
#Input a wrong option
    
    print("Invalid input. Please try again. :(")

def add():
#Showing the option for customer that whether they want add something or not
    
    print("Do you have anything need to add on?")
    print("""
[Y]Yes
[N]No
""")

def member():
#Showing the option for customer that whether they are VIP member or not

    print("Are you a VIP membership?")
    print("""
[Y]Yes
[N]No
""")

def discount():
#Showing the option for customer that whether they want to use discount voucher or not
#Remind for the VIP member that they have delivery service
    
    print("You have 5% discount of total bill!")
    print()
    print("If you need delivery service, please imform at the counter for \
the table number while showing the made the payment.")
    print()
    print("Do you want to use 5% discount? (It cannot be use next time.)")
    print("""
[Y]Yes
[N]No
""")
    

def join():
#Showing the option for customer that whether they want to join VIP member or not

    print("Do you want to join our VIP membership?")
    print("""
[Y]Yes
[N]No
""")

def recommend():
#Showing the option for customer that whether they want to recommend or not

    print("Do you have anything need to recommend?")
    print("""
[Y]Yes
[N]No
""")
