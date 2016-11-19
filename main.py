from Tkinter import *
from PIL import ImageTk, Image


def read_temp():
    print('Welcome to QuickHealth')

# variable of Sensors
alcohol = 10
temp = 37
heart = 100
pressure = 70
weight = 60
height = 1.7
bmi = round(weight/pow(height, 2), 1)
# variable of Sensors convert to Strings.
data_alcohol = str(alcohol) + ' %'
data_temp = str(temp) + ' C'
data_heart = str(heart) + '\\' + str(pressure)
data_weight = str(weight) + 'Kg'
data_height = str(height) + 'M'
data_bmi = str(bmi)

root = Tk()
root.title("QuickHealth")
root.geometry('{}x{}'.format(800, 450))

# first frame -> show user photo.
image = 'test.jpg'
img = ImageTk.PhotoImage(Image.open(image))

image_heart = 'heart2.jpg'
img_heart = ImageTk.PhotoImage(Image.open(image_heart))

image_temp = 'temp.jpg'
img_temp = ImageTk.PhotoImage(Image.open(image_temp))

image_alcohol = 'alcohol.jpg'
img_alcohol = ImageTk.PhotoImage(Image.open(image_alcohol))

image_weight = 'weight.png'
img_weight = ImageTk.PhotoImage(Image.open(image_weight))

image_height = 'height.png'
img_height = ImageTk.PhotoImage(Image.open(image_height))

image_bmi = 'BMI.png'
img_bmi = ImageTk.PhotoImage(Image.open(image_bmi))

# Create frames for Labels
frame_image = Frame(root, bg='red', width=200, height=200).grid(row=0, column=0, padx=1, pady=1,
                                                                rowspan=2, columnspan=2)
frame_heart = Frame(root, bg='cyan', width=100, height=100).grid(row=0, column=2, padx=1, pady=1,
                                                                 rowspan=1, columnspan=1)
frame_pressure = Frame(root, bg='black', width=100, height=100).grid(row=1, column=2, padx=1, pady=1,
                                                                     rowspan=1, columnspan=1)
frame_temp = Frame(root, bg='yellow', width=100, height=100).grid(row=0, column=3, padx=1, pady=1,
                                                                  rowspan=1, columnspan=1)
frame_alcohol = Frame(root, bg='red', width=100, height=100).grid(row=0, column=4, padx=1, pady=1,
                                                                  rowspan=1, columnspan=1)
frame_result = Frame(root, bg='red', width=200, height=200).grid(row=2, column=0, padx=1, pady=1,
                                                                 rowspan=2, columnspan=2)
frame_weight = Frame(root, bg='blue', width=100, height=100).grid(row=2, column=2, padx=1, pady=1,
                                                                  rowspan=1, columnspan=1)
frame_height = Frame(root, bg='cyan', width=100, height=100).grid(row=2, column=3, padx=1, pady=1,
                                                                  rowspan=1, columnspan=1)
frame_bmi = Frame(root, bg='blue', width=100, height=100).grid(row=2, column=4, padx=1, pady=1,
                                                               rowspan=1, columnspan=1)
frame = Frame(root, bg='blue', width=100, height=100).grid(row=3, column=2, padx=1, pady=1, rowspan=1, columnspan=1)
frame1 = Frame(root, bg='blue', width=250, height=100).grid(row=0, column=7, padx=30, pady=1, rowspan=1, columnspan=1)

# Show Labels in Frames
show_image = Label(frame_image, image=img, width=200, height=200).grid(row=0, column=0,
                                                                       rowspan=2, columnspan=2)
show_heart = Label(frame_heart, image=img_heart).grid(row=0, column=2, padx=1, pady=1, rowspan=1, columnspan=1, sticky='n')
show_pressure = Label(frame_pressure, text=data_heart, font='Times 25').grid(row=1, column=2)

show_temp = Label(frame_temp, image=img_temp).grid(row=0, column=3, padx=1, pady=1, rowspan=1, columnspan=1, sticky='n')
show_temp1 = Label(frame_temp, text=data_temp, font='Times 25').grid(row=0, column=3, sticky='s')

show_alcohol = Label(frame_alcohol, image=img_alcohol).grid(row=0, column=4, padx=1, pady=1, rowspan=1, columnspan=1, sticky='n')
show_alcohol1 = Label(frame_alcohol, text=data_alcohol, font='Times 25').grid(row=0, column=4, sticky='s')

show_weight = Label(frame_alcohol, image=img_weight).grid(row=2, column=2, padx=1, pady=1, rowspan=1, columnspan=1, sticky='n')
show_weight1 = Label(frame_alcohol, text=data_weight, font='Times 25').grid(row=2, column=2, sticky='s')

show_height = Label(frame_height, image=img_height).grid(row=2, column=3, padx=1, pady=1, rowspan=1, columnspan=1, sticky='n')
show_height1 = Label(frame_height, text=data_height, font='Times 25').grid(row=2, column=3, sticky='s')

show_bmi = Label(frame_bmi, image=img_bmi).grid(row=2, column=4, padx=1, pady=1, rowspan=1, columnspan=1, sticky='n')
show_bmi1 = Label(frame_bmi, text=data_bmi, font='Times 25').grid(row=2, column=4, sticky='s')

show_result = Label(frame_result, text='ket qua', font='Times 20').grid(row=2, column=0, sticky='wn')
show_result1 = Label(frame_result, text='ket qua 2 ', font='Times 20').grid(row=2, column=0, sticky='w')

root.mainloop()