import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjectModel.loginpom import login
from PageObjectModel.dashboardpom import dashboard
from Utilities.logger import logclass

@pytest.mark.usefixtures("setup")
class Test_login(logclass):

    @pytest.mark.parametrize('ussername, paassword', [('Admin', 'admin123')]) #, ('Admin', 'admin'), ('admin', 'admin123')])
    def test01(self, ussername, paassword):
        log = self.getthelogs()
        lg = login(self.driver)
        db = dashboard(self.driver)
        lg.input_username(ussername)
        log.info("username entered")
        lg.input_password(paassword)
        log.info("password entered")
        lg.click_loginbtn()
        log.info("login button pressed")
        # time.sleep(10)
        print("titlecheck :", db.check_dashboardtitle())
        if db.check_dashboardtitle() == 'Dashboard':
            log.info("Dashboard opened")
            assert True
        else:
            log.error("Dashboard not opened")
            assert False

