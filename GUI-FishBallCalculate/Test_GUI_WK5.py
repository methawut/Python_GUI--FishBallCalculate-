#GUI ทำโปรแกรมคำนวน (WK5)

from tkinter import *
from tkinter import ttk
from tkinter import messagebox  #กล่อง pop up เด้งขึ้นมา

GUI = Tk()
GUI.title('โปรแกรมคำนวนราคาปลา')
GUI.geometry('1000x700')



# ------------------------------------------------------------------------------------------ image
imagefile = PhotoImage(file = 'fishball.png')   #ที่อยู่ไฟล์ภาพ
# bg = PhotoImage(file = 'C:\\Python_From_Zero_uncleEngineer\\WK5\\car_fish.png')
# bg = PhotoImage(file = r'C:\Python_From_Zero_uncleEngineer\WK5\car_fish.png')

Background = Label(GUI, image = imagefile)
Background.pack()


# ------------------------------------------------------------------------------------------ text
#                    ข้อความ                   ฟอร์น, ขนาดฟอร์น
L = Label(GUI,text = 'กรุณากรอกจำนวนไม้ที่ต้องการ', font = (None,30))
L.pack()



def Cal():
    try:    #ถ้าไม่ error
        num = float(Input.get())    #นำค่าที่เก็บมาใส่ที่ตัวแปร num
        calc = num * 7.5     #ไม้ละ 7.5 บาท
        messagebox.showinfo('เสร็จสิ้นการคำนวน' , f'ลูกชิ้น {Input.get()} ไม้: ราคาทั้งหมด {calc} บาท')   #กล่อง pop up เด้งขึ้นมา

    except:     #ถ้า error
        messagebox.showinfo('กรอกผิด' , 'ต้องกรอกเป็นตัวเลขเท่านั้น')
        Input.set('')


# ------------------------------------------------------------------------------------------ Input Val
Input = StringVar() #ตัวแปลที่ใช้เก็บข้อความเวลาพิมพ์
InputBox = ttk.Entry(GUI,textvariable = Input, font = (None,20))    #ช่องกรอก input
InputBox.pack()


Enter = ttk.Button(GUI,text = 'คำนวน', command= Cal)     #ปุ่มกด ไปที่ฟังก์ชั่น "Cal"
Enter.pack(ipadx=30,ipady=20)       #ขนาดปุ่มแกน x แกน y


GUI.mainloop()