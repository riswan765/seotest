import time, random, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def run_bot():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--proxy-server=socks5://127.0.0.1:8081')
    
    # Render butuh install ini otomatis
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get("http://loadtiktok.wuaze.com")
        print(f"[+] Render Gacor! [{time.strftime('%H:%M:%S')}]")
        time.sleep(random.randint(60, 90))
    finally:
        driver.quit()

if __name__ == "__main__":
    while True:
        run_bot()
        
