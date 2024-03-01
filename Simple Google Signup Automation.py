from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

class Func():
    def fill_the_form(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.google.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH,  '//*[@id="gb"]/div/div[2]/a/span').click()
        driver.find_element(By.XPATH , "//span[normalize-space()='Dismiss']").click()
        # driver.find_element(By.XPATH , "//input[@id='identifierId']").send_keys("email")
        driver.find_element(By.XPATH , "//span[normalize-space()='Create account']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='For my personal use']").click()
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("name")
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("surname")
        driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        driver.implicitly_wait(100)
        dropdown = driver.find_element(By.ID, 'month')
        driver.implicitly_wait(100)
        select = Select(dropdown)
        select.select_by_index(4)
        driver.find_element(By.XPATH, "//input[@id='day']").send_keys("14")
        driver.find_element(By.XPATH, "//input[@id='year']").send_keys("2003")
        Select(driver.find_element(By.XPATH, "//select[@id='gender']")).select_by_index(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        driver.quit()

findbyid = Func()
findbyid.fill_the_form()