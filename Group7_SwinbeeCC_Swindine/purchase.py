#purchase module
#purchase.py

import price
import locale

#quan = quantity
#Asking customer to enter their wanted amount for menu
#It will record in the history

def rice_quan():
    print("Enter your wanted amount into the cart!")
    print("(Must enter number only.If don't want, put [0])")
    a01 = int(input("A01:"))
    a02 = int(input("A02:"))
    a03 = int(input("A03:"))
    a04 = int(input("A04:"))
    a05 = int(input("A05:"))
    a06 = int(input("A06:"))

    #Record in the history

    f = open('Swindine.txt','a')
    f.write("\n" + "~~~~RICE MENU ORDER LIST~~~~" + "\n")
    f.write("       Menu\t" + "    Quantity" + "\n")
    f.write("[A01]Nasi Lemak\t\t" + str(a01) +"\n")
    f.write("[A02]Chicken Rice\t" + str(a02) + "\n")
    f.write("[A03]Biryani\t\t" + str(a03) + "\n")
    f.write("[A04]Nasi Kerabu\t" + str(a04) + "\n")
    f.write("[A05]Nasi Kandar\t" + str(a05) + "\n")
    f.write("[A06]Nasi Goreng\t" + str(a06) + "\n")

    f.close()
    
    return a01,a02,a03,a04,a05,a06
            

def noodle_quan():
    print("Enter your wanted amount into the cart!")
    print("(Must enter number only.If don't want, put [0])")
    b01 = int(input("B01:"))
    b02 = int(input("B02:"))
    b03 = int(input("B03:"))
    b04 = int(input("B04:"))
    b05 = int(input("B05:"))
    b06 = int(input("B06:"))
    b07 = int(input("B07:"))
    b08 = int(input("B08:"))
    b09 = int(input("B09:"))
    b10 = int(input("B10:"))
    b11 = int(input("B11:"))
    b12 = int(input("B12:"))

    #Record in the history

    f = open('Swindine.txt','a')
    f.write("\n" + "~~~~NOODLE MENU ORDER LIST~~~~" + "\n")
    f.write("       Menu\t" + "    Quantity" + "\n")
    f.write("[B01]Kolo Mee\t\t" + str(b01) +"\n")
    f.write("[B02]Laksa\t\t" + str(b02) + "\n")
    f.write("[B03]Char Kway Teow\t" + str(b03) + "\n")
    f.write("[B04]Hakka Mee\t\t" + str(b04) + "\n")
    f.write("[B05]Fried Noodles\t" + str(b05) + "\n")
    f.write("[B06]Lor Mee\t\t" + str(b06) + "\n")
    f.write("[B07]Curry Mee\t\t" + str(b07) +"\n")
    f.write("[B08]Rojak Mee\t\t" + str(b08) + "\n")
    f.write("[B09]Mee Goreng\t\t" + str(b09) + "\n")
    f.write("[B10]Hokkien Mee\t" + str(b10) + "\n")
    f.write("[B11]Pan Mee\t\t" + str(b11) + "\n")
    f.write("[B12]Wonton Noodles\t" + str(b12) + "\n")

    f.close()


    return b01,b02,b03,b04,b05,b06,b07,b08,b09,b10,b11,b12

def dessert_quan():
    print("Enter your wanted amount into the cart!")
    print("(Must enter number only.If don't want, put [0])")
    c01 = int(input("C01:"))
    c02 = int(input("C02:"))
    c03 = int(input("C03:"))
    c04 = int(input("C04:"))
    c05 = int(input("C05:"))
    c06 = int(input("C06:"))

    #Record in the history

    f = open('Swindine.txt','a')
    f.write("\n" + "~~~~DESSERT MENU ORDER LIST~~~~" + "\n")
    f.write("       Menu\t" + "    Quantity" + "\n")
    f.write("[C01]Roti Canai\t\t" + str(c01) +"\n")
    f.write("[C02]Cendol\t\t" + str(c02) + "\n")
    f.write("[C03]Satay\t\t" + str(c03) + "\n")
    f.write("[C04]Rojak\t\t" + str(c04) + "\n")
    f.write("[C05]Roti Jala\t\t" + str(c05) + "\n")
    f.write("[C06]Lok-Lok\t\t" + str(c06) + "\n")

    f.close()

    return c01,c02,c03,c04,c05,c06

def coffee_quan():
    print("Enter your wanted amount into the cart!")
    print("(Must enter number only.If don't want, put [0])")
    bp1 = int(input("BP1:"))
    bp2 = int(input("BP2:"))
    bp3 = int(input("BP3:"))
    bp4 = int(input("BP4:"))
    bp5 = int(input("BP5:"))
    bp6 = int(input("BP6:"))
    bp7 = int(input("BP7:"))
    bp8 = int(input("BP8:"))
    bp9 = int(input("BP9:"))

    #Record in the history
    
    f = open('Swindine.txt','a')
    f.write("\n" + "~~~~COFFEE MENU ORDER LIST~~~~" + "\n")
    f.write("       Menu\t" + "    Quantity" + "\n")
    f.write("[BP1]Americano\t\t" + str(bp1) +"\n")
    f.write("[BP2]Latte\t\t" + str(bp2) + "\n")
    f.write("[BP3]White coffee\t" + str(bp3) + "\n")
    f.write("[BP4]Caffe Macchiato\t" + str(bp4) + "\n")
    f.write("[BP5]Caffe Mocha\t" + str(bp5) + "\n")
    f.write("[BP6]Green Tea Latte\t" + str(bp6) + "\n")
    f.write("[BP7]Mocha Latte\t" + str(bp7) +"\n")
    f.write("[BP8]Espresso\t\t" + str(bp8) + "\n")
    f.write("[BP9]Cappuccino\t\t" + str(bp9) + "\n")

    f.close()

    return bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,bp9

def tea_quan():
    print("Enter your wanted amount into the cart!")
    print("(Must enter number only.If don't want, put [0])")
    bx1 = int(input("BX1:"))
    bx2 = int(input("BX2:"))
    bx3 = int(input("BX3:"))
    bx4 = int(input("BX4:"))
    bx5 = int(input("BX5:"))
    bx6 = int(input("BX6:"))

    #Record in the history

    f = open('Swindine.txt','a')
    f.write("\n" + "~~~~TEA MENU ORDER LIST~~~~" + "\n")
    f.write("       Menu\t" + "    Quantity" + "\n")
    f.write("[BX1]Chinese Tea\t" + str(bx1) +"\n")
    f.write("[BX2]Black Tea\t\t" + str(bx2) + "\n")
    f.write("[BX3]Jasmine Green Tea\t" + str(bx3) + "\n")
    f.write("[BX4]Honey Lemon\t" + str(bx4) + "\n")
    f.write("[BX5]Iced Lemon Tea\t" + str(bx5) + "\n")
    f.write("[BX6]Oolong Tea\t\t" + str(bx6) + "\n")

    f.close()

    return bx1,bx2,bx3,bx4,bx5,bx6
