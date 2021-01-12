def Vatcalculator(totalprice = int(input("please enter number:"))):
    result =  totalprice + totalprice*7/100
    return result

print(Vatcalculator())
