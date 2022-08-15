from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--start-maximized")
service = Service(executable_path='C:\webdriver\chromedriver')
driver = webdriver.Chrome(options=options, service=service)

driver.get("https://www.boats.com/explore/boats/motor-yacht/")
driver.implicitly_wait(15)
ul = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div[2]/div/section[5]/div[2]/ul') 
li = ul.find_elements(By.TAG_NAME, 'li')
BOATS_BRANDS_LI = []
for i in li:
    a = i.find_element(By.TAG_NAME, 'a').get_attribute('href')
    BOATS_BRANDS_LI.append(a)
print(BOATS_BRANDS_LI)


driver.close()
driver.quit()