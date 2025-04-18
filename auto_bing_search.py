from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import time
import sys

with open('dict.txt', 'r', encoding='utf-8') as file:
    all_search_terms = [line.strip() for line in file]

def run_search(search_terms, chrome_options):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            print(f"[{time.strftime('%H:%M:%S')}] 正在初始化浏览器驱动... (尝试 {attempt + 1}/{max_retries})")
            driver = webdriver.Chrome(options=chrome_options)
            
            try:
                for index, term in enumerate(search_terms):
                    print(f"[{time.strftime('%H:%M:%S')}] 正在遍历第 {index + 1} 个搜索词: {term}")
                    driver.get('https://cn.bing.com')
                    time.sleep(3)
                    driver.refresh()
                    search_box = driver.find_element(By.NAME, 'q')
                    search_box.send_keys(term)
                    search_box.submit()
                    time.sleep(random.uniform(300, 360))
            finally:
                driver.quit()
            break
            
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] 浏览器启动失败: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(5)
            else:
                raise

def main():
    try:
        print("开始加载配置...")
        search_terms = random.sample(all_search_terms, 40)
        
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36')
        chrome_options.add_argument('--remote-allow-origins=*')  # 添加远程连接参数

        run_search(search_terms, chrome_options)
        
    except Exception as e:
        print(f"错误: {str(e)}")
        raise

if __name__ == '__main__':
    main()
