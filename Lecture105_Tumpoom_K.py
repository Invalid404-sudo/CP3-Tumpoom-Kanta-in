class Vehicle:
    licenseNumber = ""
    SerielNumber = ""
    def turnOnAirConditioner(self):
        print("Turn on : Air")
#การสืบทอดทำให้เราเอาสิ่งที่เหมือนกันมาเเยกเป็นส่วนหนึ่ง เพื่อที่จะสืบทอดไปยังฟังชั้นย่อยอื่นๆ ที่มีฟังชั้นความสามารถบางส่วนที่ต่างกัน
class Car(Vehicle) :
    def HelloWorld(self):
        print("Hello world")
class pickUp(Vehicle) :
    def HelloMars(self):
        print("Hello Mars")
class Van(Vehicle):
    def HelloNeptune(self):
        print("Hello Neptune")
class EstateCar(Vehicle):
    def HelloSun(self):
        print("Hello Sun")
car1 = Car()
car1.turnOnAirConditioner()
pickUp1 = pickUp()
pickUp1.turnOnAirConditioner()
van1 = Van()
van1.turnOnAirConditioner()
EstateCar1 = EstateCar()
EstateCar1.turnOnAirConditioner()
