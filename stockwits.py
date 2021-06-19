from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which
import time

# chrome_options= Options()
# chrome_options.add_argument("--headless")

chrome_path= which("chromedriver")
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://stocktwits.com/")
time.sleep(3)

loginButton = driver.find_element_by_xpath("(//span[@class='st_9Ki_RtG st_1SuHTwr st_1jzr122'])[1]")
loginButton.click()

time.sleep(3)

emailBox= driver.find_element_by_name("login")
emailBox.send_keys("abc123@gamil.com")
time.sleep(3)

password= driver.find_element_by_name("password")
password.send_keys("abc123%")
time.sleep(3)

password.send_keys(Keys.ENTER)

time.sleep(5)
posts= ["$BABA", "$TSNP"]

for post in posts:
    feed= driver.find_element_by_xpath("//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
    feed.send_keys(post)
    time.sleep(3)

    postButton= driver.find_element_by_xpath("(//button[@class='lib_2cF8aMP lib_c4bD4Or lib_2ybS2EZ lib_3NGW_J6 lib_2q7AR4x lib_3kUdsG1 lib_3Z398za lib_2WawZPB lib_2bmVxh4 lib_3PxyMmd lib_q275ObV lib_3-XmGDP lib_12C0HKX lib_3wnZQA7'])[2]")
    postButton.click()
    time.sleep(3)





