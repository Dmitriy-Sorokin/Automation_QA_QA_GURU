import os.path

from selene.support.shared import browser
from selene import be, have, by

from home_work_lesson_5 import test


def test_tools():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type("Dima")
    browser.element('#lastName').type("Sorokin")
    browser.element('#userEmail').type("test_qa_gug@gmail.com")
    # browser.element('[id^=gender]').double_click()
    browser.all("[name=gender]").element_by(have.value("Male")).double_click()
    browser.element('#userNumber').type("1234567890")
    browser.element('#dateOfBirthInput').click()
    browser.element('[class$=__week]>div').click()
    browser.element('#subjectsInput').type("Commerce").press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(test.__file__), "resources/1.jpg")))
    browser.element('#currentAddress').type("sdgsdgsdgsdgsdgsdg")
    browser.element('#react-select-3-input').type("NCR").press_enter()
    browser.element('#react-select-4-input').type("Delhi").press_enter()
    browser.element('#submit').click()
