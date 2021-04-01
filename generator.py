from tkinter import *
from tkinter import ttk
from PIL import Image
from tkinter import filedialog as fd
from tkinter.messagebox import *
import random
import string

root = Tk()

root.iconbitmap("kyd2.ico")
root.title("Генератор паролей")
root.geometry("740x425+700+300")
root.resizable(width=False, height=False)
style = ttk.Style()
style.theme_use('clam')
#\\\\\\\\\\\\\\\\\\\\\\\\\\фон text
def run():
    if var.get()==1:
        calculated_text['bg']='#DDA905'
    if var.get()==2:
        calculated_text['bg']='#0CCB91'
    if var.get()==3:
        calculated_text['bg']='#5A5B8D'
var=IntVar()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\
def next_image_generator10():
    photo_list = [
        PhotoImage(file="Бирюзовый.png"),
        PhotoImage(file="Бирюзовый.png"),
        PhotoImage(file="Бирюзовый.png"),
    ]

    while True:
        yield from photo_list


NEXT_IMAGE10 = next_image_generator10()

def get_next_image10():
    return next(NEXT_IMAGE10)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def next_image_generator9():
    photo_list = [
        PhotoImage(file="Фиолетовый.png"),
        PhotoImage(file="Фиолетовый.png"),
        PhotoImage(file="Фиолетовый.png"),
    ]

    while True:
        yield from photo_list


NEXT_IMAGE9 = next_image_generator9()

def get_next_image9():
    return next(NEXT_IMAGE9)
#\\\\\\\\\\\\\\\\\\\\\
def next_image_generator8():
    photo_list = [
        PhotoImage(file="Оранжевый.png"),
        PhotoImage(file="Оранжевый.png"),
        PhotoImage(file="Оранжевый.png"),
    ]

    while True:
        yield from photo_list


NEXT_IMAGE8 = next_image_generator8()

def get_next_image8():
    return next(NEXT_IMAGE8)
#\\\\\\\\\\\\\\\\\\\\\\\\\
root.configure(background='grey22')
def next_image_generator7():
    photo_list = [
        PhotoImage(file="Отделение строки.png"),
        PhotoImage(file="Отделение строки.png"),
        PhotoImage(file="Отделение строки.png"),
    ]

    while True:
        yield from photo_list


NEXT_IMAGE7 = next_image_generator7()

def get_next_image7():
    return next(NEXT_IMAGE7)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def next_image_generator6():
    photo_list = [
        PhotoImage(file="Спецсимволы.png"),
        PhotoImage(file="Спецсимволы.png"),
        PhotoImage(file="Спецсимволы.png"),
    ]

    while True:
        yield from photo_list


NEXT_IMAGE6 = next_image_generator6()

def get_next_image6():
    return next(NEXT_IMAGE6)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def next_image_generator5():
    photo_list = [
        PhotoImage(file="Цифры.png"),
        PhotoImage(file="Цифры.png"),
        PhotoImage(file="Цифры.png"),
    ]

    while True:
        yield from photo_list


NEXT_IMAGE5 = next_image_generator5()

def get_next_image5():
    return next(NEXT_IMAGE5)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\
def next_image_generator4():
    photo_list = [
        PhotoImage(file="длина поролей.png"),
        PhotoImage(file="длина поролей.png"),
        PhotoImage(file="длина поролей.png"),
    ]

    while True:
        yield from photo_list


NEXT_IMAGE4 = next_image_generator4()

def get_next_image4():
    return next(NEXT_IMAGE4)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def next_image_generator3():
    photo_list = [
        PhotoImage(file="количество поролей.png"),
        PhotoImage(file="количество поролей.png"),
        PhotoImage(file="количество поролей.png"),
    ]

    while True:
        yield from photo_list


NEXT_IMAGE3 = next_image_generator3()

def get_next_image3():
    return next(NEXT_IMAGE3)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def _on_button_click(button):
    button.config(image=get_next_image())
    button.config(image=get_next_image3())
    button.config(image=get_next_image4())
    button.config(image=get_next_image5())
    button.config(image=get_next_image6())
    button.config(image=get_next_image7())
    button.config(image=get_next_image8())
    button.config(image=get_next_image9())
    button.config(image=get_next_image10())
def next_image_generator():
    photo_list = [
        PhotoImage(file="1.png"),
        PhotoImage(file="1.png"),
        PhotoImage(file="1.png"),
    ]

    while True:
        yield from photo_list


NEXT_IMAGE = next_image_generator()

def get_next_image():
    return next(NEXT_IMAGE)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def _on_button_click1(button):
    button.config(image=get_next_image1())


def next_image_generator1():
    photo_list = [
        PhotoImage(file="2.png"),
        PhotoImage(file="2.png"),
        PhotoImage(file="2.png"),
    ]

    while True:
        yield from photo_list


NEXT_IMAGE1 = next_image_generator1()

def get_next_image1():
    return next(NEXT_IMAGE1)




def insert_text():#Открыть
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    calculated_text.insert(1.0, s)
    f.close()


def extract_text():#Сохранить как
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm")))
    f = open(file_name, 'w')
    s = calculated_text.get(1.0, END)
    f.write(s)
    f.close()


def close_win():#exit
    if askyesno("Выход", "Вы уверены?"):
        root.destroy()


def about():#О программе
    showinfo("Генератор паролей ", "Версия:2.5")

#menu
m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_cascade(label="Файл", menu=fm)
fm.add_command(label="Открыть...", command=insert_text)
fm.add_command(label="Сохранить как...", command=extract_text)
fm.add_command(label="Выход", command=close_win)
hm = Menu(m)
m.add_cascade(label="Справка", menu=hm)
hm.add_command(label="О программе", command=about)


def copy():
    calculated_text.clipboard_clear()  # Очистить буфер обмена
    calculated_text.clipboard_append(calculated_text.get(
        1.0, END))  # Скопировать текст в буфер обмен



chk_state = IntVar()
chk_state.set(0)  # задайте проверку состояния чекбокса
chk = Checkbutton(root, text='Цифры            ', variable=chk_state,background='grey22',image=get_next_image5(),activebackground="grey22")
chk.place(x=440, y=0)
chk_state1 = IntVar()
chk_state1.set(0)  # задайте проверку состояния чекбокса
chk1 = Checkbutton(root, text='Спецсимволы', variable=chk_state1,background='grey22',image=get_next_image6(),activebackground="grey22")
chk1.place(x=440, y=35)
chk_state2 = IntVar()
chk_state2.set(1)  # задайте проверку состояния чекбокса
chk2 = Checkbutton(root, text='Отделение строки', variable=chk_state2,background='grey22',image=get_next_image7(),activebackground="grey22")
chk2.place(x=440, y=80)

Radiobutton(text="Оранжевый",var=var,value=1,bg='grey22',activebackground="grey22",command=run,image=get_next_image8()).place(x=600, y=0)
Radiobutton(text="Бирюзовый",var=var,value=2,bg='grey22',activebackground="grey22",command=run,image=get_next_image10()).place(x=600, y=35)
Radiobutton(text="Фиолетовый",var=var,value=3,bg='grey22',activebackground="grey22",command=run,image=get_next_image9()).place(x=600, y=80)

calculated_text = Text(root, height=15, width=86,fg="black",bd=0,font='Rockwell 11')


chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
chars1 = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
chars2 = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars3 = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'





def password():
    data = number_entry.get()
    data1 = length_entry.get()
    if  data.isdigit()==True and data1.isdigit()==True :
        if chk_state2.get() == 1:
            calculated_text.delete('1.0', END)
            if chk_state.get() == 1 and chk_state1.get() == 1:  # все в месте
                for n in range(int(number_entry.get())):
                    password = ''
                    for i in range(int(length_entry.get())):
                        password += random.choice(chars1)
                    calculated_text.insert(END,"Password", i + 1,":"+password + "\n")

            elif chk_state.get() == 1 and chk_state1.get() == 0:  # без спец символов
                for n in range(int(number_entry.get())):
                    password = ''
                    for i in range(int(length_entry.get())):
                        password += random.choice(chars)
                    calculated_text.insert(END,"Password", i + 1,":"+password + "\n")

            elif chk_state.get() == 0 and chk_state1.get() == 1:  # без цифр
                for n in range(int(number_entry.get())):
                    password = ''
                    for i in range(int(length_entry.get())):
                        password += random.choice(chars2)
                    calculated_text.insert(END,"Password", i + 1,":"+password + "\n")

            elif chk_state.get() == 0 and chk_state1.get() == 0:  # только буквы
                for n in range(int(number_entry.get())):
                    password = ''
                    for i in range(int(length_entry.get())):
                        password += random.choice(chars3)
                    calculated_text.insert(END,"Password", i + 1,":"+password + "\n")
        else:
            calculated_text.delete('1.0', END)
            if chk_state.get() == 1 and chk_state1.get() == 1:  # все в месте
                for n in range(int(number_entry.get())):
                    password = ''
                    for i in range(int(length_entry.get())):
                        password += random.choice(chars1)
                    calculated_text.insert(END, password + "\n")

            elif chk_state.get() == 1 and chk_state1.get() == 0:  # без спец символов
                for n in range(int(number_entry.get())):
                    password = ''
                    for i in range(int(length_entry.get())):
                        password += random.choice(chars)
                    calculated_text.insert(END, password + "\n")

            elif chk_state.get() == 0 and chk_state1.get() == 1:  # без цифр
                for n in range(int(number_entry.get())):
                    password = ''
                    for i in range(int(length_entry.get())):
                        password += random.choice(chars2)
                    calculated_text.insert(END, password + "\n")

            elif chk_state.get() == 0 and chk_state1.get() == 0:  # только буквы
                for n in range(int(number_entry.get())):
                    password = ''
                    for i in range(int(length_entry.get())):
                        password += random.choice(chars3)
                    calculated_text.insert(END, password + "\n")
    else:
        showerror("Error", "(☞ ಠ_ಠ)☞ Надо число вести(положительное)")


display_button = Button(text="Сгенерить", command=password,image=get_next_image(),background="gray22")
copy_button = Button(text='скопировать', command=copy,image=get_next_image1(),background="gray22")


number_entry = Entry(width=10, justify=CENTER)
length_entry = Entry(width=10, justify=CENTER)

number_entry.insert(0, "")
length_entry.insert(0, "")

create_name = Label(text="create by Rasul Kerimzhanov",background="gray22",foreground="white",font="impact 12")
create_name.place(x=280, y=381)

number_label = Label(text="Количество паролей",image=get_next_image3(),background="gray22")
length_label = Label(text="Длина пароля",background='gray22',image=get_next_image4())





number_label.place(x=20, y=0)
length_label.place(x=20, y=35)

number_entry.place(x=260, y=10,relwidth=0.2)
length_entry.place(x=260, y=45,relwidth=0.2)

display_button.place(x=24, y=80)
copy_button.place(x=130, y=80)


calculated_text.place(x=20, y=124)


style.configure("Vertical.TScrollbar", gripcount=0,
                background="Green", darkcolor="DarkGreen", lightcolor="LightGreen",
                troughcolor="gray", bordercolor="blue", arrowcolor="white")

hs = ttk.Scrollbar(root, orient="vertical",command=calculated_text.yview)
hs.place(x=710, y=124,relheight=.638)
calculated_text.configure(yscrollcommand=hs.set)



root.mainloop()
