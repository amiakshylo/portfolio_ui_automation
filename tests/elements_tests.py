import random

from pages.elements_page import TextBoxPage, CheckboxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage, \
    UploadDownload, DynamicProperties
from pages.form_page import PracticeFormPage


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
        parametrize


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


class TestButtonPage:

    def test_click_buttons(self, driver):
        click_buttons = ButtonsPage(driver, "https://demoqa.com/buttons")
        click_buttons.open_webpage()
        assert click_buttons.click_button("Double Click Me") == "You have done a double click", \
            "Button 'Double Click Me' wasn't click"
        assert click_buttons.click_button("Right Click Me") == "You have done a right click", \
            "Button 'Right Click Me' wasn't click"
        assert click_buttons.click_button("Click Me") == "You have done a dynamic click", \
            "Button 'Click Me' wasn't click"


class TestLinkPage:

    def test_simple_link(self, driver):
        simple_link = LinksPage(driver, "https://demoqa.com/links")
        simple_link.open_webpage()
        link_href, opened_url = simple_link.click_simple_link()
        assert link_href == opened_url, "The link is broken or url is incorrect"


class TestUploadDownloadPage:

    def test_upload_file(self, driver):
        upload_file = UploadDownload(driver, "https://demoqa.com/upload-download")
        upload_file.open_webpage()
        uploading_file, uploaded_file = upload_file.upload_file()
        assert uploading_file == uploaded_file, "The file hasn't been uploaded"

    def test_download_file(self, driver):
        download_file = UploadDownload(driver, "https://demoqa.com/upload-download")
        download_file.open_webpage()
        assert download_file.download_file() is True, "The file hasn't been downloaded"


class TestDynamicProperties:
    def test_button_color_changing(self, driver):
        color_change = DynamicProperties(driver, "https://demoqa.com/dynamic-properties")
        color_change.open_webpage()
        color_before, color_after = color_change.verify_buttons_color_changing()
        assert color_after == "rgba(220, 53, 69, 1)", "Changing color of button is not correct"
        assert color_before != color_after, "Color of button has not been changed"

    def test_button_appearing(self, driver):
        button_appearing = DynamicProperties(driver, "https://demoqa.com/dynamic-properties")
        button_appearing.open_webpage()
        before, after = button_appearing.verify_button_appearing()
        assert before is False, "Button is visible before 5 sec"
        assert after is True, "Button hasn't been appeared after 5 sec"


class TestPracticeFormPage:

    def test_fill_student_registration_form(self, driver):
        fill_form = PracticeFormPage(driver, "https://demoqa.com/automation-practice-form")
        fill_form.open_webpage()
        fill_form.fill_student_registration_form()
