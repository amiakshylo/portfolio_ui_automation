from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver, url):
        self._driver = driver
        self._url = url

    def open_webpage(self):
        self._driver.get(self._url)

    def _find_visible_element(self, locator, timeout=5):
        return wait(self._driver, timeout).until(ec.visibility_of_element_located(locator))

    def _find_visible_elements(self, locator, timeout=5):
        return wait(self._driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def _find_present_element(self, locator, timeout=5):
        return wait(self._driver, timeout).until(ec.presence_of_element_located(locator))

    def _find_present_elements(self, locator, timeout=5):
        return wait(self._driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def _type(self, locator, text):
        self._find_visible_element(locator).send_keys(text)

    def _click_button(self, locator):
        self._find_visible_element(locator).click()

    def _get_text_from_element(self, locator):
        return self._find_visible_element(locator).text

    def _go_to_element(self, element):
        self._driver.execute_script("arguments[0].scrollIntoView();", element)

    def _clear_field(self, locator):
        self._find_visible_element(locator).clear()

    def remove_footer(self):
        self._driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self._driver.execute_script("document.getElementsById('close-fixedban').remove();")







