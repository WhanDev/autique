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
#ประเภทของค้า(แก้ว, พลาสติก, etc)
    # --ID :: รหัสสินค้า
    # --ProductName :: ชื่อสินค้า
    # --PriceRateReceive :: เรตราคารับ
    # --PriceRateSend :: เรตราคาส่ง
#สินค้าคงคลัง InventoryStock
    # --ID :: รหัสสินค้าคงคลัง
    # --IDProductFK :: รหัสสินค้า(FK)
    # --TotalAmount :: จำนวนรวม (น้ำหนัก)
#รายการรับซื้อ PurcheseOrder
    # --ID :: ไอดีรายการรับซื้อ
    # --IDProductFK :: รหัสสินค้า(FK)
    # --Amount :: จำนวนที่ซื้อ
    # --Price :: ราคารวม
    # --Date :: วันที่รับซื้อ (ไม่ต้องกรอกมั้ย)
    # --cus_id :: ไอดีลูกค้า (FK) **รอพิจารณาอีกที
#รายการขาย SalesOrder
    # --ID :: ไอดีรายการขาย
    # --IDProductFK :: รหัสสินค้า(FK)
    # --Amount :: จำนวนที่ซื้อ
    # --Price :: ราคารวม
    # --Date :: วันที่รับซื้อ (ไม่ต้องกรอกมั้ย)
    # --cus_id :: ไอดีลูกค้า (FK) **รอพิจารณาอีกที