import yaml

def  load_config():
    with open('config.yaml', 'r' ,encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config


if __name__ == '__main__':
    config = load_config()
    print(config)
    print("用户名是：" ,config['username'])
    print("密码是：" ,config['password'])