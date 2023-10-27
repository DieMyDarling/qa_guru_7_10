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

    def fill_phone(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_birth_date(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').all('option').element_by(have.exact_text(month)).click()
        browser.element('.react-datepicker__year-select').all('option').element_by(have.exact_text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()
        return self

    def fill_hobby(self, value):
        browser.element(f"//*[contains(text(),'{value}')]").perform(command=js.click)
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

    def register_user(self, user):
        (
            self
            .fill_first_name(user.first_name)
            .fill_last_name(user.last_name)
            .fill_user_email(user.email)
            .select_gender(user.gender)
            .fill_phone(user.phone)
            .fill_birth_date(user.birth_date.strftime('%Y'),
                             user.birth_date.strftime('%B'),
                             user.birth_date.strftime('%d'))
            .fill_subject(user.subject)
            .fill_hobby(user.hobby)
            .upload_picture(user.picture)
            .fill_current_address(user.address)
            .fill_state(user.state)
            .fill_city(user.city)
            .submit()
        )

    def should_registered_user(self, user):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.phone,
                f"{user.birth_date.strftime('%d')} "
                f"{user.birth_date.strftime('%B')},"
                f"{user.birth_date.strftime('%Y')}",
                user.subject,
                user.hobby,
                user.picture,
                user.address,
                f'{user.state} {user.city}'
            )
        )


registration_page = RegistrationPage()
