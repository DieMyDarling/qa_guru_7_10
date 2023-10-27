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
