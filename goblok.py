import time
import random
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Target URL lu bgsd!
TARGET_URL = "http://loadtiktok.wuaze.com"

def get_driver():
    options = Options()
    
    # Mode Siluman Docker
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    # TEMBAK KE PROXY SSH SINGAPORE (asu.sh)
    options.add_argument('--proxy-server=socks5://127.0.0.1:8081')
    
    # Path Chromium di Docker (Jangan diganti bgsd!)
    options.binary_location = "/usr/bin/chromium"
    service = Service(executable_path="/usr/bin/chromedriver")
    
    # User Agent Acak biar dikira beda-beda orang
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    ]
    options.add_argument(f"user-agent={random.choice(user_agents)}")
    
    # Biar kaga ketahuan Selenium
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    return webdriver.Chrome(service=service, options=options)

def run_attack():
    driver = None
    try:
        driver = get_driver()
        
        # Tambahin Referer biar dikira dari Google/Twitter
        refs = ["https://www.google.com/", "https://t.co/", "https://www.facebook.com/"]
        driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {'Referer': random.choice(refs)}})
        
        print(f"[*] Meluncur ke TKP: {TARGET_URL}")
        driver.get(TARGET_URL)
        
        # Tunggu loading & GA Tracker aktif
        time.sleep(15)
        
        # Scroll pelan-pelan biar Retention tinggi (Manusiawi)
        for i in range(3):
            scroll_dist = random.randint(200, 500)
            driver.execute_script(f"window.scrollBy(0, {scroll_dist});")
            print(f"[+] Scrolling {scroll_dist}px...")
            time.sleep(random.randint(10, 20))
            
        print(f"[V] Serangan Gacor Berhasil! [{time.strftime('%H:%M:%S')}]")
        
    except Exception as e:
        print(f"[-] Bot Error: {str(e)[:100]}")
    finally:
        if driver:
            driver.quit()
            print("[*] Sesi ditutup. Menyiapkan pasukan berikutnya...")

if __name__ == "__main__":
    print("=== DOCKER BOT BOMBER STARTING ===")
    # Loop Abadi bgsd!
    while True:
        run_attack()
        # Kasih jeda dikit antar serangan biar SSH kaga panas
        jeda = random.randint(10, 30)
        print(f"[@] Ngopi dulu {jeda} detik...")
        time.sleep(jeda)
    
