

# import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
# from config import *
from urllib.parse import quote

# browser = webdriver.Chrome()
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)

url = 'https://login.taobao.com/member/login.jhtml'
weibo_username = ""  # 改成你的微博账号
weibo_password = ""  # 改成你的微博密码

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches',
                                ['enable-automation'])
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Chrome()

wait = WebDriverWait(browser, 10)
# client = pymongo.MongoClient(MONGO_URL)
# db = client[MONGO_DB]

KEYWORD = 'iPad'
MAX_PAGE = 100

def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        # save_to_mongo(product)


# def save_to_mongo(result):
#     """
#     保存至MongoDB
#     :param result: 结果
#     """
#     try:
#         if db[MONGO_COLLECTION].insert(result):
#             print('存储到MongoDB成功')
#     except Exception:
#         print('存储到MongoDB失败')

def auto_login():

    # 打开网页
    # 等待 密码登录选项 出现
    password_login = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
    password_login.click()

    # 等待 微博登录选项 出现
    weibo_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.submit')))
    weibo_login.click()

    # 等待 微博账号 出现
    weibo_user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.username-field > .W_input')))
    weibo_user.send_keys(weibo_username)

    # 等待 微博密码 出现
    weibo_pwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.password-field > .W_input')))
    weibo_pwd.send_keys(weibo_password)

    # 等待 登录按钮 出现
    submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_tip > a > span')))
    submit.click()

    # 直到获取到淘宝会员昵称才能确定是登录成功
    taobao_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                  '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))
    # 输出淘宝昵称
    print("登陆成功" + taobao_name.text)


def main():
    """
    遍历每一页
    """
    # auto_login()
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    browser.close()


if __name__ == '__main__':
    main()

