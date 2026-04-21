# //*[@class="text-base multirow-ellipsis-2"]

from ctypes.wintypes import HACCEL
from idna import decode
import requests
from lxml import etree
from selenium import webdriver
import time
from package import SAVEPATH


url = "https://rebang.today/home"
driver = webdriver.Edge()
driver.get(url)
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
#     "Referer": "https://rebang.today/"
# }
# response = requests.get(url, headers=headers)
# print(response.status_code)
# html = etree.HTML(response.content.decode())
# data_list = html.xpath()

last_height = 0
stable_count = 0
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(10)
    new_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(1)
    if new_height == last_height:
        stable_count += 1
        if stable_count >= 3:
            break
    else:
        stable_count = 0
        last_height = new_height

Html = etree.HTML(driver.page_source)
html = decode(Html)
data_list = html.xpath('//h2[contains(@class, "text-base")]')
for data in data_list:
    news = data.xpath('.//*[@class="text-base multirow-ellipsis-2"]/text()')
    print(news)


driver.close()
driver.quit()

