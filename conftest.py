from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture(scope='session', autouse=True)
def config():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture()
def open_google():
    browser.open('https://google.com')
