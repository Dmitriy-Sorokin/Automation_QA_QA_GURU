from selene.support.shared import browser
from selene import be, have, by


def test_tools():
    browser.element('#firstName').type("Dima")
    browser.element('#lastName').type("Sorokin")
    browser.element('#userEmail').type("test_qa_gug@gmail.com")
    browser.element('[id^=gender]').double_click()
    browser.element('#userNumber').type("1234567890")
    browser.element('#dateOfBirthInput').click()
    browser.element('[class$=__week]>div').click()
    browser.element('#subjectsContainer>div>div.css-1hwfws3').click()
    browser.element('#hobbies-checkbox-1')
