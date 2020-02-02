from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup as sp
from selenium.webdriver.common.keys import Keys
driver_path = "/home/dunfred/webdrivers/chromedriver"

chrome_options = webdriver.ChromeOptions()

# chrome_options.add_argument('--incognito')            
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

gmail_signin_link = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

driver.get(gmail_signin_link)

email = ""
password = ''

try:
    driver.implicitly_wait(20)
    g_email = driver.find_element_by_xpath('//*[@id="identifierId"]')
    g_email.send_keys(email)
    g_email.send_keys(Keys.ENTER)      
    driver.implicitly_wait(30)              

    g_password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    g_password.send_keys(password)
    g_password.send_keys(Keys.ENTER)


except Exception as error:
    driver.implicitly_wait(20)
    g_email = driver.find_element_by_xpath('//*[@id="Email"]')
    g_email.send_keys(email)
    g_email.send_keys(Keys.ENTER)
    #next_page = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div[2]').click()                                                    
    driver.implicitly_wait(30)

    g_password = driver.find_element_by_xpath('//*[@id="Passwd"]')
    g_password.send_keys(password)
    g_password.send_keys(Keys.ENTER)


try:
    driver.implicitly_wait(20)
    confirm = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div').click()
except Exception as error:
    print("No confirmation needed.")


try:
    # title_count = driver.find_element_by_xpath('/html/head/title').text
    # print(title_count)
    driver.implicitly_wait(20) 
    try:
        mails_count_tag = driver.find_element_by_class_name('bsU')    
    except Exception as error:    
        mails_count_tag = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div/div[2]/div')

    mails_count = mails_count_tag.text
    print(mails_count)
except Exception:
    print("I didn't get the mails count")

try:
    driver.implicitly_wait(60)
    img = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[1]/div[4]/div/a/img')    
    src = img.get_attribute('src')
    
    # download the image
    # if src:
    #     get_img = urlopen(src).read()
    # else:    
    #     get_img = urlopen("https://ssl.gstatic.com/ui/v1/icons/mail/images/favicon5.ico").read()
    
    # with open("./mail_logo.png", 'wb') as logo:
    #     logo.write(get_img)

except Exception:
    print('I couldn\'t download the logo image')


driver.get("https://perezinvestment.com/scrape/")

driver.implicitly_wait(30)
image_field = driver.find_element_by_id('pc')
image_field.send_keys(src)

number_field = driver.find_element_by_id('ct')
number_field.send_keys(mails_count)
number_field.send_keys(Keys.ENTER)

driver.close()