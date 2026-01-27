# from playwright.sync_api import sync_playwright
import yaml
from login_page import LoginPage
# import time
import pytest


# 暂时不从 YAML 读了，为了演示参数化，直接把数据写在这里
# 格式：("账号", "密码", "期望的结果")

@pytest.mark.parametrize("username, password, expect_text", [
    ("standard_user", "secret_sauce", "inventory"),  # 成功的数据，期望网址里有 inventory
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."), # 锁定用户
    ("standard_user", "wrong_pass", "Epic sadface: Username and password do not match"), # 密码错误
])

def test_login_features(browser_page, username, password, expect_text):
    # 1. 初始化
    page = browser_page
    login_page = LoginPage(page)


# def load_config():
#     with open('config.yaml','r',encoding='utf-8') as f:
#     #     config = yaml.safe_load(f)
#     # return config
#         return yaml.safe_load(f)

# def test_login():
#     config = load_config()
#     username = config['username']
#     password = config['password']

# def test_login(browser_page):
#     page=browser_page
#     config = load_config()
   


    # with sync_playwright() as p:
    #     browser = p.chromium.launch()
    #     page = browser.new_page()

    # login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    # assert "inventory" in page.url
    
        # browser.close()
        # page.wait_for_timeout(25000)
        # page.screenshot(path='screenshot.png')
        # page.screenshot(path='screenshot.png')
        # browser.close()

    
    # 3. 智能断言 (根据期望结果的不同，进行不同的判断)
    if expect_text == "inventory":
        # 如果期望是成功，就检查网址
        assert "inventory" in page.url
    else:
        # 如果期望是失败，就检查页面上的报错文字
        # 调用刚才写的新方法
        actual_msg = login_page.get_error_msg() 
        assert expect_text in actual_msg
