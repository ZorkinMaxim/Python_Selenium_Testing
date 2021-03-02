import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://strongbody.md/")
driver.find_element_by_css_selector("input[name='q']").send_keys("whey")
driver.find_element_by_css_selector(".s_btn").click()
driver.find_element_by_xpath("//a[@href='https://strongbody.md/ru/catalog/100-whey-gold-standard-227-kg']").click()
driver.find_element_by_css_selector(".jq-selectbox__trigger-arrow").click()
driver.find_element_by_xpath("//div[@class='jq-selectbox__dropdown']/ul/li[3]").click()
driver.find_element_by_css_selector(".more").click()
driver.find_element_by_class_name("buy").click()
driver.find_element_by_xpath("//a[@href='https://strongbody.md/ru/cart']").click()
driver.find_element_by_name("name").send_keys("Test")
driver.find_element_by_name("city").send_keys("Abracacity")
driver.find_element_by_name('phone').send_keys('007')
driver.find_element_by_name('address').send_keys('Самая лучшая улица')
driver.find_element_by_name('email').send_keys('abra@gmail.com')
driver.find_element_by_css_selector("input[value='Заказать']").click()

