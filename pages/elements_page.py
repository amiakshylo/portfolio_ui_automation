import base64
import os
import random

import requests
from selenium.webdriver.common.by import By
from generator.generator import generating_person, generating_file
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

    def filling_out_the_form(self):
        # data(d)
        generated_data = next(generating_person())
        self._type(self.__full_name_locator, generated_data.full_name)
        self._type(self.__email_locator, generated_data.email)
        self._type(self.__current_address_locator, generated_data.current_address)
        self._type(self.__permanent_address_locator, generated_data.permanent_address)
        self._go_to_element(self._find_present_element(self.__button_submit_locator))
        self._click(self.__button_submit_locator)
        generated_data.current_address = generated_data.current_address.replace("\n", " ")
        generated_data.permanent_address = generated_data.permanent_address.replace("\n", " ")
        return (generated_data.full_name, generated_data.email, generated_data.current_address,
                generated_data.permanent_address)

    def verify_filed_form(self):
        result_name = self._get_text_from_element(self.__result_name_locator).split(":")[1]
        result_email = self._get_text_from_element(self.__result_email_locator).split(":")[1]
        result_curr_addr = self._get_text_from_element(self.__result_curr_addr_locator).split(":")[1]
        result_perm_addr = self._get_text_from_element(self.__result_perm_addr_l).split(":")[1]
        return result_name, result_email, result_curr_addr, result_perm_addr


class CheckboxPage(BasePage):
    # locators
    __button_expend_all_locator = (By.XPATH, "//button[@title='Expand all']")
    __all_checkboxes_locator = (By.XPATH, "//span[@class='rct-title']")
    __checked_checkboxes_locator = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    __checkbox_text_locator = ".//ancestor::span[@class='rct-text']"
    __resulted_checkboxes = (By.XPATH, "//span[@class='text-success']")

    def click_expend_all_button(self):
        self._click(self.__button_expend_all_locator)

    def click_random_checkboxes(self):
        random_number_for_cycle = random.randint(1, 15)
        all_checkboxes = self._find_present_elements(self.__all_checkboxes_locator)
        while random_number_for_cycle != 0:
            choosing_random_checkbox = all_checkboxes[random.randint(0, 16)]
            self._go_to_element(choosing_random_checkbox)
            choosing_random_checkbox.click()
            random_number_for_cycle -= 1

    def save_selected_checkboxes(self):
        checked_items_elements = self._find_present_elements(self.__checked_checkboxes_locator)
        checked_items_list = []
        for checked_item_element in checked_items_elements:
            getting_checked_checkboxes_text = checked_item_element.find_element("xpath", self.__checkbox_text_locator)
            checked_items_list.append(getting_checked_checkboxes_text.text)
        return str(checked_items_list).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def result_selected_items(self):
        result_items = self._find_present_elements(self.__resulted_checkboxes)
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
        if "yes" or "impressive" or "no" in button:
            self._click(__radio_button)

    def check_radio_button(self):
        return self._get_text_from_element(self.__text_success)


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
    __buttons_edit_row_l = (By.XPATH, "//span[@title='Edit']")
    __fields_of_registration_form = (By.XPATH, "//div[@class='mt-2 row']")
    __rows_switcher_button_l = (By.XPATH, "//select[@aria-label='rows per page']")
    __search_box_l = (By.ID, "searchBox")
    __full_people_list = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    __switcher_buttons_list = (By.XPATH, "//option[@value]")
    __all_table_rows_l = (By.XPATH, "//div[@role='rowgroup']")

    def number_of_rows_before(self):
        number_rows_before = self._find_visible_elements(self.__button_delete_row_l)
        return len(number_rows_before)

    def add_new_person(self):
        self._click(self.__button_add)
        self._type(self.__first_name_l, self.__person_info.first_name)
        self._type(self.__last_name_l, self.__person_info.last_name)
        self._type(self.__email_l, self.__person_info.email)
        self._type(self.__age_l, self.__person_info.age)
        self._type(self.__salary_l, self.__person_info.salary)
        self._type(self.__department_l, self.__person_info.department)
        self._click(self.__button_submit)
        return list((self.__person_info.first_name, self.__person_info.last_name, str(self.__person_info.age),
                     self.__person_info.email, str(self.__person_info.salary), self.__person_info.department))

    def number_of_rows_after(self):
        number_rows_after = self._find_visible_elements(self.__button_delete_row_l)
        return len(number_rows_after)

    def search_person(self, text):
        self._type(self.__search_box_l, text)

    @staticmethod
    def if_person_found(key_word, result_lists):
        for sublist in result_lists:
            if key_word in sublist:
                return True
        return False

    def check_person(self):
        list_of_persons = self._find_present_elements(self.__full_people_list)
        result_data = []
        for text_field in list_of_persons:
            result_data.append(text_field.text.splitlines())
        return result_data

    def edit_random_row_and_field(self):
        existing_rows = self._find_present_elements(self.__buttons_edit_row_l)
        choosing_random_row = random.choice(existing_rows)
        choosing_random_row.click()
        existing_fields = self._find_present_elements(self.__fields_of_registration_form)
        choosing_random_field = random.choice(existing_fields)
        random_field_text = choosing_random_field.text
        if random_field_text == "Department":
            self._clear_field(self.__department_l)
            self._type(self.__department_l, self.__person_info.department)
            self._click(self.__button_submit)
            return self.__person_info.department
        elif random_field_text == "First Name":
            self._clear_field(self.__first_name_l)
            self._type(self.__first_name_l, self.__person_info.first_name)
            self._click(self.__button_submit)
            return self.__person_info.first_name
        elif random_field_text == "Last Name":
            self._clear_field(self.__last_name_l)
            self._type(self.__last_name_l, self.__person_info.last_name)
            self._click(self.__button_submit)
            return self.__person_info.last_name
        elif random_field_text == "Email":
            self._clear_field(self.__email_l)
            self._type(self.__email_l, self.__person_info.email)
            self._click(self.__button_submit)
            return self.__person_info.email
        elif random_field_text == "Age":
            self._clear_field(self.__age_l)
            self._type(self.__age_l, self.__person_info.age)
            self._click(self.__button_submit)
            return self.__person_info.age
        elif random_field_text == "Salary":
            self._clear_field(self.__salary_l)
            self._type(self.__salary_l, self.__person_info.salary)
            self._click(self.__button_submit)
            return self.__person_info.salary

    def switch_row_per_page(self):
        self._go_to_element(self._find_present_element(self.__rows_switcher_button_l))
        self._click(self.__rows_switcher_button_l)
        buttons_select_rows_per_page = self._find_present_elements(self.__switcher_buttons_list)
        value = True
        for button_select_rows_per_page in buttons_select_rows_per_page:
            button_select_rows_per_page.click()
            clicked_button = button_select_rows_per_page.text.split(" ")[0]
            rows_per_table = self._find_present_elements(self.__all_table_rows_l)
            if clicked_button != str(len(rows_per_table)):
                value = False
                break
        return value

    def delete_person_from_table(self):
        count_rows_before_deleting = self.number_of_rows_before()
        self._click(self.__button_delete_row_l)
        count_rows_after_deleting = self.number_of_rows_after()
        if count_rows_before_deleting == count_rows_after_deleting + 1:
            return True


class ButtonsPage(BasePage):
    # locators
    __double_click_button_locator = (By.ID, "doubleClickBtn")
    __double_click_message_locator = (By.ID, "doubleClickMessage")
    __right_click_button_locator = (By.ID, "rightClickBtn")
    __right_click_message_locator = (By.ID, "rightClickMessage")
    ___click_me_button_locator = (By.XPATH, "//button[text()='Click Me']")
    ___click_me_message_locator = (By.ID, "dynamicClickMessage")

    def click_button(self, button):
        if button == "double_click_button":
            self._action("double_click", self.__double_click_button_locator)
            return self._get_text_from_element(self.__double_click_message_locator)
        elif button == "right_click_button":
            self._action("context_click", self.__right_click_button_locator)
            return self._get_text_from_element(self.__right_click_message_locator)
        elif button == "simple_click_button":
            self._click(self.___click_me_button_locator)
            return self._get_text_from_element(self.___click_me_message_locator)


class LinksPage(BasePage):
    # locators
    __simple_link_locator = (By.ID, "simpleLink")
    __dynamic_link_locator = (By.ID, "dynamicLink")

    def click_simple_link(self):
        simple_link_href = self._get_element_attribute(self.__simple_link_locator, "href")
        request_simple_link = requests.get(simple_link_href)
        if request_simple_link.status_code == 200:
            self._click(self.__simple_link_locator)
            self._switch_browser_tab_to(1)
            opened_tabs_url = self._current_url()
            return simple_link_href, opened_tabs_url
        else:
            return simple_link_href, request_simple_link.status_code


class UploadDownload(BasePage):
    # locators
    __chose_file_locator = (By.ID, "uploadFile")
    __uploaded_file_path = (By.ID, "uploadedFilePath")
    __download_file_locator = (By.ID, "downloadButton")

    def upload_file(self):
        file_name, path = generating_file()
        self._type(self.__chose_file_locator, path)
        os.remove(path)
        uploaded_file = self._get_text_from_element(self.__uploaded_file_path)
        return uploaded_file.split("\\")[-1], file_name

    def download_file(self):
        file_link = self._get_element_attribute(self.__download_file_locator, "href").split(",")[1]
        link_b = base64.b64decode(file_link)
        path_name_file = f".\\testfile{random.randint(0, 999)}.jpg"
        with open(path_name_file, 'wb+') as file:
            file.write(link_b)
            check_file = os.path.exists(path_name_file)
        os.remove(path_name_file)
        return check_file


class DynamicProperties(BasePage):
    # locators
    __button_color_change_locator = (By.ID, "colorChange")
    __button_visible_after_5sec_locator = (By.ID, "visibleAfter")

    def verify_buttons_color_changing(self):
        color_before = self._get_element_property(self.__button_color_change_locator)
        color_after = self._get_element_property(self.__button_color_change_locator)
        return color_before, color_after

    def verify_button_appearing(self):
        visibility_of_element_before_5sec = self._is_displayed(self.__button_visible_after_5sec_locator, 1)
        visibility_of_element_after_5sec = self._is_displayed(self.__button_visible_after_5sec_locator, 5)
        return visibility_of_element_before_5sec, visibility_of_element_after_5sec
