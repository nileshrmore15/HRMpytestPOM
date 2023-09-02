
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
driver = None
import time

#### for sensitive data create .properties file
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")
##add this to below code
#request.cls.driver.get(config.get("Url", "base_url"))
###

@pytest.fixture
def setup(request):
    global driver
    request.cls.driver = webdriver.Chrome()
    #request.cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    request.cls.driver.get(config.get("Url", "base_url"))
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(10)
    #time.sleep(10)
    yield
    request.cls.driver.quit()
