from tkinter import *
from tkinter import messagebox
# package ส่ง line
from songline import Sendline
# package csv
import csv
from datetime import datetime

#function csv
def writecsv(record_list):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(record_list)

token = 'mGrBkxC4HCyprxKrWPtzrnv5fvRuPzfpWdP9nC3ppGv'
messenger = Sendline(token)

GUI = Tk()

GUI.title('โปรแกรมซ่อมบำรุง by Highvolt')
GUI.geometry('500x500+50+50')

FONT1 = ('Angsana New', 20, 'bold')
FONT2 = ('Angsana New', 15)


L = Label(GUI, text='ใบแจ้งซ่อม',font=FONT1)
L.pack()


L = Label(GUI, text='ชื่อผู้แจ้ง',font=FONT2)
L.place(x=30,y=50)
v_name = StringVar() #ตัวแปรพิเศษใช้กับ GUI
E1 = Entry(GUI,textvariable=v_name,font=FONT2)
E1.place(x=150,y=50)

L = Label(GUI, text='แผนก',font=FONT2)
L.place(x=30,y=100)
v_department = StringVar()
E2 = Entry(GUI,textvariable=v_department,font=FONT2)
E2.place(x=150,y=100)


L = Label(GUI, text='ชนิดอุปกรณ์',font=FONT2)
L.place(x=30,y=150)
v_machine = StringVar()
E3 = Entry(GUI,textvariable=v_machine,font=FONT2)
E3.place(x=150,y=150)

L = Label(GUI, text='อาการเสีย',font=FONT2)
L.place(x=30,y=200)
v_problem = StringVar()
E4 = Entry(GUI,textvariable=v_problem,font=FONT2)
E4.place(x=150,y=200)

L = Label(GUI, text='หมายเลขเครื่อง',font=FONT2)
L.place(x=30,y=250)
v_number = StringVar()
E5 = Entry(GUI,textvariable=v_number,font=FONT2)
E5.place(x=150,y=250)

L = Label(GUI, text='เบอร์โทรผู้แจ้ง',font=FONT2)
L.place(x=30,y=300)
v_tel = StringVar()
E6 = Entry(GUI,textvariable=v_tel,font=FONT2)
E6.place(x=150,y=300)

def save():
    name = v_name.get() #.get คือการดึงค่าออกมาจ่ก StringVar
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_number.get()
    tel = v_tel.get()

    text = 'ชื่อผู้แจ้ง: ' + name + '\n'
    text = text + 'แผนก: ' + department + '\n'
    text = text + 'อุปกรณ์: ' + machine + '\n'
    text = text + 'อาการเสีย: ' + problem + '\n'
    text = text + 'หมายเลขเครื่อง: ' + number + '\n'
    text = text + 'โทร: ' + tel + '\n'

    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datalist = [dt,name,department,machine,problem,number,tel]
    writecsv(datalist)

    messenger.sendtext(text)

    messagebox.showinfo('กำลังบันทึกข้อมูล...',text)

B = Button(GUI, text='บันทึกใบแจ้งซ่อม',command=save)
B.place(x=200,y=350)

GUI.mainloop()
