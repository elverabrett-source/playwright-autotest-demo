import requests
import pytest

# 定义基础url 后面可复用
BASE_URL = "https://jsonplaceholder.typicode.com"


# 准备测试数据：(用户ID, 期望的名字)
test_data = [
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch")
]

# 批量测试
@pytest.mark.parametrize("user_id, expected_name", test_data)

def test_batch_users(user_id, expected_name):
    # 发送请求
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.get(url)
    
    # 核心断言
    assert response.status_code == 200
    # 验证 API 返回的名字，和我们期望的名字是否一致
    assert response.json()['name'] == expected_name

# 获取存在的用户
def test_get_users():
    users_id = 1
    url = f"{BASE_URL}/users/{users_id}"

    # 发送请求
    print(f"正在查询用户 {users_id}...")
    response = requests.get(url)


    # 断言 1.检查响应状态码
    assert response.status_code == 200, f"期望状态码 200，实际状态码 {response.status_code}"

    # 断言 2.检查响应内容

    # 解析响应内容为json格式
    data = response.json()

    # 断言 3.检查响应内容是否包含预期的字段
    assert data['id'] == 1

    assert data['name'] == 'Leanne Graham'

    assert "@" in data['email']

    # 场景2：获取不存在的用户
def test_get_not_exist_user():
    users_id = 9999
    url = f"{BASE_URL}/users/{users_id}"

    # 发送请求
    print(f"正在查询用户 {users_id}...")
    response = requests.get(url)

    # 断言 1.检查响应状态码
    assert response.status_code == 404, f"期望状态码 404，实际状态码 {response.status_code}"




