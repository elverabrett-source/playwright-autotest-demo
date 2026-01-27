class LoginPage:
    def __init__(self, page):
        # 在这里把 page 存给 self
        self.page = page
        # 在这里定义 url 变量
        self.url ='https://www.saucedemo.com/'
        # 在这里定义 3 个元素的定位符 (Selector)
        self.username_input = '#user-name'
        self.password_input = '#password'
        self.login_button = '#login-button'
        pass 

    def navigate(self):
        # 这里用 self.page 去打开 self.url
        self.page.goto(self.url)
       

    def login(self, username, password):

        # 这里用 self.page 去填入 username
        self.page.fill(self.username_input, username)
        # 这里用 self.page 去填入 password
        self.page.fill(self.password_input, password)
        # 这里用 self.page 去点击按钮
        self.page.click(self.login_button)



    def get_error_msg(self):
        # 那个红色报错框的定位符是 h3[data-test='error']
        # inner_text() 是获取元素里面的文字
        return self.page.inner_text("h3[data-test='error']")
        
        