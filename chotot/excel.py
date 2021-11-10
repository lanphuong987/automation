from hmac import new

import self
from openpyxl import Workbook

from data_scraping.open_classroom.database import connect
from get_data_from_mysql import *
from database import *
def new_wb():
    conn = connect()
    cursor = conn.cursor()
    all_contacts = get_all_from_db_HN(cursor)
    wb = Workbook()
    ws = wb.active
    ws.title = "TP HCM"
    title = ["Tên người bán", "Hãng xe", "Số điện thoại", "Nguồn", "Thành phố", "Quận"]
    ws.append(title)
    for c in all_contacts:
        contact = [c.dealer, c.brand, c.phone, c.source, c.city, c.district]
        ws.append(contact)
    wb.save("contact3.xls")
    conn.close()

new_wb()