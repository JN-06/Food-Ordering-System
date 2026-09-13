import printing
import menu
import price
import purchase

#main -- Swindine

a01=a02=a03=a04=a05=a06=0
total_a01=total_a02=total_a03=total_a04=total_a05=total_a06=0
totalrice = 0

b01=b02=b03=b04=b05=b06=b07=b08=b09=b10=b11=b12=0
total_b01=total_b02=total_b03=total_b04=total_b05=total_b06=\
           total_b07=total_b08=total_b09=total_b10=total_b11=total_b12=0
totalnoodle = 0

c01=c02=c03=c04=c05=c06=0
total_c01=total_c02=total_c03=total_c04=total_c05=total_c06=0
totaldessert=0

bp1=bp2=bp3=bp4=bp5=bp6=bp7=bp8=bp9=0
total_bp1=total_bp2=total_bp3=total_bp4=total_bp5=total_bp6=total_bp7=total_bp8=total_bp9=0
totalcoffee=0

bx1=bx2=bx3=bx4=bx5=bx6=0
total_bx1=total_bx2=total_bx3=total_bx4=total_bx5=total_bx6=0
totaltea=0

totalamount=0

menu.gui()
#Can choose dine in or take away option.
print()
printing.register()
#Register name and student id, it will be record in history
printing.line()
print("We provide a variety of food. I hope you will enjoy for it!")
print()

x = True
while True:
    printing.main_menu()
    #All the main menu can be choosen
    printing.line()
    
    sel_1 = str(input("Option selection: ")).upper()
    #Choose one option from the main menu
    printing.line()

    if sel_1 == 'A':
        printing.order()
        #For the order menu, we provide food, drink and dessert.
        printing.line()
        
        while True:
            sel_2 = str(input("Option selection: ")).upper()
            #Choose one option in food, drink or dessert.
            printing.line()
            
            if sel_2 == 'F':
            #Choose for food
                printing.food()
                #Showing the food that we provide, which are rice and noodle
                printing.line()
                
                while True:
                    sel_3 = str(input("Option selection: ")).upper()
                    #Choose one option in rice or noodle
                    printing.line()
                    
                    if sel_3 == "R":
                    #Choosen for rice
                        menu.rice_menu()
                        #Showing the rice menu
                        printing.line()
                        
                        a01,a02,a03,a04,a05,a06=purchase.rice_quan()
                        totalrice = price.rice_price(a01,a02,a03,a04,a05,a06,total_a01,total_a02,\
                                                     total_a03,total_a04,total_a05,total_a06,totalrice)
                        #The total price for rice that order
                        printing.line()
                        break

                    elif sel_3 == "N":
                    #Choosen for noodle
                        menu.noodle_menu()
                        #Showing the noodle menu
                        printing.line()
                        
                        b01,b02,b03,b04,b05,b06,b07,b08,b09,b10,b11,b12=purchase.noodle_quan()
                        totalnoodle = price.noodle_price(b01,b02,b03,b04,b05,b06,b07,b08,b09,b10,b11,b12,\
                                                         total_b01,total_b02,total_b03,total_b04,\
                                                         total_b05,total_b06,total_b07,total_b08,\
                                                         total_b09,total_b10,total_b11,total_b12,\
                                                         totalnoodle)
                        #The total price for noodle that order
                        printing.line()
                        break
                 
                    else:
                        printing.invalid()
                        #Input a wrong option
                        printing.line()
                break   
                
                 
            elif sel_2 == "G":
            #Choose for drink
                printing.drink()
                #Showing the drink that we provide, which are coffee and tea
                printing.line()
                
                while True:
                    sel_4 = str(input("Option selection: ")).upper()
                    #Choose one option in coffee or tea
                    printing.line()
                    
                    if sel_4 == 'C':
                    #Choose for coffee
                        menu.coffee_menu()
                        #Showing the coffee menu
                        printing.line()
                        
                        bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,bp9 = purchase.coffee_quan()
                        totalcoffee = price.coffee_price(bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,bp9,\
                                                         total_bp1,total_bp2,total_bp3,total_bp4,\
                                                         total_bp5,total_bp6,total_bp7,total_bp8,\
                                                         total_bp9,totalcoffee)
                        #The total price for coffee that order
                        printing.line()
                        break
                    
                    elif sel_4 == 'T':
                    #Choose for tea
                        menu.tea_menu()
                        #Showing the tea menu
                        printing.line()
                        
                        bx1,bx2,bx3,bx4,bx5,bx6 = purchase.tea_quan()
                        totaltea = price.tea_price(bx1,bx2,bx3,bx4,bx5,bx6,total_bx1,total_bx2,\
                                                   total_bx3,total_bx4,total_bx5,total_bx6,totaltea)
                        #The total price for tea that order
                        printing.line()
                        break
                    
                    else:
                        printing.invalid()
                        #Input a wrong option
                        printing.line()
                break
        
            elif sel_2 == 'H':
            #Choose for dessert
                menu.dessert_menu()
                #Showing the dessert menu
                printing.line()
                
                c01,c02,c03,c04,c05,c06 = purchase.dessert_quan()
                totaldessert = price.dessert_price(c01,c02,c03,c04,c05,c06,total_c01,total_c02,\
                                                   total_c03,total_c04,total_c05,total_c06,\
                                                   totaldessert)
                #The total price for dessert that order
                printing.line()
                break

            else:
                printing.invalid()
                #Input a wrong option
                printing.line()
       
        
        while True:
            printing.add()
            #Asking customer whether they want add something or not
            printing.line()
            
            sel_4 = str(input("Option selection: ")).upper()
            #Ask for yes or no
            printing.line()
            
            if sel_4 == "Y":
                totalamount = price.total_price(totalrice,totalnoodle,totaldessert,totaltea,totalcoffee)
                #The total amount for the previous order
                printing.line()
                break

            elif sel_4 == 'N':
                totalamount = price.total_price(totalrice,totalnoodle,totaldessert,totaltea,totalcoffee)
                #The total amount for the previous order
                printing.line()
                break
            
            else:
                printing.invalid()
                #Input a wrong option
                printing.line()
                    
    elif sel_1 == 'B':
        print("Your order have been received.Here is your total amount.")
        print()
        totalamount = price.total_price(totalrice,totalnoodle,totaldessert,totaltea,totalcoffee)
        #Showing the total amount that had order
        printing.line()
        
        printing.member()
        #Asking customer whether they are VIP member or not
        printing.line()
        
        while True:
            sel_5 = str(input("Option Selection: ")).upper()
            #Ask for yes or no
            printing.line()
            
            if sel_5 == 'Y':
            #Choose yes
                printing.discount()
                #VIP member will give discount
                printing.line()
                
                while True:
                    sel_6 = str(input("Option Selection: ")).upper()
                    #Asking customer whether they want to use discount voucher or not
                    printing.line()
                    
                    if sel_6 == 'Y':
                    #Choose yes    
                        price.discount(totalrice,totalnoodle,totaldessert,totaltea,totalcoffee)
                        #Showing the sub total, discount, gst, service tax and rounded total
                        break
                    
                    elif sel_6 == 'N':
                        price.ori(totalrice,totalnoodle,totaldessert,totaltea,totalcoffee)
                        #Showing the sub total, gst, service tax and rounded total
                        break

                    else:
                        printing.invalid()
                        #Input a wrong option
                        printing.line()

                break
                
            elif sel_5 == 'N':
            #Choose no
                printing.join()
                #Asking customer whether they want to join the VIP member or not
                printing.line()
                
                while True:
                    sel_7 = str(input("Option selection: ")).upper()
                    #Asking yes or no
                    printing.line()
                    
                    if sel_7 == 'Y':
                    #Customer want to join VIP
                        printing.discount()
                        #Asking customer whether they want to use discount voucher or not
                        printing.line()
                        
                        while True:
                            sel_8 = str(input("Option Selection: ")).upper()
                            #Asking yes or no
                            printing.line()
                            
                            if sel_8 == 'Y':
                                price.discount(totalrice,totalnoodle,totaldessert,totaltea,totalcoffee)
                                #Showing the sub total, discount, gst, service tax and rounded total
                                break
                                
                            elif sel_8 == 'N':
                                price.ori(totalrice,totalnoodle,totaldessert,totaltea,totalcoffee)
                                #Showing the sub total, gst, service tax and rounded total
                                break

                            else:
                                printing.invalid()
                                #Input a wrong option
                        break
                        
                    elif sel_7 == 'N':
                    #Customer did not want to join VIP
                        price.ori(totalrice,totalnoodle,totaldessert,totaltea,totalcoffee)
                        #Showing the sub total, gst, service tax and rounded total
                        break
                        
                    else:
                        printing.invalid()
                        #Input a wrong option
                        printing.line()

                break
                    
            else:
                printing.invalid()
                #Input a wrong option
                printing.line()

        printing.line()
        menu.payment_method()
        #Showing the payment method, face-to-face (Cash) or online paying
        
        while True:
            sel_9 = str(input("Option selection: ")).upper()
            #Choose payment method
            printing.line()
            
            if sel_9 == 'Q':
            #Choose paying cash, pay at counter
                print("Proceed at counter. Resit can get at counter.")
                print()
                print("Your order have been recorded. Thank you ^_^")
                printing.line()
                break

            elif sel_9 == 'S':
            #Choose online paying
                menu.payment_online()
                #Showing the online paying method
                #After paying, customer need to give a look at counter
                print("Please show your payment evidence to the counter.")
                print("Resit can get at counter.")
                print()
                print("Your order have been recorded. Thank you ^_^")
                printing.line()
                break

            else:
                printing.invalid()
                #Input a wrong option
                printing.line()

        

    elif sel_1 == 'C':
    #Choose for history
    #Can look for the history for register and spending
        
        with open('Swindine.txt','r') as f:
            history = f.read()
            print(history)

        f.close()
        printing.line()

    elif sel_1 == 'D':
    #Look for the VIP Membership's Benefits
    #Customer can look for the benefits and also the list of gift
        
        menu.gift()
        printing.line()
        
    elif sel_1 == 'E':
    #Choose exit to close the program
        printing.recommend()
        #Asking customer whether they have any recommend or not
        printing.line()
        while True:
            sel_10 = str(input("Option selection: ")).upper()
            #Ask for yes or no
            printing.line()
            if sel_10 == 'Y':
            #Choose yes
                input_2 = str(input("Recommend: "))
                #Can let customer type their recommend
                
                #It will record in the history
                f = open('Swindine.txt','a')
                f.write("\n" + "Recommend: " + str(input_2) + "\n")
                f.close()
                break

            elif sel_10 == 'N':
                #Choose no and quit
                break

            else:
                printing.invalid()
                #Input a wrong option
                printing.line()
                
        print("Thank you for coming. Welcome back again ^_^")
        break
        
    else:
        printing.invalid()
        #Input a wrong option
        printing.line()
