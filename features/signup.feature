Feature: User Registration
    @regression
    Scenario Outline: User registration with different data
        Given I go to the signup page
        When I register with <data_type> data
        Then I should see '<expected_message>'

        Examples:
            | data_type        | expected_message        |
            | valid           | User created with success |
            | invalid_company | Company not found       |
            | existing_user   | User already exists     |