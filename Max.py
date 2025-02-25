import tkinter as tk
from tkinter import messagebox

def calculate_import_tax(cost, product_type):
    if product_type == 1:
        I = cost * 0.01
        F = cost * 0.10
        CIF = cost + I + F
        cost_import = CIF * 0.30
    elif product_type == 2:
        I = cost * 0.01
        F = cost * 0.10
        CIF = cost + I + F
        cost_import = CIF * 0.20
    elif product_type == 3:
        I = cost * 0.01
        F = cost * 0.10
        CIF = cost + I + F
        cost_import = CIF * 0.30
    elif product_type == 4:
        I = cost * 0.01
        F = cost * 0.10
        CIF = cost + I + F
        cost_import = CIF * 0.30
    else:
        return None

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
        product_type = int(type_entry.get())
        result = calculate_import_tax(cost, product_type)

        if result:
            result_text.set(f"สินค้า ประเภทที่ {product_type}\n"
                            f"ราคา {cost:.2f} บาท\n"
                            f"ราคา CIF = {result['CIF']:.2f} บาท\n"
                            f"ภาษีอากรขาเข้า = {result['cost_import']:.2f} บาท\n"
                            f"ภาษีมูลค่าเพิ่ม = {result['vat']:.2f} บาท\n"
                            f"รวมภาษีนำเข้า = {result['import_duty']:.2f} บาท")
        else:
            messagebox.showerror("ข้อผิดพลาด", "ประเภทสินค้าต้องเป็น 1, 2, 3 หรือ 4 เท่านั้น")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกราคาสินค้าและประเภทสินค้าเป็นตัวเลข")


# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมคำนวณภาษีนำเข้า")
root.geometry("500x400")

# ส่วนของอินพุต
tk.Label(root, text="กรอกราคาสินค้า (บาท):").pack(pady=5)
cost_entry = tk.Entry(root)
cost_entry.pack(pady=5)


tk.Label(root, text="กรอกประเภทสินค้า (1, 2, 3, 4):").pack(pady=5)
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


