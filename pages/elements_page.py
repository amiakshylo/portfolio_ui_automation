import random


from selenium.webdriver.common.by import By
from generator.generator import generating_person
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    # locators(l)
    __full_name_locator = (By.ID, "userName")
    __email_locator = (By.ID, "userEmail")
    __current_address_locator = (By.ID, "currentAddress")
    __permanent_address_locator = (By.ID, "permanentAddress")
    __button_submit_locator = (By.XPATH, "//button[@id='submit']")
    __result_name_locator = (By.XPATH, "//p[@id='name']")
    __result_email_locator = (By.XPATH, "//p[@id='email']")
    __result_curr_addr_locator = (By.XPATH, "//p[@id='currentAddress']")
    __result_perm_addr_l = (By.XPATH, "//p[@id='permanentAddress']")

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def form_fill(self):
        # data(d)
        generated_data = next(generating_person())
        super()._type(self.__full_name_locator, generated_data.full_name)
        super()._type(self.__email_locator, generated_data.email)
        super()._type(self.__current_address_locator, generated_data.current_address)
        super()._type(self.__permanent_address_locator, generated_data.permanent_address)
        super()._go_to_element(self._find_present_element(self.__button_submit_locator))
        super()._click_button(self.__button_submit_locator)
        generated_data.current_address = generated_data.current_address.replace("\n", " ")
        generated_data.permanent_address = generated_data.permanent_address.replace("\n", " ")
        return generated_data.full_name, generated_data.email, generated_data.current_address, generated_data.permanent_address

    def verify_filed_form(self):
        result_name = super()._get_text_from_element(self.__result_name_locator).split(":")[1]
        result_email = super()._get_text_from_element(self.__result_email_locator).split(":")[1]
        result_curr_addr = super()._get_text_from_element(self.__result_curr_addr_locator).split(":")[1]
        result_perm_addr = super()._get_text_from_element(self.__result_perm_addr_l).split(":")[1]
        return result_name, result_email, result_curr_addr, result_perm_addr


class CheckboxPage(BasePage):
    # locators
    __button_expend_all_locator = (By.XPATH, "//button[@title='Expand all']")
    __all_checkboxes_locator = (By.XPATH, "//span[@class='rct-title']")
    __checked_checkboxes_locator = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    __checkbox_text_locator = ".//ancestor::span[@class='rct-text']"
    __resulted_checkboxes = (By.XPATH, "//span[@class='text-success']")

    def click_expend_all_button(self):
        super()._click_button(self.__button_expend_all_locator)

    def click_random_checkboxes(self):
        random_number_for_cycle = 15
        all_checkboxes = super()._find_present_elements(self.__all_checkboxes_locator)
        while random_number_for_cycle != 0:
            selection_random_checkbox = all_checkboxes[random.randint(0, 16)]
            super()._go_to_element(selection_random_checkbox)
            selection_random_checkbox.click()
            random_number_for_cycle -= 1

    def save_selected_checkboxes(self):
        checked_items_elements = self._find_present_elements(self.__checked_checkboxes_locator)
        checked_items_list = []
        for checked_item_element in checked_items_elements:
            getting_checked_checkboxes_text = checked_item_element.find_element("xpath", self.__checkbox_text_locator)
            checked_items_list.append(getting_checked_checkboxes_text.text)
        return str(checked_items_list).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def result_selected_items(self):
        result_items = super()._find_present_elements(self.__resulted_checkboxes)
        item_list = []
        for item in result_items:
            item_list.append(item.text)
        return str(item_list).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    # locators
    __text_success = (By.XPATH, "//span[@class='text-success']")

    def click_radio_button(self, button):
        # locators
        __radio_button = (By.XPATH, f"//label[@for='{button}Radio']")
        if button == "yes":
            super()._click_button(__radio_button)
        elif button == "impressive":
            super()._click_button(__radio_button)
        elif button == "no":
            super()._click_button(__radio_button)

    def check_radio_button(self):
        return super()._get_text_from_element(self.__text_success)


class WebTablesPage(BasePage):
    # data generator
    __person_info = next(generating_person())
    # locators
    __button_add = (By.XPATH, "//button[@id='addNewRecordButton']")
    __button_submit = (By.ID, "submit")
    __first_name_l = (By.ID, "firstName")
    __last_name_l = (By.ID, "lastName")
    __email_l = (By.ID, "userEmail")
    __age_l = (By.ID, "age")
    __salary_l = (By.ID, "salary")
    __department_l = (By.ID, "department")
    __button_delete_row_l = (By.XPATH, "//span[@title='Delete']")
    __button_edit_row_l = (By.XPATH, "//span[@title='Edit']")
    __rows_switcher_button_l = (By.XPATH, "//select[@aria-label='rows per page']")
    __search_box_l = (By.ID, "searchBox")
    __full_people_list = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    __switcher_buttons_list = (By.XPATH, "//option[@value]")
    __all_table_rows_l = (By.XPATH, "//div[@role='rowgroup']")

    def number_of_rows_before(self):
        number_rows_before = super()._find_visible_elements(self.__button_delete_row_l)
        return len(number_rows_before)

    def add_new_person(self):
        super()._click_button(self.__button_add)
        super()._type(self.__first_name_l, self.__person_info.first_name)
        super()._type(self.__last_name_l, self.__person_info.last_name)
        super()._type(self.__email_l, self.__person_info.email)
        super()._type(self.__age_l, self.__person_info.age)
        super()._type(self.__salary_l, self.__person_info.salary)
        super()._type(self.__department_l, self.__person_info.department)
        super()._click_button(self.__button_submit)
        return [self.__person_info.first_name, self.__person_info.last_name,
                str(self.__person_info.age), self.__person_info.email,
                str(self.__person_info.salary),
                self.__person_info.department]

    def number_of_rows_after(self):
        number_rows_after = super()._find_visible_elements(self.__button_delete_row_l)
        return len(number_rows_after)

    def check_new_added_person(self):
        people_list = super()._find_present_elements(self.__full_people_list)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_person(self, text):
        super()._type(self.__search_box_l, text)

    def check_person(self):
        search_result = super()._find_present_elements(self.__full_people_list)
        result_data = []
        for item in search_result:
            result_data.append(item.text.splitlines())
        return str(result_data)

    def edit_row(self):
        new_name = self.__person_info.first_name
        super()._click_button(self.__button_edit_row_l)
        super()._clear_field(self.__first_name_l)
        super()._type(self.__first_name_l, new_name)
        super()._click_button(self.__button_submit)
        return str(new_name)

    def switch_row_per_page(self):
        super()._go_to_element(self._find_present_element(self.__rows_switcher_button_l))
        super()._click_button(self.__rows_switcher_button_l)
        buttons_select_rows_per_page = super()._find_present_elements(self.__switcher_buttons_list)
        value = True
        for button_select_rows_per_page in buttons_select_rows_per_page:
            button_select_rows_per_page.click()
            clicked_button = button_select_rows_per_page.text.split(" ")[0]
            rows_per_table = super()._find_present_elements(self.__all_table_rows_l)
            if clicked_button != str(len(rows_per_table)):
                value = False
                break
        return value

    def delete_person_from_table(self):
        count_rows_before_deleting = self.number_of_rows_before()
        super()._click_button(self.__button_delete_row_l)
        count_rows_after_deleting = self.number_of_rows_after()
        if count_rows_before_deleting == count_rows_after_deleting + 1:
            return True







