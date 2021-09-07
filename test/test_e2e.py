import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class E2ETests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari(executable_path=r'/usr/bin/safaridriver')
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity', self.driver.title)

    def test_page_heading_is_named_entity_finder(self):
        heading = self._find("app-title").text
        self.assertEqual('Named Entity Finder', heading)

    def test_page_has_input_for_text(self):
        input_element = self._find('input-text')
        self.assertIsNotNone(input_element)

    def test_page_has_button_for_submitting_text(self):
        button = self._find('submit-button')
        self.assertIsNotNone(button)

    def test_page_has_ner_table(self):
        table = self._find('ner-table')
        self.assertIsNotNone(table)

    def test_page_submit_updates_table(self):
        input_element = self._find('input-text')
        button = self._find('submit-button')
        table = self._find('ner-table')
        input_element.send_keys("Caleb Baym lives in Wales.")
        button.click()
        wait = WebDriverWait(self.driver, 1)
        first_ent_xpath = '/html/body/div[1]/div[4]/table/tr[1]/td[1]'
        second_ent_xpath = '/html/body/div[1]/div[4]/table/tr[2]/td[1]'
        self.assertEqual( wait.until(EC.visibility_of_element_located(
                          (By.XPATH, first_ent_xpath))).text, "Caleb Baym")
        self.assertEqual( wait.until(EC.visibility_of_element_located(
                          (By.XPATH, second_ent_xpath))).text, "Wales")
    def _find(self, val):
        return self.driver.find_element_by_css_selector(f'[data-test-id={val}]')

