from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture(autouse='True')
def screen_config():
    browser.open('https://google.com').driver.set_window_size(1920, 1280)



