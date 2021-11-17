from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

def driver():
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('ignore-certificate-errors')
    chrome_option.add_argument("--disable-infobars")
    chrome_option.add_argument("start-maximized")
    chrome_option.add_argument("--disable-extensions")
    chrome_option.add_argument("start-maximized")
    chrome_option.add_argument("enable-automation")
    chrome_option.add_argument("--no-sandbox")
    chrome_option.add_argument("--disable-dev-shm-usage")
    chrome_option.add_argument("--disable-browser-side-navigation")
    chrome_option.add_argument("--disable-gpu")
    chrome_option.accept_untrusted_certs = True
    s = Service(executable_path=".\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=chrome_option)
    return driver


