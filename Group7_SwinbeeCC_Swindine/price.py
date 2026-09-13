#price module
#price.py

import locale
locale.setlocale(locale.LC_ALL,'en_MY')
import purchase

def rice_price(a01,a02,a03,a04,a05,a06,total_a01,total_a02,\
               total_a03,total_a04,total_a05,total_a06,totalrice):
#The total price for each rice menu
    
    total_a01 += (a01*10.8)
    total_a02 += (a02*9.5)
    total_a03 += (a03*8)
    total_a04 += (a04*8.3)
    total_a05 += (a05*8.6)
    total_a06 += (a06*6.9)
                  
    totalrice = total_a01 + total_a02 + total_a03 + total_a04 + total_a05 + total_a06
    #The total price that adding all of the rice menu that order
    print("Total price:",locale.currency(totalrice))
    return totalrice

def noodle_price(b01,b02,b03,b04,b05,b06,b07,b08,b09,b10,b11,b12,\
                 total_b01,total_b02,total_b03,total_b04,total_b05,\
                 total_b06,total_b07,total_b08,total_b09,total_b10,\
                 total_b11,total_b12,totalnoodle):
#The total price for each noodle menu
    
    total_b01 += (b01*5.3)
    total_b02 += (b02*6)
    total_b03 += (b03*8)
    total_b04 += (b04*5.7)
    total_b05 += (b05*6)
    total_b06 += (b06*6)
    total_b07 += (b07*7.8)
    total_b08 += (b08*7)
    total_b09 += (b09*8.5)
    total_b10 += (b10*8)
    total_b11 += (b11*10.5)
    total_b12 += (b12*6.8)

    totalnoodle = total_b01 + total_b02 + total_b03 + total_b04 + total_b05 + \
                 total_b06 + total_b07 + total_b08 + total_b09 + total_b10 + \
                 total_b11 + total_b12
    #The total price that adding all of the noodle menu that order
    print("Total price:", locale.currency(totalnoodle))
    return totalnoodle


def dessert_price(c01,c02,c03,c04,c05,c06,total_c01,total_c02,total_c03,\
                  total_c04,total_c05,total_c06,totaldessert):
#The total price for each dessert menu
    
    total_c01 += (c01*3)
    total_c02 += (c02*5.3)
    total_c03 += (c03*6)
    total_c04 += (c04*8)
    total_c05 += (c05*3)
    total_c06 += (c06*1)

    totaldessert = total_c01 + total_c02 + total_c03 + total_c04 + total_c05 +\
                   total_c06
    #The total price that adding all of the dessert menu that order
    print("Total price:", locale.currency(totaldessert))
    return totaldessert

def coffee_price(bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,bp9,total_bp1,total_bp2,total_bp3,\
                 total_bp4,total_bp5,total_bp6,total_bp7,total_bp8,total_bp9,totalcoffee):
#The total price for each coffee menu
    
    total_bp1 += (bp1*9)
    total_bp2 += (bp2*8)
    total_bp3 += (bp3*5.5)
    total_bp4 += (bp4*9.8)
    total_bp5 += (bp5*10.9)
    total_bp6 += (bp6*9.9)
    total_bp7 += (bp7*8.7)
    total_bp8 += (bp8*3)
    total_bp9 += (bp9*10)

    totalcoffee = total_bp1 + total_bp2 + total_bp3 + total_bp4 + total_bp5 + \
                 total_bp6 + total_bp7 + total_bp8 + total_bp9
    #The total price that adding all of the coffee menu that order
    print("Total price:", locale.currency(totalcoffee))
    return totalcoffee

def tea_price(bx1,bx2,bx3,bx4,bx5,bx6,total_bx1,total_bx2,total_bx3,\
              total_bx4,total_bx5,total_bx6,totaltea):
#The total price for each tea menu
    
    total_bx1 += (bx1*4)
    total_bx2 += (bx2*4)
    total_bx3 += (bx3*5.6)
    total_bx4 += (bx4*6.5)
    total_bx5 += (bx5*3.5)
    total_bx6 += (bx6*9.9)
   
    totaltea = total_bx1 + total_bx2 + total_bx3 + total_bx4 + total_bx5 + total_bx6 
    #The total price that adding all of the tea menu that order
    print("Total price:", locale.currency(totaltea))
    return totaltea

def total_price(totalrice,totalnoodle,totaldessert,totaltea,totalcoffee):
#The total price that adding all of the menu that order
    
    totalamount = float(totalrice+totalnoodle+totaldessert+totaltea+totalcoffee)
    print("Total amount:",locale.currency(totalamount))
    
    

def discount(totalrice,totalnoodle,totaldessert,totaltea,totalcoffee):
#discount = A VIP member, which can get discount
#The discount given to the VIP member
#Showing the final amount
#Final amount include sub total, discount, gst, service tax and rounded total
    
    totalamount = float(totalrice+totalnoodle+totaldessert+totaltea+totalcoffee)
    print("Here is your amount. Please check carefully *_*")
    print()
    print("Sub Total:",locale.currency(totalamount))
    #Showing the original price
    
    print()
    dis = float(totalamount)*0.05
    print("Discount    (5%):",locale.currency(dis))
    #The discount given to the VIP member
    
    after_dis = float(totalamount)- float(dis)
    #The amount after the discount deducted
    
    gst = float(after_dis)*0.04
    print("GST         (4%):",locale.currency(gst))
    #The gst that charge
    
    ser = float(after_dis)*0.02
    print("Service Tax (2%):",locale.currency(ser))
    #The service tax that charge
    
    tax = float(after_dis)*0.06
    #The total charge
    
    print()
    totalamount=float(after_dis)+float(tax)
    print("Rounded Total:",locale.currency(totalamount))
    #Showing the final amount that customer need to pay
    
    #Final amount will record in history
    #The point will show in the history, which is same as the final amount
    #The point will add up by the staff at counter, if customer want to exchange the gift
    f = open('Swindine.txt','a')
    f.write("\n"+ "Here is your paying history." + "\n")
    f.write("Spending: " + locale.currency(totalamount) + "\n")
    f.write("Points: + "+ str(round(totalamount,2)) + "\n")

    f.close()

def ori(totalrice,totalnoodle,totaldessert,totaltea,totalcoffee):
#ori = original price, not VIP member
#Showing the final amount
#Final amount include sub total, gst, service tax and rounded total
    
    totalamount = float(totalrice+totalnoodle+totaldessert+totaltea+totalcoffee)
    print("Here is your amount. Please check carefully *_*")
    print("Sub Total:",locale.currency(totalamount))
    #Showing the original price
    
    print()
    gst = float(totalamount)*0.04
    print("GST         (4%):",locale.currency(gst))
    #The gst that charge
    
    ser = float(totalamount)*0.02
    print("Service Tax (2%):",locale.currency(ser))
    print()
    #The service tax that charge
    
    totalamount = float(totalamount) +float(gst) + float(ser)
    print("Rounded Total:",locale.currency(totalamount))
    #Showing the final amount that customer need to pay

    #Final amount will record in history
    f = open('Swindine.txt','a')
    f.write("\n"+ "Here is your paying history." + "\n")
    f.write("Spending: " + locale.currency(totalamount) + "\n")
    
    f.close()

   
