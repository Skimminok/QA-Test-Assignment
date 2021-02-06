from .pages.main_page import MainPage

def test_phone_textfield_isempty(browser):
        link1 = "https://www.avito.ru"
        page = MainPage(browser, link1)
        page.open()
        page.go_to_login()
        page.login()
        page.check_login()
        link2 = "https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1"
        page = MainPage(browser, link2)
        page.open()
        page.go_to_page()
        page.go_to_delivery()
        page.check_phone_textfield()



