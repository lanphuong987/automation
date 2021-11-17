import time
from open_classroom.database import connect
from setup_driver import driver
from open_classroom.action import login, get_cour_by_link, get_all_course

conn = connect()
driver = driver()
driver.maximize_window()

connect()
# --------------------------------------------Đăng nhập-----------------------------------
if not login(driver):
    time.sleep(900)
    login(driver)
# ----------------------------------------VÒNG LẶP NGOÀI-------------------------------------------
else:
    get_all_course(driver, "Anh")