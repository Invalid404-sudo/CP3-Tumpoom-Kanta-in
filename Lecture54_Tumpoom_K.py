#login
#show menu
#select menu
#Vat
#price
x = 0
def login():
    username = input("Username:")
    password = input("Password:")
    if username == "admin" and password == "1234" :
        return True
    else:
        return False
def showMenu():
    print("Welcome to whatever shop")
    print("1.Vat calculator ")
    print("2.price calculator")
def SelectMenu():
    userselect = int(input("please select your goods by typing number in front of product:"))
    return userselect
def vatCalculate(total):
    result = total + (total * 7/100)
    return result
def priceCalculate():
    price1 = int(input("price1:"))
    price2 = int(input("price2:"))
    return vatCalculate(price1 + price2)

if login() == True and x < 5 :
    showMenu()
    selected = SelectMenu()
    if selected == 1 :
        price = int(input("plaese enter your Good's price: "))
        print(vatCalculate(price))
    elif selected == 2 :
        print(priceCalculate())
    print("Thank You")

else :
    print("     Access Deny          ")
    print("please try again later....")
