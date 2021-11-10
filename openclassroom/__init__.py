import time
from database import connect
from setup_driver import driver
from action import login, get_cour_by_link

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
    get_cour_by_link("https://openclassrooms.com/fr/courses/5614116-go-full-stack-with-node-js-express-and-mongodb", driver)