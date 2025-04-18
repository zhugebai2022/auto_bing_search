from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import time
import sys
from pathlib import Path

with open('dict.txt', 'r', encoding='utf-8') as file:
    all_search_terms = [line.strip() for line in file]

def run_search(search_terms, chrome_options):
    print(f"[{time.strftime('%H:%M:%S')}] 正在初始化浏览器驱动...")
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
        search_terms = random.sample(all_search_terms, 40)
        print(f"[{time.strftime('%H:%M:%S')}] 已选择搜索词: {search_terms}")

        # 创建chrome配置
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--remote-allow-origins=*")
        
        run_search(search_terms, chrome_options)
        
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] 致命错误: {str(e)}")
        raise

if __name__ == '__main__':
    print("程序开始运行...")
    try:
        main()
    except Exception as e:
        print(f"运行出错: {str(e)}")
    finally:
        input("按回车键退出程序...")  # 防止程序立即关闭
