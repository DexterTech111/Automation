from selenium import webdriver
#import undetected_chromedriver as uc
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import random


username = 'preshitech'
options = webdriver.ChromeOptions()
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
]
user_agent = random.choice(user_agents)
options.add_argument(f"user-agent={user_agent}")
options.add_argument("--disable-extensions")
options.add_experimental_option("detach", True)
# Run in headless mode for automated tasks without a visible browser window
#options.add_argument("--headless")
# Maximize the Chrome window upon startup for an optimized viewport
options.add_argument("start-maximized")
# Disable Chrome extensions to ensure a clean automation environment
options.add_argument("--disable-extensions")
# Disable sandbox mode, which can be necessary in certain environments
options.add_argument('--no-sandbox')
# Disable the use of the /dev/shm shared memory space, addressing potential memory-related issues
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
stealth(
    driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)


driver.get('https://www.instagram.com/')

# Load cookies from a JSON file
with open('1.json', 'r') as cookies_file:
    cookies = json.load(cookies_file)

time.sleep(2)
# Import cookies
for cookie in cookies:
    # Remove the domain key if it exists, since it's not required for add_cookie
    if 'domain' in cookie:
        del cookie['domain']
    
    # Check and fix the sameSite attribute
    if 'sameSite' in cookie and cookie['sameSite'] not in ["Strict", "Lax", "None"]:
        del cookie['sameSite']

    # Add the cookie to the browser
    driver.add_cookie(cookie)

# Refresh the page to apply cookies
driver.refresh()

#remove notification pop up
time.sleep(1)
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
    not_now_button = driver.find_element(By.XPATH, "//button[text()='Not Now']")
    not_now_button.click()
    print("Clicked the 'Not Now' button")
except Exception as e:
    print("Timed out waiting for the 'Not Now' button")
except NoSuchElementException:
    print("'Not Now' button not found on the page")
    



#goto account
driver.get(f'https://www.instagram.com/{username}')


#click on follow
time.sleep(3)
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Follow']")))
    not_now_button = driver.find_element(By.XPATH, "//div[text()='Follow']")
    not_now_button.click()
    print("Clicked the 'Follow' button")
except Exception as e:
    print("Timed out waiting for the 'Follow' button")
except NoSuchElementException:
    print("'Follow' button not found on the page")
    
    



"""  
#click on search button
time.sleep(1)
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0_vX"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]')))
search = driver.find_element(By.XPATH, '//*[@id="mount_0_0_vX"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]')
search.click()

#search for user
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#mount_0_0_ty > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.x1dr59a3.xixxii4.x13vifvy.xeq5yr9.x1n327nk > div > div > div.x10l6tqk.x1u3tz30.x1ja2u2z > div > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1d52u69.xktsk01.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div > input")))
text_input = driver.find_element(By.CSS_SELECTOR, "#mount_0_0_ty > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.x1dr59a3.xixxii4.x13vifvy.xeq5yr9.x1n327nk > div > div > div.x10l6tqk.x1u3tz30.x1ja2u2z > div > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1d52u69.xktsk01.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div > input")
text_input.clear()
text_input.send_keys(username)
# Wait for a few seconds to observe the click action (optional)

#click on the profile
try:
    WebDriverWait(driver, 2).until( EC.presence_of_element_located((By.XPATH, ".//span[text()='{username}']")))
    element = driver.find_element(By.XPATH, ".//span[text()='precious']")
    element.click()
    print("Clicked the span element containing 'precious'")
except Exception as e:
    print("Timed out waiting for the span element")
    
    
"""  
    
time.sleep(5)

# Close the browser
#driver.quit()
