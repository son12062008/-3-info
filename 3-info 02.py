# รับค่าจากผู้ใช้
min_value = float(input("ป้อนค่าต่ำสุด: "))
max_value = float(input("ป้อนค่าสูงสุด: "))

# คำนวณค่าเฉลี่ย
average = (min_value + max_value) / 2

# แสดงผลลัพธ์แบบทศนิยม 6 ตำแหน่ง
print(f"{average:.6f}")
