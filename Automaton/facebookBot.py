from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Timer
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\DnG\AppData\Local\Google\Chrome\\User Data")


browser = webdriver.Chrome(executable_path='C:\software\chromedriver.exe', chrome_options=options)

def load():
    browser.get('https://www.facebook.com')
    print('loading facebook')

def openChat():
    search = browser.find_element_by_class_name("_3a-4")
    search.click()
    print('Open chat')

def findFriend():
    print('finding friend')
    message = browser.switch_to.active_element
    message.send_keys('Man')
    message.send_keys(Keys.ENTER)

def sendMessage():
    print('typing message')
    message = browser.switch_to.active_element
    message.send_keys(Keys.TAB)
    message.send_keys('Rao. Aapana kadhi aani kuthe bhetnaar next time?')

Timer(5.0, load).start()

Timer(13.0, openChat).start()

Timer(15.0, findFriend).start()

Timer(20.0, sendMessage).start()
