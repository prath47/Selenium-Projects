from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

class Func():
    def book(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.goindigo.in/")
        driver.maximize_window()
        driver.find_element(By.XPATH , "//span[@id='salePopupCloseBtn']").click()
        time.sleep(5)
        driver.switch_to.frame(driver.find_element(By.XPATH , '//*[@id="cx-iframe"]'))
        driver.find_element(By.XPATH , "//i[@class='ri-subtract-line']").click()

        driver.switch_to.default_content()
        book_button = driver.find_element(By.XPATH , '//*[@id="skyplus6e-header"]/div[1]/div[5]/div/nav/ul/li[1]/a[1]')
        print(book_button.text)
        achain_button = ActionChains(driver)
        achain_button.move_to_element(book_button).perform()
        driver.find_element(By.XPATH , '//*[@id="skyplus6e-header"]/div[1]/div[5]/div/nav/ul/li[1]/div/ul/li[1]/a').click()

        from_city = driver.find_element(By.XPATH , "//input[@placeholder='From']")
        from_city.send_keys("prayag")
        from_city.send_keys(Keys.ENTER)
        to_city = driver.find_element(By.XPATH, "//input[@placeholder='To']")
        to_city.send_keys("pune")
        to_city.send_keys(Keys.ENTER)
        driver.quit()


Book_the_ticket = Func()
Book_the_ticket.book()
