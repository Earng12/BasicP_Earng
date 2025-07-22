x = int(input("ระยะทาง : "))

if x >= 5 and x <= 50:
    print("ราคาส่ง10บาท")
elif x >= 51 and x <= 100:
    print("ราคาส่ง15บาท")
elif x >= 101 and x <= 300:
    print("ราคาส่ง25บาท")
elif x >= 301 and x <= 500:
    print("ราคาส่ง35บาท")
elif x > 500:
    print("ราคาส่ง45บาท")
else :
    print("ไม่ส่ง")