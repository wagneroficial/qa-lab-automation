Feature: API Creation from Scratch
    As an admin user
    I want to create APIs from scratch
    So that I can build custom APIs in the system

    Background:
        Given I go to the login page
        When I log in with valid admin credentials
        Then I should be logged in successfully

    Scenario: Create Pokemon API from scratch successfully
        Given I am on the APIs section
        When I create a new Pokemon API from scratch
        Then I should see API created successfully with full verification
