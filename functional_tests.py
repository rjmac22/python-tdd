from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new onlie to-do app.
        # She goes to check out its hompage.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-to lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').header_text
        self.assertIn('To-Do', header_text)

        #She is invited to enter a to-do litem stright away
        inputbox = self.broser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('plaseholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')


        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # There is still a text box inviting her to add another item,
        # She enters "Use peacock fathers to make a fly"

        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her lists


        # Edth wonders wheather the site will remember her list, Then She
        # sees that the site had generated a unique URL for her -- there is
        # some explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

if __name__=='__main__':
    unittest.main(warnings='ignore')
