from selene.support.shared import browser
from selene import have, be


def test_google():
    browser.open("https://www.google.com/")
    browser.element("#APjFqb").should(be.blank).type("selene").press_enter()
    browser.element("[id=search]").should(have.text("Selene - 40DEN.eu"))

browser.quit()