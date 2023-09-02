import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjectModel.loginpom import login
from PageObjectModel.dashboardpom import dashboard
from Utilities.logger import logclass

import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup")
class Test_login(logclass):

    def test02(self):
        log = self.getthelogs()
        lg = login(self.driver)
        db = dashboard(self.driver)
        lg.input_username(config.get("credential", "incorrect_username"))
        log.info("username entered")
        lg.input_password(config.get("credential", "incorrect_password"))
        log.info("password entered")
        lg.click_loginbtn()
        log.info("login button pressed")
        # time.sleep(10)
        #print("titlecheck :", db.check_dashboardtitle())
        try:
            if db.check_dashboardtitle() == 'Dashboard':
                log.info("Dashboard opened")
                assert True
        except:
            self.driver.save_screenshot('Screenshots\\loginbutton_001.png')
            log.error("Dashboard not opened")
            assert False


