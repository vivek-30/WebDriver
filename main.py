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

chrome = webdriver.Chrome()

chrome.get(f'https://{platform}.com')

# verify whether we are on required platfrom or not
assert platform.casefold() in chrome.title.casefold(), 'problem in opening platform'
chrome.maximize_window()

if platform == 'youtube':
    search_box = chrome.find_element_by_id('search')
elif platform in ['github','stackoverflow','google']:
    search_box = chrome.find_element_by_name('q')
else:
    print('the platform you are looking for is not in our list try something else')
    exit()

if search_box:
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    assert 'no results found' not in chrome.page_source.casefold() or 'did not match any documents' not in chrome.page_source.casefold() , "Query isn't proper"
    
chrome.close()