import time

import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.maximize_window()
    yield
    time.sleep(2)
    browser.quit()
