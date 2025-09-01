Feature: login
    Scenario: Successful_admin_login
        Given I go to the login page
        When  I log in with valid admin credentials
        Then I should be logged in successfully

    Scenario: Successful_customer_login
        Given I go to the login page
        When  I log in with valid customer credentials
        Then I should be logged in successfully