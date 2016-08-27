from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Timer

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\DnG\AppData\Local\Google\Chrome\\User Data")


browser = webdriver.Chrome(executable_path='C:\software\chromedriver.exe')

def load():
    browser.get('https://gmail.com')
    print('opening gmail')

def enterUser():
    print('entering user')
    email = browser.find_element_by_id('Email')
    email.send_keys('kedar.nadkarny@gmail.com')
    email.click()
    next = browser.find_element_by_id('next')
    next.click()

def enterPassword():
    print('entering password')
    password = browser.find_element_by_id('Passwd')
    password.send_keys('YOUR_PASSWORD')
    signin = browser.find_element_by_id('signIn')
    signin.click()

def logoutGmail():
    print('logging out of gmail')
    btn = browser.find_element_by_class_name('gb_2a')
    btn.click()
    logout = browser.find_element_by_id('gb_71')
    logout.click()

def composeEmail():
    print('opening compose mail')
    composeMail = browser.find_element_by_class_name('T-I-KE')
    composeMail.click()

def contentForEmail():
    print('creating content')
    receiver = browser.find_element_by_id(':op')
    receiver.send_keys('vidhz.vasani@gmail.com')
    subject = browser.find_element_by_id(':o9')
    subject.send_keys('Greetings!')
    content = browser.find_element_by_id(':pe')
    content.send_keys('Hey Amit. This is an automatically generated email. I did not open my gmail and hit compose. I wrote a python script which does this for me and then logs out of my gmail. cool isnt it? Anyways. Take care, Have a good day!')
    print('sending email')
    send = browser.find_element_by_id(':nz')
    send.click()

def closeBrowser():
    browser.close()


# Opens the browser and loads Gmail
Timer(5.0, load).start()

# Enter email in text input
Timer(10.0, enterUser).start()

# Enter password in text input
Timer(12.0, enterPassword).start()

# Open Compose mail
compose = Timer(25.0, composeEmail).start()

# Fill contents for email
Timer(30.0, contentForEmail).start()

# Logs out of Gmail
Timer(40.0, logoutGmail).start()

# Close the browser window that the driver has focus of
Timer(50.0, closeBrowser).start()
