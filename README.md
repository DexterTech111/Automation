# Instagram Automation Script

This repository contains a Python script that automates interactions with Instagram using Selenium and the `selenium-stealth` library. The script is designed to log into Instagram, load cookies to bypass login, and perform actions such as following a user.

## Features

- **Browser Automation:** Uses Selenium WebDriver to automate browser interactions.
- **Stealth Mode:** Uses `selenium-stealth` to avoid detection by Instagram.
- **Cookie Management:** Loads cookies from a JSON file to bypass the login process.
- **Automated Actions:** Automatically handles pop-ups and follows a specified user.
- **Auto Follow:** Searches for a specif user and follow the proifile

## Requirements

- Python 3.x
- Google Chrome
- ChromeDriver (compatible with your Chrome version)
- `selenium` library
- `selenium-stealth` library

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/instagram-automation.git
    cd instagram-automation
    ```

2. **Install the required Python libraries:**

    ```sh
    pip install selenium selenium-stealth
    ```

3. **Download ChromeDriver:**

    Download the ChromeDriver that matches your installed version of Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Place the `chromedriver` executable in a directory that is included in your system's PATH.

## Usage

1. **Prepare the cookies:**

    - Log in to Instagram manually in your browser.
    - Export the cookies to a file named `1.json` in the repository directory. You can use browser extensions like "EditThisCookie" to export cookies.

2. **Edit the script:**

    - Update the `username` variable in the script with the Instagram username you want to follow.

3. **Run the script:**

    ```sh
    python instagram_automation.py
    ```

## Script Explanation

Here's a step-by-step explanation of what the script does:

### 1. Imports necessary libraries:

```python
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import random
```

### 2. Set up user agent and Chrome options:
```
options = webdriver.ChromeOptions()
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
]
user_agent = random.choice(user_agents)
options.add_argument(f"user-agent={user_agent}")
options.add_argument("--disable-extensions")
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
```

### 3. Initialize the WebDriver with stealth settings:

```
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
```

### 4. Open Instagram and load cookies:

```
driver.get('https://www.instagram.com/')
with open('1.json', 'r') as cookies_file:
    cookies = json.load(cookies_file)
time.sleep(2)
for cookie in cookies:
    if 'domain' in cookie:
        del cookie['domain']
    if 'sameSite' in cookie and cookie['sameSite'] not in ["Strict", "Lax", "None"]:
        del cookie['sameSite']
    driver.add_cookie(cookie)
driver.refresh()
```


### 5. Handle pop-ups and navigate to the user's profile:

```
time.sleep(1)
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
    not_now_button = driver.find_element(By.XPATH, "//button[text()='Not Now']")
    not_now_button.click()
except Exception as e:
    print("Timed out waiting for the 'Not Now' button")
except NoSuchElementException:
    print("'Not Now' button not found on the page")

driver.get(f'https://www.instagram.com/{username}')
```

### 6. Follow the user:
```
time.sleep(3)
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Follow']")))
    follow_button = driver.find_element(By.XPATH, "//div[text()='Follow']")
    follow_button.click()
except Exception as e:
    print("Timed out waiting for the 'Follow' button")
except NoSuchElementException:
    print("'Follow' button not found on the page")
```

## Notes
Ensure you comply with Instagram's terms of service and usage policies when using this script.
Use this script responsibly and avoid spamming or automating excessive actions, as this could lead to your account being flagged or banned.


## License
This project is licensed under the `MIT License` - see the LICENSE file for details.
