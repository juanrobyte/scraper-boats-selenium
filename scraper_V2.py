from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

PROXY = "185.199.228.220:7300"

options = Options()
options.add_argument("--proxy-server=%s" % PROXY)
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
service = Service(executable_path='C:\webdriver\chromedriver')
driver = webdriver.Chrome(options=options, service=service)
driver.get('https://www.boats.com/explore/overnight-cruising/')
container = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div[2]/div/section[1]/div[3]')
items = container.find_elements(By.CLASS_NAME, 'showcase-grid__item')
boat_li = []

forSale = open("forSale.csv" ,"w", encoding='utf-8')
forSale.write("name, make, model, condition, price, title, class, lenght, fuel type, hull material, location, LOA, beam, max. draft, min draft, keel type, displacement, max bridge clearance, engine type, engine make, designer, cabins, singer berths, fuel tanks, fresh water tanks, holding tanks, hull shape")

onlyDesc = open("onlyDesc.csv", "w", encoding='utf-8')
onlyDesc.write("name, price, year, type, class, lenght, hull material, LOA, lenght on deck, beam, max draft, dry weight, max bridge clearance, number of engines, engine type, engine make, engine mode, power, cabins, fuel tanks, fresh water tanks, holding tanks, hull shape")


def search():
        try:
            ol = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div[1]/div/section[2]/div[1]/ol')
            print('yes')
            li = ol.find_elements(By.TAG_NAME, 'li')
            for z in li:
                try:
                    div = z.find_element(By.TAG_NAME, 'div')
                    link_boat = div.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    boat_li.append(link_boat)
                    print('Find')
                except:
                    print('Empty')

        except NoSuchElementException:
            print('not')
            ol = driver.find_element(By.XPATH, '//*[@id="listings-srp"]/ol')
            li = ol.find_elements(By.TAG_NAME, 'li')
            for z in li:
                try:
                    div = z.find_element(By.TAG_NAME, 'div')
                    link_boat = div.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    boat_li.append(link_boat)
                    print('Find')
                except:
                    print('Empty')
                        
def search2():
    while True:
        try:    
            search()
            x = driver.find_element(By.XPATH, '//*[@id="search-results"]/div[2]/a[2]').get_attribute('href')
            driver.get(x)
        except NoSuchElementException:
            print('Finish')
            break                       



with open("./links.txt", 'w+', encoding='utf-8') as f:
    for a in items:
            links = a.find_element(By.CLASS_NAME, 'c-tile__main-link').get_attribute('href')
            f.write(links)
            f.write('\n')
with open("./links.txt", 'r', encoding='utf-8') as f:
    with open("./ignore.txt", "r", encoding='utf-8') as f2:
        difference = set(f).difference(f2)
with open("./results.txt", "w+", encoding='utf-8') as f3:
    for line in difference:
        f3.write(line)
        
with open('./results.txt', 'r', encoding='utf-8') as f4:
     final_links = [line.strip() for line in f4]
     for x in final_links:
        driver.get(x)
        driver.find_element(By.CLASS_NAME, 'o-view-all-results').click()
        driver.find_element(By.ID, 'list-view-js').click()
        search()
        y = driver.find_element(By.XPATH, '//*[@id="search-results"]/div[2]/a').get_attribute('href')
        driver.get(y)
        search2()
        


                      
result_boat_li = []
for element in boat_li: 
    if element not in result_boat_li:
        result_boat_li.append(element)

specifications_boats = []

def regexing(c):
    c = c.replace(',', '.')
    c = c.replace('|', '')
    c = c.replace('/', '')
    return c 

for info in result_boat_li:
    driver.get(info)
    try:
        title = regexing( driver.find_element(By.XPATH, '//*[@id="description"]/div/div[2]/h2').text )
        price = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/dl/div[1]/dd/a').text)
        year = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/dl/div[2]/dd').text)
        atype = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/dl/div[3]/dd').text)
        aclass = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/dl/div[4]/dd').text)
        alenght = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/dl/div[5]/dd').text)
        hullMaterial = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/dl/div[6]/dd').text)
        loa = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[1]/div[1]/dd').text)
        lod = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[1]/div[2]/dd').text)
        beam = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[1]/div[3]/dd').text)
        maxDraft = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[1]/div[4]/dd').text)
        dryWeight = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[1]/div[5]/dd').text)
        maxBridge = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[1]/div[6]/dd').text)
        noe = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[2]/div[1]/dd').text)
        engineType = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[2]/div[2]/dd').text)
        engineMake = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[2]/div[3]/dd').text)
        engineMode = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[2]/div[4]/dd').text)
        power = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[2]/div[5]/dd').text)
        cabins = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[3]/div/dd').text)
        fuelTanks = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[4]/div[1]/dd').text)
        fwt = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[4]/div[2]/dd').text)
        holdingTanks = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[4]/div[3]/dd').text)
        hullShape = regexing(driver.find_element(By.XPATH, '//*[@id="specifications"]/div/div[1]/div/div/dl[5]/div/dd').text)
        
        onlyDesc.write(title + ',' + price + ',' + year + ',' + atype + ',' + aclass + ',' + alenght + ',' + hullMaterial + ',' + loa + ',' + lod + ',' + beam + ',' + maxDraft + ',' + dryWeight + ',' + maxBridge + ',' + noe + ',' + engineType + ',' + engineMake + ',' + engineMode + ',' + power + ',' + cabins + ',' + fuelTanks + ',' + fwt + ',' + fuelType + ',' + holdingTanks + ',' + hullShape)
        onlyDesc.write('\n')
        onlyDesc.close()
         
        
    except NoSuchElementException:        
        title = regexing(driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[1]/div/section/header/div/h1').text)
        make = regexing(driver.find_element(By.XPATH, '//*[@id="boat-details"]/div[2]/table/tbody/tr[1]/td').text)
        model = regexing(driver.find_element(By.XPATH, '//*[@id="boat-details"]/div[2]/table/tbody/tr[2]/td').text)
        year = regexing(driver.find_element(By.XPATH, '//*[@id="boat-details"]/div[2]/table/tbody/tr[3]/td').text)
        condition = regexing(driver.find_element(By.XPATH, '//*[@id="boat-details"]/div[2]/table/tbody/tr[4]/td').text)
        price = regexing(driver.find_element(By.XPATH, '//*[@id="boat-details"]/div[2]/table/tbody/tr[5]/td').text)
        atype = regexing(driver.find_element(By.XPATH, '//*[@id="boat-details"]/div[2]/table/tbody/tr[6]/td').text)
        aclass = regexing(driver.find_element(By.XPATH, '//*[@id="boat-details"]/div[2]/table/tbody/tr[7]/td').text)
        alenght = regexing(driver.find_element(By.XPATH, '//*[@id="boat-details"]/div[2]/table/tbody/tr[8]/td').text)
        fuelType = regexing(driver.find_element(By.XPATH, '//*[@id="boat-details"]/div[2]/table/tbody/tr[9]/td').text)
        hullMaterial = regexing(driver.find_element(By.XPATH, '//*[@id="boat-details"]/div[2]/table/tbody/tr[10]/td').text)
        location = regexing(driver.find_element(By.XPATH, '//*[@id="boat-details"]/div[2]/table/tbody/tr[11]/td').text)
        loa = regexing(driver.find_element(By.XPATH, '//*[@id="measurements"]/div[2]/table/tbody/tr[1]/td').text)
        beam = regexing(driver.find_element(By.XPATH, '//*[@id="measurements"]/div[2]/table/tbody/tr[2]/td').text)
        maxDraft = regexing(driver.find_element(By.XPATH, '//*[@id="measurements"]/div[2]/table/tbody/tr[3]/td').text)
        minDraft = regexing(driver.find_element(By.XPATH, '//*[@id="measurements"]/div[2]/table/tbody/tr[4]/td').text)
        keelType = regexing(driver.find_element(By.XPATH, '//*[@id="measurements"]/div[2]/table/tbody/tr[5]/td').text)
        displacement = regexing(driver.find_element(By.XPATH, '//*[@id="measurements"]/div[2]/table/tbody/tr[6]/td').text)
        mbc = regexing(driver.find_element(By.XPATH, '//*[@id="measurements"]/div[2]/table/tbody/tr[7]/td').text)
        engineType = regexing(driver.find_element(By.XPATH, '//*[@id="propulsion"]/div[2]/table/tbody/tr[1]/td').text)
        engineMake = regexing(driver.find_element(By.XPATH, '//*[@id="propulsion"]/div[2]/table/tbody/tr[2]/td').text)
        designer = regexing(driver.find_element(By.XPATH, '//*[@id="other-specs"]/div[2]/table/tbody/tr[1]/td').text)
        cabins = regexing(driver.find_element(By.XPATH, '//*[@id="other-specs"]/div[2]/table/tbody/tr[2]/td').text)
        singerBerths = regexing(driver.find_element(By.XPATH, '//*[@id="other-specs"]/div[2]/table/tbody/tr[3]/td').text)
        fuelTanks = regexing(driver.find_element(By.XPATH, '//*[@id="other-specs"]/div[2]/table/tbody/tr[4]/td').text)
        fwt = regexing(driver.find_element(By.XPATH, '//*[@id="other-specs"]/div[2]/table/tbody/tr[5]/td').text)
        holdingTanks = regexing(driver.find_element(By.XPATH, '//*[@id="other-specs"]/div[2]/table/tbody/tr[6]/td').text)
        hull = regexing(driver.find_element(By.XPATH, '//*[@id="other-specs"]/div[2]/table/tbody/tr[7]/td').text)
        
        forSale.write(title + ',' + make + ',' + model + ',' + year + ',' + condition + ',' + atype + ',' + aclass + ',' + alenght + ',' + fuelType + ',' + hullMaterial + ',' + location + ',' + loa + ',' + beam + ',' + maxDraft + ',' + dryWeight + ',' + maxBridge + ',' + minDraft + ',' + keelType + ',' + displacement + ',' + mbc + ',' + engineType + ',' + engineMake + ',' + designer + ',' + cabins + ',' + singerBerths + ',' + fuelTanks + ',' + fwt + ',' + holdingTanks + ',' + hull)
        forSale.write('\n')
        forSale.close()


        
driver.close()
driver.quit()
