from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

search_box = None
search_button = None

query = input('Which thing would you like to search: ').strip().lower()
platform = input(f'From which platfrom you wanted to search {query}: ').strip().lower()

if not query or not platform:
    print('please enter required information to procced')
    exit()

driver = webdriver.Chrome()

driver.get(f'https://{platform}.com')
driver.maximize_window()

if platform == 'youtube':
    search_box = driver.find_element_by_id('search')
elif platform in ['github','stackoverflow','google']:
    search_box = driver.find_element_by_name('q')
else:
    print('the platform you are looking for is not in our list try something else')
    exit()

if search_box:
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
