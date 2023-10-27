import os

from selene.api import *
from pages.registration_page import registration_page


def test_fill_form(open_browser):
    registration_page.open()
    registration_page.close_banner()
    # WHEN
    (
        registration_page
        .fill_first_name('Alexey')
        .fill_last_name('Kokorev')
        .fill_user_email('test@gmail.ru')
        .select_gender('Male')
        .fill_user_number('1234567890')
        .fill_date_of_birth('1991', 'May', 15)
        .fill_subject('Maths')
        .fill_hobby('Sports')
        .upload_picture('bat.png')
        .fill_current_address('Bali, Ubud, 1')
        .fill_state('NCR')
        .fill_city('Delhi')
        .submit()
    )

    # THEN
    registration_page.should_register_user(
                'Alexey Kokorev',
                'test@gmail.ru',
                'Male',
                '1234567890',
                '15 May,1991',
                'Maths',
                'Sports',
                'bat.png',
                'Bali, Ubud, 1',
                'NCR Delhi')

    # browser.execute_script('document.querySelector("#fixedban").remove()')
    # browser.element('footer').execute_script('element.remove()')
    # browser.element('#firstName').should(be.blank).type('TestFirstName')
    # browser.element('#lastName').should(be.blank).type('TestLastName')
    # browser.element('#userEmail').should(be.blank).type('test@gmail.com')
    # browser.element('[for="gender-radio-1"]').click()
    # browser.element('#userNumber').should(be.blank).type('1234567890')
    # browser.element('#dateOfBirthInput').click()
    # browser.element(".react-datepicker__month-select>option[value='1']").click()
    # browser.element(".react-datepicker__year-select>option[value='1999']").click()
    # browser.element('.react-datepicker__day--019').click()
    # browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    # browser.element("[for='hobbies-checkbox-3']").click()
    # browser.element('#uploadPicture').send_keys(os.path.abspath('resources/bat.png'))
    # browser.element('#currentAddress').type("test")
    # browser.element('#react-select-3-input').type('ncr').press_enter()
    # browser.element('#react-select-4-input').type('delhi').press_enter()
    # browser.element('#submit').press_enter()
    # browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    # browser.element('.table').should(have.text('TestFirstName TestLastName'))
    # browser.element('.table').should(have.text('test@gmail.com'))
    # browser.element('.table').should(have.text('Male'))
    # browser.element('.table').should(have.text('1234567890'))
    # browser.element('.table').should(have.text('19 February,1999'))
    # browser.element('.table').should(have.text('Maths'))
    # browser.element('.table').should(have.text('Music'))
    # browser.element('.table').should(have.text('bat.png'))
    # browser.element('.table').should(have.text('test'))
    # browser.element('.table').should(have.text('NCR Delhi'))
