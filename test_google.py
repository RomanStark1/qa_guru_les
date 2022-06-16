from conftest import *

valid_data = 'selene'
not_valid_data = 'r32rdsf'
result = 'User-oriented Web UI browser tests in Python'

def test_first_positive(open_google):
    browser.element('[name="q"]').should(be.blank).type(valid_data).press_enter()
    browser.element('[id="search"]').should(have.text(result))

def test_second_negative(open_google):
    browser.element('[name="q"]').should(be.blank).type(not_valid_data).press_enter()
    browser.element('[id="search"]').should(have.no.text(result))

