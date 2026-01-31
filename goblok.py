import time
import random
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # PAKSA PROXY KE SSH SINGAPORE LU (Port 8081)
    chrome_options.add_argument('--proxy-server=socks5://127.0.0.1:8081')
    
    # Path Chrome di Codespaces
    chrome_options.binary_location = "/usr/bin/chromium-browser"
    
    service = Service(executable_path="/usr/bin/chromedriver")
    return webdriver.Chrome(service=service, options=chrome_options)

def run_bot():
    driver = None
    try:
        driver = get_driver()
        driver.get("http://loadtiktok.wuaze.com")
        print(f"[+] Codespace Gacor: Serangan Masuk! [{time.strftime('%H:%M:%S')}]")
        time.sleep(random.randint(60, 120)) # Nongkrong lama biar GA nyatet
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    while True:
        run_bot()
