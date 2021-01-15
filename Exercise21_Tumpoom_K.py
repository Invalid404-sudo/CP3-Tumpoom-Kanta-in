from tkinter import *
import math
def leftclickButton(event):
    print("Left Click")
def rightclickButton(event):
    print("Right Click")
def DoubleClick(event):
    print("Double Click")
def RightandLeft():
    main = Tk()
    button = Button(main,text = "My button")
    button.pack()
    button.bind('<Button-1>', leftclickButton)
    button.bind('<Button-3>', rightclickButton)
    main.mainloop()
def Calculate(event):
    result = float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2)
    print(float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2))
    if result > 30 :
        labelresult.configure(text = "อ้วนมาก")
    elif 29.9 >= result >= 25.0 :
        labelresult.configure(text="อ้วน")
    elif 24.9 >= result >= 23.0 :
        labelresult.configure(text="น้ำหนักเกิน")
    elif 22.9 >= result >= 18.6 :
        labelresult.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        labelresult.configure(text="ผอมเกินไป")

main = Tk()
labelHeight=Label(main,text="ส่วนสูง " )
labelHeight.grid(row =0,column= 0)
textboxHeight = Entry(main)
textboxHeight.grid(row=0,column=1)
labelWeight = Label(main, text="น้ำหนัก")
labelWeight.grid(row=1, column=0)
textboxWeight = Entry(main)
textboxWeight.grid(row=1, column=1)
print(type(textboxWeight))
CalculateButton = Button(main,text = "คำนวณ")
CalculateButton.bind('<Button-1>',Calculate)
CalculateButton.grid(row=2,column = 0)
labelresult = Label(main, text="ผลลัพธ์")
labelresult.grid(row=2, column=1)
main.mainloop()
