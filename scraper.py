from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
service = Service(executable_path='C:\webdriver\chromedriver')
driver = webdriver.Chrome(options=options, service=service)

driver.get("https://www.boats.com/explore/boats/motor-yacht/")
driver.implicitly_wait(5)
ul = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div[2]/div/section[5]/div[2]/ul') 
li = ul.find_elements(By.TAG_NAME, 'li')
BOATS_BRANDS_LI = []
for i in li:
    a = i.find_element(By.TAG_NAME, 'a').get_attribute("textContent")
    BOATS_BRANDS_LI.append(a)

driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/nav/ul/li[8]').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/nav/ul/li[8]/div[2]/div[1]/div/div[2]/div[1]/form/div/div[6]/a').click()

for x in BOATS_BRANDS_LI:
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/section/form/div/section[1]/fieldset[4]/label/span[2]/span[1]/span').click()
    driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys(x)
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/section/form/div/div/button').click()
    
driver.close()
driver.quit()