
# AutoBing 🤖

一个基于Python和Selenium的Bing搜索自动化工具，用于模拟真实用户的搜索行为。通过随机选择关键词并控制间隔时间，帮助完成每日搜索任务或进行自动化测试。

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange)
![EdgeDriver](https://img.shields.io/badge/EdgeDriver-Latest-lightgrey)

## 功能特性 🚀
- 从`dict.txt`随机选取40个搜索词
- 全自动化的Edge浏览器控制
- 模拟人类操作（随机间隔300-360秒）
- 实时输出带时间戳的运行日志
- 防崩溃设计（自动关闭浏览器实例）

## 快速开始 🛠️

### 前置要求
- Python 3.8+
- Microsoft Edge浏览器
- [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

### 安装步骤
1. 克隆仓库
```bash
git clone https://github.com/yourusername/autobing.git
cd autobing
```

2. 安装依赖
```bash
pip install selenium
```

3. 准备EdgeDriver
- 下载与Edge浏览器版本匹配的驱动
- 将`msedgedriver.exe`放在项目目录或系统PATH路径

### 配置文件
1. 创建`dict.txt`文件，每行一个搜索词：
```text
人工智能
机器学习
GitHub技巧
...
```

2. （可选）修改脚本参数：
```python
search_terms = random.sample(all_search_terms, 40)  # 调整搜索次数
time.sleep(random.uniform(300, 360))  # 修改间隔时间
```

### 运行程序
```bash
python autobing.py
```
程序结束后按回车键退出控制台

## 注意事项 ⚠️
1. 首次运行会触发Edge浏览器安全提示，需手动允许
2. 确保网络连接稳定
3. 请遵守[Bing服务条款](https://www.microsoft.com/legal/terms-of-use)
4. 建议搭配定时任务使用（如Windows任务计划程序）

## 贡献指南 👥
欢迎提交Issue或PR！建议步骤：
1. Fork项目
2. 创建特性分支（`git checkout -b feature/awesome`）
3. 提交修改（`git commit -m 'Add awesome feature'`）
4. 推送分支（`git push origin feature/awesome`）
5. 发起Pull Request

## 许可证 📄
[MIT License](LICENSE)
