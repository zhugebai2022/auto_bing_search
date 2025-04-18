from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import time
import sys
from pathlib import Path
import os

with open('dict.txt', 'r', encoding='utf-8') as file:
    all_search_terms = [line.strip() for line in file]

def run_search(search_terms, chrome_options):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            print(f"[{time.strftime('%H:%M:%S')}] 正在初始化浏览器驱动... (尝试 {attempt + 1}/{max_retries})")
            driver = webdriver.Chrome(options=chrome_options)
            print(f"[{time.strftime('%H:%M:%S')}] 浏览器已成功启动！")
            
            try:
                for index, term in enumerate(search_terms):
                    
                    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    print(f"[{current_time}] 正在遍历第 {index + 1} 个搜索词: {term}")
                    driver.get('https://cn.bing.com')
                    time.sleep(3)  # 每次打开必应页面后等待3秒
                    driver.refresh()  # 刷新页面
                    search_box = driver.find_element(By.NAME, 'q')
                    search_box.send_keys(term)
                    search_box.submit()
                    time.sleep(random.uniform(300, 360))
                    sys.stdout.flush()  # 强制刷新日志
            finally:
                driver.quit()
            break  # 如果成功运行，跳出重试循环
            
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] 浏览器启动失败: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(5)  # 重试前等待
            else:
                raise  # 重试次数用完后抛出异常

def main():
    try:
        # 强制初始化日志（添加时间戳验证）
        init_time = time.strftime("%Y-%m-%d %H:%M:%S")
        with open('autobing-log.txt', 'w', encoding='utf-8') as f:
            f.write(f"=== 程序启动于 {init_time} ===\n")
            f.flush()
        
        # 添加实时心跳日志
        sys.stdout = open('autobing-log.txt', 'a', encoding='utf-8')
        sys.stderr = sys.stdout
        
        print(f"[{time.strftime('%H:%M:%S')}] 开始加载配置...")  # 添加时间戳
        search_terms = random.sample(all_search_terms, 1)
        print(f"[{time.strftime('%H:%M:%S')}] 已选择搜索词: {search_terms}")

        # 创建chrome配置
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-software-rasterizer')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-setuid-sandbox')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--no-first-run')
        chrome_options.add_argument('--no-default-browser-check')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36')

        run_search(search_terms, chrome_options)
        
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] 致命错误: {str(e)}")
        raise

def is_ci_environment():
    """检查是否在CI环境中运行"""
    return os.environ.get('CI') or os.environ.get('GITHUB_ACTIONS')

if __name__ == '__main__':
    print("程序开始运行...")
    try:
        main()
    except Exception as e:
        print(f"运行出错: {str(e)}")
    finally:
        if not is_ci_environment():
            input("按回车键退出程序...")  # 仅在非CI环境下等待用户输入
        print("=== 程序执行完毕 ===")
