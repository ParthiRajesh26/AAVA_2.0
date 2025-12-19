Feature: User Registration

  Scenario: Successful registration with valid information
    Given I am a new user on the registration page
    When I enter a valid name, a valid email address, and a strong password
    And I click the 'Register' button
    Then my account should be created
    And I should be redirected to the welcome page

  Scenario: Registration attempt with invalid email format
    Given I am a new user on the registration page
    When I enter a valid name, an invalid email address, and a strong password
    And I click the 'Register' button
    Then I should see an error message 'Invalid email format'
    And the registration should not be completed

  Scenario: Registration attempt with weak password
    Given I am a new user on the registration page
    When I enter a valid name, a valid email address, and a weak password
    And I click the 'Register' button
    Then I should see an error message 'Password does not meet strength requirements'
    And the registration should not be completed
