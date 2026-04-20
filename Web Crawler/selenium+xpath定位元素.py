from selenium import webdriver
import time
from package import SAVEPATH

driver = webdriver.Edge()

driver.get('https://passport.lanqiao.cn/login/?action=login&dialog=0&usertype=0&auth_type=login&from=shiyan&backurl=https%3A%2F%2Fwww.lanqiao.cn%2Fusers%2F3099586%2F')
# time.sleep(1)


#time.sleep(1) 强制等待

#driver.implicitly_wait(19)隐式等待，加载页面时会等待，直到页面加载完成或者达到指定的时间（19秒）为止

#显式等待，可以等待某个条件，较高级
"""
from selenium.webdriver.suppoert import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

WebDriverWait(driver, 10,0.2).until(
    EC.visibility_of_element_located((by='xpath', value='//span[normalize-space(text())="手机登录"]'))
    #等待页面上某个元素可见，例如登录按钮等
    EC.element_to_be_clickable((by='xpath', value='//span[normalize-space(text())="手机登录"]')
    #等待页面上某个元素可点击，例如登录按钮等
) # 创建一个WebDriverWait对象，等待时间为10秒,每0.2秒检查一次条件是否满足

"""


driver.find_element(by='xpath', value='//span[normalize-space(text())="手机登录"]').click()#点击页面上的元素，例如登录按钮等

driver.find_element(by='xpath', value='//input[@placeholder="请输入手机号码/邮箱"]').send_keys('173')#通过xpath定位输入框并输入内容

driver.find_element(by='xpath', value='//input[@placeholder="请输入密码"]').send_keys('wana666')#通过xpath定位输入框并输入内容

driver.find_element(by='xpath', value='//button[@class="!text-18px ant-btn ant-btn-primary ant-btn-block"]').click()#点击页面上的元素，例如登录按钮等















driver.quit()#关闭浏览器,如果不关闭浏览器，程序会一直运行，占用系统资源