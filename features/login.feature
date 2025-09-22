Feature: Login

    @regression
    Scenario Outline: User login with different credentials
        Given I go to the login page
        When I log in with <credential_type> credentials
        Then I should see '<expected_message>'

        Examples:
            | credential_type | expected_message            |
            | valid_admin     | dashboard                   |
            | valid_customer  | dashboard                   |
            | invalid_email   | Invalid email or password.  |
            | invalid_password| Invalid email or password.  |
            | empty_fields    | Please fill out this field. |