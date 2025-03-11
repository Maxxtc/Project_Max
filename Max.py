import tkinter as tk
from tkinter import messagebox

def calculate_import_tax(cost, product_type):
    import_rates = {"01": 0.30, "02": 0.20, "03": 0.10, "04": 0.05}
    
    if product_type not in import_rates:
        return None

    I = cost * 0.01
    F = cost * 0.10
    CIF = cost + I + F
    cost_import = CIF * import_rates[product_type]
    vat = (CIF + cost_import) * 0.07
    import_duty = cost_import + vat

    return {
        "CIF": CIF,
        "cost_import": cost_import,
        "vat": vat,
        "import_duty": import_duty
    }

def calculate_and_display():
    try:
        cost = float(cost_entry.get())
        product_type = type_entry.get().zfill(2)  # เติมเลข 0 ด้านหน้าให้เป็น 2 หลัก
        result = calculate_import_tax(cost, product_type)

        if result:
            result_text.set(f"สินค้า ประเภทที่ {product_type}\n"
                            f"ราคา {cost:.2f} บาท\n"
                            f"ราคา CIF = {result['CIF']:.2f} บาท\n"
                            f"ภาษีอากรขาเข้า = {result['cost_import']:.2f} บาท\n"
                            f"ภาษีมูลค่าเพิ่ม = {result['vat']:.2f} บาท\n"
                            f"รวมภาษีนำเข้า = {result['import_duty']:.2f} บาท")
        else:
            messagebox.showerror("ข้อผิดพลาด", "ประเภทสินค้าต้องเป็น 01, 02, 03 หรือ 04 เท่านั้น")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกราคาสินค้าและประเภทสินค้าเป็นตัวเลข")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมคำนวณภาษีนำเข้า")
root.geometry("700x500")

# ส่วนของอินพุต
tk.Label(root, text="กรอกราคาสินค้า (บาท):").pack(pady=5)
cost_entry = tk.Entry(root)
cost_entry.pack(pady=5)

# คำแนะนำประเภทสินค้า
product_info = ("ประเภทสินค้า:\n"
                "01 (30%) เช่น ชุดเสื้อผ้า รองเท้า เครื่องสำอาง น้ำหอม จักรยาน อะไหล่รถยนต์\n"
                "02 (20%) เช่น กระเป๋า โปรเจกเตอร์ เฟอร์นิเจอร์ โคมไฟ ไฟ LED\n"
                "03 (10%) เช่น อุปกรณ์อิเล็กทรอนิกส์ มีด อุปกรณ์เครื่องใช้ ของเล่น โมเดล ภาพวาด อุปกรณ์ออกกำลังกาย\n"
                "04 (5%) เช่น วิตามิน อาหารเสริม นาฬิกา แว่นตา")
tk.Label(root, text=product_info, justify="left", wraplength=650).pack(pady=5)

tk.Label(root, text="กรอกประเภทสินค้า (01, 02, 03, 04):").pack(pady=5)
type_entry = tk.Entry(root)
type_entry.pack(pady=5)

# ปุ่มคำนวณ
tk.Button(root, text="คำนวณภาษี", command=calculate_and_display).pack(pady=10)

# ส่วนแสดงผลลัพธ์
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.pack(pady=10)

# เริ่ม GUI
root.mainloop()



