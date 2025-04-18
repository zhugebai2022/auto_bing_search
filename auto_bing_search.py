from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import random
import time
import sys
from pathlib import Path

with open('dict.txt', 'r', encoding='utf-8') as file:
    all_search_terms = [line.strip() for line in file]

def run_search():
    edge_options = Options()
    edge_options.add_argument("--headless=new")  # 新增的无头模式参数
    edge_options.add_argument("--remote-allow-origins=*")  # 新增的允许远程连接参数
    edge_options.add_argument("--disable-extensions")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    edge_options.add_argument('--log-level=3')
    
    driver = webdriver.Edge(options=edge_options)
    time.sleep(3)
    driver.refresh()
    
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
    finally:
        driver.quit()

def main():
    log_path = Path(__file__).parent / "autobing-log.txt"
    sys.stdout = open(log_path, 'w', encoding='utf-8')
    sys.stderr = sys.stdout
    sys.stdout = open('autobing-log.txt', 'w', encoding='utf-8')
    sys.stderr = sys.stdout
    global search_terms
    search_terms = random.sample(all_search_terms, 40)
    print(f"本次搜索词: {search_terms}")
    run_search()

if __name__ == '__main__':
    print("程序开始运行...")
    try:
        main()
    except Exception as e:
        print(f"运行出错: {str(e)}")
    finally:
        input("按回车键退出程序...")  # 防止程序立即关闭
