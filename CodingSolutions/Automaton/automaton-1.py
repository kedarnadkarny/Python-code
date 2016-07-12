import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\DnG\AppData\Local\Google\Chrome\\User Data")
    driver = webdriver.Chrome(executable_path='C:\software\chromedriver.exe')
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, query):
    driver.get("http://www.gmail.com")
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "Email")))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME, "Email")))
        box.send_keys(query)
        button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")


if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "kedar.nadkarny")
    time.sleep(5)
    emailElem = driver.find_element_by_class_name('Email')
    #emailElem.send_keys('kedar.nadkarny')
    #driver.quit()