from requests import options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options


def driver():
    option = webdriver.ChromeOptions()
    option.add_argument('--no-sandbox')
    option.add_argument("--headless")
    option.add_argument('--disable-dev-shm-usage')
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s, options=option)
    browser.maximize_window()
    return browser
