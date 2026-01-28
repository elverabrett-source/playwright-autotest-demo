import requests

def run_get_request():
    # --- 这个网站，它非常友好，不会随便封号 ---
    url = "https://jsonplaceholder.typicode.com/users/1"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    print(f"正在发送 GET 请求到: {url}")
    
    # 发送请求
    response = requests.get(url, headers=headers)
    
    print("状态码:", response.status_code)
    
    if response.status_code == 200:
        data = response.json()
        print("响应内容:", data)
        # 这个网站返回的数据结构里，email 就在最外层，或者在嵌套里
        print("提取到的名字:", data['name'])
        print("提取到的邮箱:", data['email'])
    else:
        print("还是失败了...")
        print("报错信息:", response.text)

if __name__ == "__main__":
    run_get_request()