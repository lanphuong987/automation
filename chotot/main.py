from setup_driver import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from excel import *
import time
contact = []
conn = connect()
driver = driver()
cursor = conn.cursor()


def get_all_contact():
    page_number = 6
    driver.get("https://xe.chotot.com/mua-ban-oto-moi-binh-duong-sdca2?page=" + str(page_number))
    while True:
        time.sleep(3)
        contacts = []
        contacts_from_db = get_all_phone_from_db(cursor)
        contacts_from_web = []
        car_details = WebDriverWait(driver, 15).until(
                        EC.visibility_of_all_elements_located((By.CLASS_NAME,
                                                          "AdItem_adItem__2O28x")))
        href = []
        for detail in car_details:
            href.append(detail.get_attribute('href'))
        for url in href:
            driver.get(url)
            try:
                money = WebDriverWait(driver, 3).until(
                            EC.element_to_be_clickable(
                                (By.XPATH, "//img[@src='https://static.chotot.com/storage/assets/ESCROW/escrow_protected_deposit.png']")))
                button_show_phone = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//body/div[@id='__next']/div/div/div/div/div/div/div[3]/div[1]/div[1]")))
                ActionChains(driver).move_to_element(button_show_phone).click(button_show_phone).perform()
                time.sleep(1)
                phone_number = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='sc-EHOje lnlbMI']//span"))).text
            except:
                try:
                    button_show_phone = WebDriverWait(driver, 20).until(
                                EC.element_to_be_clickable(
                                    (By.XPATH, "//body/div[@id='__next']/div/div/div/div/div/div/div[2]/div[1]")))
                    ActionChains(driver).move_to_element(button_show_phone).click(button_show_phone).perform()
                    time.sleep(1)
                    phone_number = WebDriverWait(driver, 20).until(
                                EC.presence_of_element_located((By.XPATH, "//div[@class='sc-EHOje lnlbMI']//span"))).text
                except:
                    button_show_phone = WebDriverWait(driver, 20).until(
                                EC.element_to_be_clickable(
                                    (By.XPATH, "//body/div[@id='__next']/div/div/div/div/div/div/div[2]/div[1]")))
                    ActionChains(driver).move_to_element(button_show_phone).click(button_show_phone).perform()
                    time.sleep(1)
                    phone_number = WebDriverWait(driver, 20).until(
                                EC.presence_of_element_located((By.XPATH, "//div[@class='sc-EHOje lnlbMI']//span"))).text
            if phone_number not in contacts_from_web and (phone_number not in contacts_from_db or not contacts_from_db):
                contacts_from_web.append(phone_number)
                dictrict = WebDriverWait(driver, 20).until(
                                EC.presence_of_element_located((By.XPATH, "//div[@class='row']//li[4]"))).text
                costumer_name = WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.XPATH, "//a[@target='_blank']//div[1]//div[1]//b"))).text
                dictrict = dictrict[dictrict.rfind("Quận") + 5: len(dictrict)]
                try:
                    branch_name = WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.XPATH, "//span[@itemprop='carbrand']"))).text
                except:
                    branch_name = ""
                user = Contact(costumer_name, branch_name, phone_number, "chotot", "Bình Dương", dictrict)
                contacts.append(user)
        for c in contacts:
            insert_contact(c)
        contacts.clear()
        contacts_from_web.clear()
        if contacts_from_db:
            contacts_from_db.clear()
        page_number = page_number + 1
        print(page_number)
        driver.get("https://xe.chotot.com/mua-ban-oto-moi-binh-duong-sdca2?page=" + str(page_number))

def set_location(city_name, dictrict_name):
    driver.get("https://xe.chotot.com/mua-ban-oto-moi-sdca2")
    select_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='button']//span[contains(text(),'Tp Hồ Chí Minh')]")))
    select_box.click()
    if city_name != '':
        city = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='ChoTot Modal']//div//div//div//div//ul")))
        for c in city:
            if city_name in c.text:
                ActionChains(driver).move_to_element(c).click(c).perform()
                time.sleep(3)
    if city_name != '' and dictrict_name!= "":
        distric = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='ChoTot Modal']//div//div//div//div//ul")))
        for c in distric:
            if distric in c.text:
                ActionChains(driver).move_to_element(c).click(c).perform()
                time.sleep(3)

connect()
get_all_contact()