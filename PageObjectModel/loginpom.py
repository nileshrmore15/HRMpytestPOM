
from selenium import webdriver
from selenium.webdriver.common.by import By


class login():

    def __init__(self, driver):
        self.driver = driver
        self.username = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
        self.password = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        self.loginbutton = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    def input_username(self, Username):
        self.driver.find_element(By.XPATH, self.username).send_keys(Username)
        #self.driver.find_element_by_xpath(self.username).send_keys(Username)

    def input_password(self, Password):
        self.driver.find_element(By.XPATH, self.password).send_keys(Password)

    def click_loginbtn(self):
        self.driver.find_element(By.XPATH, self.loginbutton).click()


