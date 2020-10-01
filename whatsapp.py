from selenium import webdriver
import requests
import time
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://web.whatsapp.com')
# time.sleep(30)

re = requests.get("https://api.myip.com")
re.json()
re.text