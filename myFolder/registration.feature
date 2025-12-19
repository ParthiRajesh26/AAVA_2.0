Feature: User Registration

  Scenario: Successful registration with valid details
    Given I am a new user on the registration page
    When I enter a valid name, email, and password
    And I submit the registration form
    Then my account should be created
    And I should be redirected to the welcome page

  Scenario: Registration attempt with invalid email format
    Given I am a new user on the registration page
    When I enter a valid name and password
    And I enter an invalid email format
    And I submit the registration form
    Then I should see an error message indicating the email format is invalid
    And my account should not be created

  Scenario: Registration attempt with weak password
    Given I am a new user on the registration page
    When I enter a valid name and email
    And I enter a password that does not meet the strength requirements
    And I submit the registration form
    Then I should see an error message indicating the password is too weak
    And my account should not be created
