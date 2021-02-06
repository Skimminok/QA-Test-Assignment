import time, unittest
from selenium import webdriver

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_textfield_phone(self):
        # данные для авторизации
        name = ""
        password = ""

        driver = self.driver
        driver.get("https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1")
        time.sleep(5)

        selector = "[data-marker='catalog-serp'] > [data-marker='item']:nth-child(2) > div > div > div > a"
        first_url = driver.find_element_by_css_selector(selector)

        # меняем атрибут targeta для перехода по ссылке в текущем окне браузера
        driver.execute_script("arguments[0].setAttribute('target','_self')", first_url)

        first_url.click()
        time.sleep(5)

        # оформление заказа с доставкой
        delivery_button = driver.find_element_by_css_selector("[data-marker='delivery-item-button-main']")
        delivery_button.click()
        time.sleep(5)

        # авторизация
        textarea = driver.find_element_by_css_selector("[name='login']")
        textarea.send_keys(f"{name}")
        textarea = driver.find_element_by_css_selector("[name='password']")
        textarea.send_keys(f"{password}")
        submit_button = driver.find_element_by_css_selector("[name='submit']")
        submit_button.click()

        # для прохождения капчи, надеюсь на тестовом стенде она отключена :)
        time.sleep(50)

        # проверка поля "Телефон"
        phone_area = driver.find_element_by_css_selector("[name='phone']").text
        assert phone_area == ""

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


