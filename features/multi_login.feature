Feature: Multi-user login

    Scenario: Admin and Customer login simultaneously
        Given Admin is on the login page
        And Customer is on the login page
        When Admin logs in
        And Customer logs in
        Then Admin dashboard is visible
        And Customer dashboard is visible
