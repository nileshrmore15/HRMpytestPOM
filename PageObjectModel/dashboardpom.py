
from selenium import webdriver
from selenium.webdriver.common.by import By

class dashboard():

    def __init__(self, driver):
        self.driver = driver
        self.dbtitle = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6'



    def check_dashboardtitle(self):
        # import pdb
        # pdb.set_trace()
        db_title = self.driver.find_element(By.XPATH, self.dbtitle).text
        return db_title
