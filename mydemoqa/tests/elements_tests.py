import random
import time

from pages.elements_page import TextBoxPage, CheckboxPage, RadioButtonPage, WebTablesPage


class TestTextBoxPage:

    def test_text_box(self, driver):
        text_box = TextBoxPage(driver, "https://demoqa.com/text-box")
        text_box.open_webpage()
        assert text_box.form_fill() == text_box.verify_filed_form()


class TestCheckBoxPage:

    def test_checkbox_page(self, driver):
        checkbox = CheckboxPage(driver, "https://demoqa.com/checkbox")
        checkbox.open_webpage()
        checkbox.click_expend_all_button()
        checkbox.click_random_checkboxes()
        checked_items = checkbox.save_selected_checkboxes()
        result_items = checkbox.result_selected_items()
        assert checked_items == result_items, "No elements have been selected"


class TestRadioButton:

    def test_radio_button(self, driver):
        radio_button = RadioButtonPage(driver, "https://demoqa.com/radio-button")
        radio_button.open_webpage()
        radio_button.click_radio_button("yes")
        assert radio_button.check_radio_button() == "Yes", "Button 'yes' has not been clicked"
        radio_button.click_radio_button("impressive")
        assert radio_button.check_radio_button() == "Impressive", "Button 'Impressive' has not been clicked"
        radio_button.click_radio_button("no")
        assert radio_button.check_radio_button() == "No", "Button 'No' has not been clicked"


class TestWebFormPage:

    def test_add_person(self, driver):
        web_form = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_form.open_webpage()
        rows_before = web_form.number_of_rows_before()
        added_data = web_form.add_new_person()
        rows_after = web_form.number_of_rows_after()
        assert rows_after == rows_before + 1, "Row has not been added"
        result_data = web_form.check_new_added_person()
        assert added_data in result_data, "New person has not been added"

    def test_search_person(self, driver):
        web_form = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_form.open_webpage()
        key_word = web_form.add_new_person()[random.randint(0, 5)]
        web_form.search_person(key_word)
        search_result = web_form.check_person()
        assert key_word in search_result, "The person has not been found"

    def test_edit_row(self, driver):
        web_form = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_form.open_webpage()
        text_edited_field = web_form.edit_row()
        edited_result = web_form.check_person()
        assert text_edited_field in edited_result, "The person has not been changed"

    def test_rows_per_page_switcher(self, driver):
        web_form = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_form.open_webpage()
        assert web_form.switch_row_per_page(), "Buttons changing rows per page in table doesn't work"

    def test_deleting_person_from_table(self, driver):
        web_form = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_form.open_webpage()
        assert web_form.delete_person_from_table(), "Button 'delete' doesn't work, person has not been deleted"
