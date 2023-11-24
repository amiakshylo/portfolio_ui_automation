import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from generator.generator import generating_person, generating_subjects
from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    # locators:
    __firs_name_locator = (By.ID, "firstName")
    __last_name_locator = (By.ID, "lastName")
    __email_locator = (By.ID, "userEmail")
    __gender_locator = (By.XPATH, f"//label[@for='gender-radio-{random.randint(1, 3)}']")
    __mobile_number_locator = (By.ID, "userNumber")
    __date_of_birth_locator = (By.ID, "dateOfBirthInput")
    __month_locator = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    __months_input = (By.XPATH, f"//option[@value='{random.randint(0, 11)}']")
    __years_locator = (By.XPATH, "//select[@class='react-datepicker__year-select']")
    __years_input = (By.XPATH, "//select[@class='react-datepicker__year-select']/option")
    __days_locator = (By.XPATH, "//div[@tabindex='-1']")
    __subject_locator = (By.ID, "subjectsInput")
    __hobbies_locator = (By.ID, f"hobbies-checkbox-{random.randint(1, 3)}")
    __chose_file_locator = (By.ID, "uploadPicture")
    __current_address_locator = (By.ID, "currentAddress")
    __select_state_locator = (By.XPATH, "//div[@id='state']")
    __input_state_locator = (By.ID, "react-select-3-input")
    __select_city_locator = (By.XPATH, "//div[@id='city']")
    __input_city_locator = (By.ID, "react-select-4-input")

    def fill_student_registration_form(self):
        generated_data = next(generating_person())
        subjects_data = generating_subjects()
        self._type(self.__firs_name_locator, generated_data.first_name)
        self._type(self.__last_name_locator, generated_data.last_name)
        self._type(self.__email_locator, generated_data.email)
        self._click(self.__gender_locator)
        self._type(self.__mobile_number_locator, generated_data.mobile)
        self._click(self.__date_of_birth_locator)
        self._click(self.__month_locator)
        # random_month = super()._find_visible_elements(self.__months_input)
        self._go_to_element(self._find_visible_elements(self.__months_input))

        time.sleep(5)







