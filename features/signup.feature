Feature: User Registration
    Scenario: Successful registration
        Given I am on the signup page
        When I complete the signup form
        Then I should see the message "User created with success"
