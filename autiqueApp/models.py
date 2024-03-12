#รับซื้อของเก่า
#พนักงาน Employee
    # --ID :: รหัสบัตรปปช
    # --Username :: ชื่อผู้ใช้
    # --Email :: Email
    # --firstName :: ชื่อจริง
    # --lastName :: นามสกุล
    # --Address :: ที่อยู่
    # --Tell :: เบอร์โทร่
    # --Password :: รหัสผ่าน (Save as Auth user)
    # Admin Added
#ลูกค้า Customer
    # --ID :: รหัสบัตรปปช Auto
    # --firstName :: ชื่อจริง
    # --lastName :: นามสกุล
    # --Address :: ที่อยู่
    # --Tell :: เบอร์โทร่
#ประเภทของ type
    # --ID :: รหัสสินค้า
    # --PricePerUnit :: ราคาสินค้าต่อน้ำหนัก
    # --totalPrice :: ราคาสินค้ารวม
    # --Amount :: จำนวน
    # --DateAdded :: วันที่เพิ่มสินค้า
#รายการรับซื้อ PurcheseOrder
    # --ID :: ไอดีรายการรับซื้อ
    # --InventoryID :: ??3
    # --Amount :: จำนวนที่ซื้อ
    # --PricePerUnit :: ราคาต่อหน่วย
    # --PriceAll :: ราคารวม
    # --Date :: วันที่รับซื้อ (ไม่ต้องกรอกมั้ย) **รอพิจารณา
    # --cus_id :: ไอดีลูกค้า (FK) **รอพิจารณาอีกที
#รายการขาย SalesOrder
    # --ID :: ไอดีรายการขาย