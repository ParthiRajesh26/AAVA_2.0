import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

REGISTRATION_URL = 'https://your-app-url.com/register'  # Replace with actual URL

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Or use webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get(REGISTRATION_URL)
        logging.info('Navigated to registration page')

    def tearDown(self):
        self.driver.quit()
        logging.info('Closed browser')

    def fill_registration_form(self, name, email, password):
        driver = self.driver
        driver.find_element(By.ID, 'name').clear()
        driver.find_element(By.ID, 'name').send_keys(name)
        driver.find_element(By.ID, 'email').clear()
        driver.find_element(By.ID, 'email').send_keys(email)
        driver.find_element(By.ID, 'password').clear()
        driver.find_element(By.ID, 'password').send_keys(password)
        logging.info(f'Entered registration info: {name}, {email}, {password}')

    def click_register(self):
        self.driver.find_element(By.ID, 'register-btn').click()
        logging.info('Clicked Register button')

    def test_successful_registration(self):
        """Scenario: Successful registration with valid information"""
        self.fill_registration_form('Test User', 'testuser@example.com', 'StrongPassw0rd!')
        self.click_register()
        try:
            self.driver.find_element(By.ID, 'welcome-page')
            logging.info('Redirected to welcome page')
        except NoSuchElementException:
            self.fail('Welcome page not found after registration')
        # Optionally check account creation in DB or API

    def test_invalid_email_format(self):
        """Scenario: Registration attempt with invalid email format"""
        self.fill_registration_form('Test User', 'invalid-email', 'StrongPassw0rd!')
        self.click_register()
        try:
            error = self.driver.find_element(By.ID, 'error-message')
            self.assertIn('Invalid email format', error.text)
            logging.info('Correct error message displayed for invalid email')
        except NoSuchElementException:
            self.fail('Error message not displayed for invalid email format')
        # Ensure registration was not completed
        self.assertFalse(self.is_registration_successful())

    def test_weak_password(self):
        """Scenario: Registration attempt with weak password"""
        self.fill_registration_form('Test User', 'testuser@example.com', '12345')
        self.click_register()
        try:
            error = self.driver.find_element(By.ID, 'error-message')
            self.assertIn('Password does not meet strength requirements', error.text)
            logging.info('Correct error message displayed for weak password')
        except NoSuchElementException:
            self.fail('Error message not displayed for weak password')
        # Ensure registration was not completed
        self.assertFalse(self.is_registration_successful())

    def is_registration_successful(self):
        # Checks for the presence of the welcome page or confirmation element
        try:
            self.driver.find_element(By.ID, 'welcome-page')
            return True
        except NoSuchElementException:
            return False

if __name__ == '__main__':
    unittest.main()
