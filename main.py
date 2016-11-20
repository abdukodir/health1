from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH, StringVar
from ttk import Frame, Style
from time import sleep
from threading import Thread
import paho.mqtt.client as mqtt


def thread(fn):
    def wrapped(*args, **kwargs):
        Thread(target=fn, args=args, kwargs=kwargs).start()

    return wrapped


def writeData(data, name):
    f = open(name, 'w')
    f.write(data)
    f.close()


def readData(name):
    f = open(name, 'r')
    data = f.read()
    f.close()
    return data


class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("QuickHealth")
        self.pack(fill=BOTH, expand=1)
        Style().configure("TFrame", background="white")

        user = Image.open("health.jpg")
        img_user = ImageTk.PhotoImage(user)
        show_user = Label(self, image=img_user)
        show_user.image = img_user
        show_user.place(x=0, y=0)

        image_heart = 'heart2.jpg'
        img_heart = ImageTk.PhotoImage(Image.open(image_heart))
        show_heart = Label(self, image=img_heart)
        show_heart.image = img_heart
        show_heart.place(x=220, y=0)

        self.val_show_heart = StringVar()
        self.val_show_heart.set('')
        show_heart1 = Label(self, textvar=self.val_show_heart, font='Times 35', background='white')
        show_heart1.place(x=240, y=120)

        image_pressure = 'pressure.jpg'
        img_pressure = ImageTk.PhotoImage(Image.open(image_pressure))
        show_pressure = Label(self, image=img_pressure)
        show_pressure.image = img_pressure
        show_pressure.place(x=350, y=0)

        self.val_show_pressure = StringVar()
        self.val_show_pressure.set('')
        show_heart1 = Label(self, textvar=self.val_show_pressure, font='Times 30', background='white')
        show_heart1.place(x=340, y=120)

        image_temp = 'temp.jpg'
        img_temp = ImageTk.PhotoImage(Image.open(image_temp))
        show_temp = Label(self, image=img_temp)
        show_temp.image = img_temp
        show_temp.place(x=470, y=0)

        self.val_show_temp = StringVar()
        self.val_show_temp.set('')
        show_temp1 = Label(self, textvar=self.val_show_temp, font='Times 35', background='white')
        show_temp1.place(x=480, y=120)

        image_alcohol = 'alcohol.jpg'
        img_alcohol = ImageTk.PhotoImage(Image.open(image_alcohol))
        show_alcohol = Label(self, image=img_alcohol)
        show_alcohol.image = img_alcohol
        show_alcohol.place(x=600, y=0)

        self.val_show_alcohol = StringVar()
        self.val_show_alcohol.set('')
        show_alcohol1 = Label(self, textvar=self.val_show_alcohol, font='Times 35', background='white')
        show_alcohol1.place(x=620, y=120)

        image_weight = 'weight.png'
        img_weight = ImageTk.PhotoImage(Image.open(image_weight))
        show_weight = Label(self, image=img_weight)
        show_weight.image = img_weight
        show_weight.place(x=350, y=220)

        self.val_show_weight = StringVar()
        self.val_show_weight.set('')
        show_weight1 = Label(self, textvar=self.val_show_weight, font='Times 35', background='white')
        show_weight1.place(x=370, y=330)

        image_height = 'height.png'
        img_height = ImageTk.PhotoImage(Image.open(image_height))
        show_height = Label(self, image=img_height)
        show_height.image = img_height
        show_height.place(x=470, y=220)

        self.val_show_height = StringVar()
        self.val_show_height.set('')
        show_height1 = Label(self, textvar=self.val_show_height, font='Times 35', background='white')
        show_height1.place(x=490, y=330)

        image_bmi = 'BMI.png'
        img_bmi = ImageTk.PhotoImage(Image.open(image_bmi))
        show_bmi = Label(self, image=img_bmi)
        show_bmi.image = img_bmi
        show_bmi.place(x=600, y=220)

        self.val_show_bmi = StringVar()
        self.val_show_bmi.set('')
        show_bmi1 = Label(self, textvar=self.val_show_bmi, font='Times 35', background='white')
        show_bmi1.place(x=620, y=330)

        self.val_show_result1 = StringVar()
        self.val_show_result1.set('')
        show_result1 = Label(self, textvar=self.val_show_result1, font='Times 15', background='white')
        show_result1.place(x=5, y=205)

        self.val_show_result2 = StringVar()
        self.val_show_result2.set('')
        show_result2 = Label(self, textvar=self.val_show_result2, font='Times 15', background='white')
        show_result2.place(x=5, y=230)

        self.val_show_result3 = StringVar()
        self.val_show_result3.set('')
        show_result3 = Label(self, textvar=self.val_show_result3, font='Times 15', background='white')
        show_result3.place(x=5, y=255)

        self.val_show_result4 = StringVar()
        self.val_show_result4.set('')
        show_result4 = Label(self, textvar=self.val_show_result4, font='Times 15', background='white')
        show_result4.place(x=5, y=280)

        self.val_show_result5 = StringVar()
        self.val_show_result5.set('')
        show_result5 = Label(self, textvar=self.val_show_result5, font='Times 15', background='white')
        show_result5.place(x=5, y=310)

class MyMQTTClass:
    def __init__(self, clientid=None):
        self._mqttc = mqtt.Client(clientid)
        self._mqttc.on_message = self.mqtt_on_message
        self._mqttc.on_connect = self.mqtt_on_connect
        self._mqttc.on_subscribe = self.mqtt_on_subscribe

    def mqtt_on_connect(self, mqttc, obj, flags, rc):
        print("rc: " + str(rc))

    def mqtt_on_message(self, mqttc, obj, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        if str(msg.topic) == '/heart':
            print 'Print Heart to file'
            writeData(str(msg.payload), 'heart.txt')
        if str(msg.topic) == '/pressure':
            writeData(str(msg.payload), 'pressure.txt')
        if str(msg.topic) == '/temp':
            writeData(str(msg.payload), 'temp.txt')
        if str(msg.topic) == '/alcohol':
            writeData(str(msg.payload), 'alcohol.txt')
        if str(msg.topic) == '/weight':
            writeData(str(msg.payload), 'weight.txt')
        if str(msg.topic) == '/height':
            writeData(str(msg.payload), 'height.txt')
        if msg.topic == '/pressure':
            writeData(str(msg.payload), 'pressure.txt')

    def mqtt_on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    @thread
    def run(self):
        self._mqttc.connect("192.168.1.111", 1883, 60)
        self._mqttc.subscribe("/heart", 0)
        self._mqttc.subscribe("/pressure", 0)
        self._mqttc.subscribe("/temp", 0)
        self._mqttc.subscribe("/alcohol", 0)
        self._mqttc.subscribe("/weight", 0)
        self._mqttc.subscribe("/height", 0)
        rc = 0
        while rc == 0:
            rc = self._mqttc.loop()
            sleep(1)
        return rc


@thread
def condition(_app):
    var1 = 'Heart rate above'
    var2 = 'Heart rate below'
    var3 = 'High blood pressure'
    var4 = 'Low Blood Pressure'
    var5 = 'high body temperature'
    var6 = 'Low body temperature'
    var7 = 'You are normal'
    while True:
        _app.val_show_heart.set(readData('heart.txt'))
        _app.val_show_pressure.set(readData('pressure.txt'))
        _app.val_show_temp.set(readData('temp.txt'))
        _app.val_show_alcohol.set(readData('alcohol.txt'))
        _app.val_show_weight.set(readData('weight.txt'))
        _app.val_show_height.set(readData('height.txt'))
        _app.val_show_bmi.set(readData('bmi.txt'))

        heart = float(readData('heart.txt'))
        if heart < 65:
            _app.val_show_result1.set(var2)
        elif heart > 85:
            _app.val_show_result1.set(var1)
        else:
            _app.val_show_result1.set('Your heart is normal')

        pressure1 = float(readData('pressure.txt')[0:3])
        pressure2 = float(readData('pressure.txt')[4:6])
        if pressure1 > 139 and pressure2 > 89:
            _app.val_show_result2.set(var3)
        elif pressure1 < 130:
            _app.val_show_result2.set(var4)
        else:
            _app.val_show_result2.set(var7)

        temp = float(readData('temp.txt'))
        if temp > 37.5:
            _app.val_show_result3.set(var5)
        if temp < 37:
            _app.val_show_result3.set(var6)
        else:
            _app.val_show_result3.set('Body Temperature is normal')

        sleep(1)

if __name__ == '__main__':
    root = Tk()
    root.geometry("710x410+300+300")
    app = Application(root)
    d = MyMQTTClass()
    d.run()
    condition(app)
    root.mainloop()
