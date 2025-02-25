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
        return "No data, try again"
    
    vat = (CIF + cost_import) * 0.07
    import_duty = cost_import + vat
    
    return {
        "CIF": CIF,
        "cost_import": cost_import,
        "vat": vat,
        "import_duty": import_duty
    }

# รับข้อมูลจากผู้ใช้
cost = float(input("กรุณากรอกราคาสินค้า (บาท): "))
product_type = int(input("กรุณากรอกประเภทสินค้า (1, 2, 3, 4): "))

result = calculate_import_tax(cost, product_type)

if result == "No data, try again":
    print(result)
else:
    print("\nสวัสดีครับ")
    print(f"สินค้า ประเภทที่ {product_type} ราคา {cost:.2f} บาท")
    print(f"มีราคา CIF = {result['CIF']:.2f} บาท")
    print(f"มีภาษีอากรขาเข้า = {result['cost_import']:.2f} บาท")
    print(f"มีภาษีมูลค่าเพิ่ม = {result['vat']:.2f} บาท")
    print(f"ดังนั้นต้องชำระภาษีนำเข้า = {result['import_duty']:.2f} บาท")
