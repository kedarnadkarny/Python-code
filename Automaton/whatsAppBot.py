from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Timer

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\DnG\AppData\Local\Google\Chrome\\User Data")


browser = webdriver.Chrome(executable_path='C:\software\chromedriver.exe', chrome_options=options)

receive = "boom"

def load():
    browser.get('https://web.whatsapp.com')
    print('loading whatsapp')

def findFriend():
    emailElem = browser.find_element_by_class_name('input')
    emailElem.send_keys('Deepali')
    print('finding friend')


def openChat():
    title = browser.find_element_by_class_name('chat-body')
    title.click()
    print('opening chat')

def enterMessage():
    message = browser.switch_to.active_element
    #message.send_keys('Hey\nWhen are you leaving for home?')
    message.send_keys(receive)
    print('typing message')

def sendMessage():
    send = browser.find_element_by_class_name('btn-icon')
    send.click()
    print('Message sent', receive)

def findMessageTime():
    # time = browser.find_element_by_class_name('message-datetime')
    # print(time.text)
    # emojitext = browser.find_element_by_class_name('emojitext')
    emojitext = browser.find_element_by_xpath(".//*[@id='pane-side']/div/div/div/div/div/div/div[2]/div[2]/div[1]/span")
    # emojitext = browser.find_element_by_css_selector(".emojitext:last-child")
    print(emojitext.text)
    global receive
    receive = emojitext.text



Timer(5.0, load).start()

Timer(15.0, findFriend).start()

Timer(20.0, findMessageTime).start()

Timer(22.0, openChat).start()

Timer(24.0, enterMessage).start()

Timer(26.0, sendMessage).start()


