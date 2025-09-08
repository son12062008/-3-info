from tkinter import *
import pyqrcode
import png
from PIL import ImageTk, Image

# ฟังก์ชันสร้าง QR Code
def create_qr_code():
    # รับข้อมูลจากช่องกรอก
    qr_name = name_entry.get()
    qr_link = link_entry.get()

    if qr_name and qr_link:
        # สร้าง QR Code จาก URL
        qr = pyqrcode.create(qr_link)

        # บันทึกเป็นไฟล์ PNG
        qr.png('qr_code.png', scale=10)

        # เปิดไฟล์ QR Code และแสดงผลใน Tkinter
        img = Image.open('qr_code.png')
        img_tk = ImageTk.PhotoImage(img)

        # แสดงภาพใน Label
        label_qr.config(image=img_tk)
        label_qr.image = img_tk  # เก็บอ้างอิงภาพไว้ใน label
    else:
        # หากกรอกข้อมูลไม่ครบ
        error_label.config(text="กรุณากรอกข้อมูลให้ครบทั้งชื่อและ URL", fg="red")

# สร้างหน้าต่างหลัก
root = Tk()
root.title("QRCode Generator")
canvas = Canvas(root, width=400, height=500)
canvas.pack()

# แสดงชื่อแอพ
app_label = Label(root, text="QRCode Generator", font=('Arial', 20, 'bold'))
canvas.create_window(200, 50, window=app_label)

# แสดง Label สำหรับชื่อคิวอาร์โค้ด
name_label = Label(root, text="ชื่อคิวอาร์โค้ด:")
canvas.create_window(100, 100, window=name_label)

# แสดง Label สำหรับ URL
link_label = Label(root, text="URL:")
canvas.create_window(100, 150, window=link_label)

# สร้าง Textbox สำหรับกรอกชื่อและ URL
name_entry = Entry(root)
canvas.create_window(200, 100, window=name_entry)

link_entry = Entry(root)
canvas.create_window(200, 150, window=link_entry)

# ปุ่มสำหรับสร้าง QR Code
button = Button(root, text="สร้างคิวอาร์โค้ด", command=create_qr_code)
canvas.create_window(200, 200, window=button)

# Label สำหรับแสดง QR Code
label_qr = Label(root)
canvas.create_window(200, 300, window=label_qr)

# Label สำหรับข้อความผิดพลาด
error_label = Label(root, text="", font=('Arial', 10, 'italic'))
canvas.create_window(200, 400, window=error_label)

# เริ่มต้นโปรแกรม
root.mainloop()
