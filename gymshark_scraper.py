from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

Size = "l" # Available: s, m, l, xl, xxl
link = "https://de.gymshark.com/products/gymshark-critical-zip-joggers-olive-green"
DRIVER_PATH = r'C:\Users\olive\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

def gym_scrape(url):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(link)
    time.sleep(3)
    h1 = driver.find_element_by_tag_name('svg')
    h2 = h1.get_attribute('value')
    print(h1.tag_name)
    driver.quit()
    print(h1)
    print(h2)
    
gym_scrape(link)
    
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
options.add_argument("--window-size=1920,1200")
driver.get(link)

butts = re.compile(r"size-select_")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "size-select_s"))
    )
    soup_level1=BeautifulSoup(driver.page_source, 'html')
    soup = BeautifulSoup(soup_level1.text, "html.parser")
    soup2 = str(soup)
    
finally:
    if("instock:{}".format(Size) in soup2):
        print("Size available")
    else:
        print("Size still not available")
    driver.quit()
    
