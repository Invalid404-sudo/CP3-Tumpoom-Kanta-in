username = input("Username:")
password = input("Password:")
if username == "tumpoom" and password == "1234" :
    print("Welcome to whatever shop")
    print("1.Orange        20 bath ")
    print("2.Apple         15 bath ")
    print("3.Lay           30 bath ")
    print("4.Cookie        25 bath ")
    print("5.Comic book   199 bath ")
    userselect = int(input("please select your goods by typibg number in front of product:"))
    if userselect == 1 :
        orange = int(input("How many orange do you want?:"))
        print("Total",20*orange,"Bath")
    elif userselect == 2 :
        Apple = int(input("How many apple do you want?:"))
        print("Total", 15*Apple , "Bath")
    elif userselect == 3 :
        Lay = int(input("How many Lay do you want?:"))
        print("Total", 30*Lay , "Bath")
    elif userselect == 4 :
        Cookie = int(input("How many Cookie do you want?:"))
        print("Total", 25*Cookie , "Bath")
    elif userselect == 5 :
        ComicBook = int(input("How many Comic book do you want?:"))
        print("Total", 199*ComicBook , "Bath")
else :
    print("Access Deny")
