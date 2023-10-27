from pages.registration_page import registration_page
from data.user import user


def test_fill_form(open_browser):
    registration_page.open()

    # WHEN
    registration_page.register_user(user)

    # THEN
    registration_page.should_registered_user(user)
