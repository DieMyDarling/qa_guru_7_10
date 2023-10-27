from selene.api import *
import os

from selene.core.command import js


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def close_banner(self):
        browser.execute_script('document.querySelector("#fixedban").remove()')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_user_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def select_gender(self, value):
        browser.element(f'[value={value}] + label').click()
        return self

    def fill_user_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').all('option').element_by(have.exact_text(month)).click()
        browser.element('.react-datepicker__year-select').all('option').element_by(have.exact_text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()
        return self

    def fill_hobby(self, value):
        browser.element(f"//*[contains(text(),'{value}')]").click()
        return self

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(f'resources/{value}'))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def fill_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()
        return self

    def fill_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()
        return self

    def submit(self):
        browser.element('#submit').should(be.visible).perform(command=js.click)
        return self

    def should_register_user(self, *result):
        browser.element('.table').all('td').even.should(
            have.exact_texts(result))
        return self


registration_page = RegistrationPage()
