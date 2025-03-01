# Importing Libraries
from selenium import webdriver;
from selenium.webdriver.chrome.service import Service;
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options;
from webdriver_manager.chrome import ChromeDriverManager;

# Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Creating the WebDriver instance
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

# Fetching the main page
wd.get("https://www.wikipedia.org/")

# Fetching the element by ID
input_element = wd.find_element(by=By.ID,value="searchInput")
input_element.send_keys("ASD")
search = wd.find_element(by=By.CLASS_NAME,value="pure-button")
wd.execute_script("arguments[0].click();",search)

# Fetching the link through link text
link_element = wd.find_element(By.PARTIAL_LINK_TEXT,value="Adaptive software development")
# Clicking the link
wd.execute_script("arguments[0].click();",link_element)

# Fetching all elements with <p> tags
p_tags = wd.find_elements(by=By.TAG_NAME,value="p")

# Extracting the text from the fetched elements
text_lines = ''
for p_tag in p_tags:
    text_lines+=p_tag.text

#print (txt_lines)
# Extracting nested elements using CSS selector
elems = wd.find_elements(By.CSS_SELECTOR,value="p > a")
# Creating the Dictionary
link_dict = {}
for ele in elems:
    link_dict[ele.text] = ele.get_attribute("href")
#print("------------------------------")    
#print (link_dict)
