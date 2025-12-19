# registration.py
"""
Production-ready Selenium automation script generated from 'registration.feature'.
Includes error handling, logging, and reporting for registration scenarios.
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='registration_test.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

REGISTRATION_URL = 'https://example.com/register'  # Replace with actual registration page URL

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(REGISTRATION_URL)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def submit_form(self, name, email, password):
        driver = self.driver
        try:
            driver.find_element(By.ID, 'name').clear()
            driver.find_element(By.ID, 'name').send_keys(name)
            driver.find_element(By.ID, 'email').clear()
            driver.find_element(By.ID, 'email').send_keys(email)
            driver.find_element(By.ID, 'password').clear()
            driver.find_element(By.ID, 'password').send_keys(password)
            driver.find_element(By.ID, 'register').click()
            logging.info(f"Form submitted: name={name}, email={email}, password={password}")
        except NoSuchElementException as e:
            logging.error(f"Element not found: {e}")
            self.fail(f"Element not found: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            self.fail(f"Unexpected error: {e}")

    def test_successful_registration(self):
        """Scenario: Successful registration with valid details"""
        self.submit_form('John Doe', 'john.doe@example.com', 'StrongPass123!')
        driver = self.driver
        try:
            # Check for account creation confirmation (e.g., success message)
            success_msg = driver.find_element(By.ID, 'success-message').text
            self.assertIn('Account created', success_msg)
            # Check for redirection to welcome page
            self.assertIn('/welcome', driver.current_url)
            logging.info("Successful registration validated.")
        except (NoSuchElementException, AssertionError) as e:
            logging.error(f"Validation failed: {e}")
            self.fail(f"Validation failed: {e}")

    def test_invalid_email_format(self):
        """Scenario: Registration attempt with invalid email format"""
        self.submit_form('Jane Doe', 'invalid-email', 'StrongPass123!')
        driver = self.driver
        try:
            error_msg = driver.find_element(By.ID, 'email-error').text
            self.assertIn('invalid email format', error_msg.lower())
            # Ensure account is not created
            self.assertNotIn('/welcome', driver.current_url)
            logging.info("Invalid email format scenario validated.")
        except (NoSuchElementException, AssertionError) as e:
            logging.error(f"Validation failed: {e}")
            self.fail(f"Validation failed: {e}")

    def test_weak_password(self):
        """Scenario: Registration attempt with weak password"""
        self.submit_form('Alice Smith', 'alice.smith@example.com', '123')
        driver = self.driver
        try:
            error_msg = driver.find_element(By.ID, 'password-error').text
            self.assertIn('password is too weak', error_msg.lower())
            # Ensure account is not created
            self.assertNotIn('/welcome', driver.current_url)
            logging.info("Weak password scenario validated.")
        except (NoSuchElementException, AssertionError) as e:
            logging.error(f"Validation failed: {e}")
            self.fail(f"Validation failed: {e}")

if __name__ == "__main__":
    unittest.main()
