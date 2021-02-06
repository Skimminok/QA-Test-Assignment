import time
from .base_page import BasePage

name = ""
password = ""

class MainPage(BasePage):
    def go_to_login(self):
        selector = "[data-marker = 'header/login-button']"
        login_link = self.browser.find_element_by_css_selector(selector)
        login_link.click()

    def login(self):
        textarea = self.browser.find_element_by_css_selector("[name='login']")
        textarea.send_keys(f"{name}")
        textarea = self.browser.find_element_by_css_selector("[name='password']")
        textarea.send_keys(f"{password}")
        submit_button = self.browser.find_element_by_css_selector("[name='submit']")
        submit_button.click()

        # для прохода капчи
        # time.sleep(50)

    def check_login(self):
        selector = "[href = '/profile']"
        check_login = self.browser.find_element_by_css_selector(selector)
        assert check_login, "Ошибка авторизации"

    def go_to_page(self):
        selector = "[data-marker='catalog-serp'] > [data-marker='item']:nth-child(2) > div > div > div > a"
        first_url = self.browser.find_element_by_css_selector(selector)

        # меняем атрибут targeta для перехода по ссылке в текущем окне браузера
        self.browser.execute_script("arguments[0].setAttribute('target','_self')", first_url)
        first_url.click()

    def go_to_delivery(self):
        delivery_button = self.browser.find_element_by_css_selector("[data-marker='delivery-item-button-main']")
        delivery_button.click()

    def check_phone_textfield(self):
        phone_area = self.browser.find_element_by_css_selector("[data-marker='sd/order-widget-field/phone']")
        assert phone_area.text == '', "Поле телефон не пустое"
