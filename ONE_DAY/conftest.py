# conftest.py
import pytest
from playwright.sync_api import sync_playwright

# @pytest.fixture 标记这个函数是一个"夹具"
# scope="function" 表示每个测试用例执行前，都会跑一遍这个夹具
@pytest.fixture(scope="function")
def browser_page():
    print("\n[管家]：正在为您启动浏览器...")
    with sync_playwright() as p:
        # 1. 启动操作
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        # 2. yield 关键字是分水岭
        # yield 之前的代码是"前置操作"（测试开始前执行）
        # yield 之后的代码是"后置操作"（测试结束后执行）
        yield page 
        
        # 3. 清理操作
        print("\n[管家]：测试结束，正在清理现场...")
        context.close()
        browser.close()