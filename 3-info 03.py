# รับค่าอุณหภูมิเป็นองศาเซลเซียส
celsius = float(input("ป้อนอุณหภูมิ (องศาเซลเซียส): "))

# คำนวณองศาฟาเรนไฮต์
fahrenheit = (9/5) * celsius + 32

# คำนวณเคลวิน
kelvin = celsius + 273.15

# แสดงผลลัพธ์
print(f"องศาฟาเรนไฮต์: {fahrenheit:.2f}")
print(f"องศาเคลวิน: {kelvin:.2f}")
