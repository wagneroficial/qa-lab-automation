Feature: API Creation
    As an admin user
    I want to create APIs from URL
    So that I can manage external APIs in the system

    Background:
        Given I go to the login page
        When I log in with valid admin credentials
        Then I should be logged in successfully

    Scenario: Create API from URL successfully
        Given I am on the APIs section
        When I create a new API from URL
        Then I should see API created successfully