from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://strongbody.md/")

print(driver.title)
print(driver.current_url)
driver.get("https://strongbody.md/ru/catalog")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
