Feature: API Creation and Management
    As an admin user
    I want to create and manage APIs from URL
    So that I can manage external APIs in the system

    Background:
        Given I go to the login page
        When I log in with valid_admin credentials
        Then I should see 'dashboard'

    @regression
    Scenario: Create complete API workflow from URL
        Given I am on the APIs section
        When I create a new API from URL
        Then I should see API created successfully
        When I configure the API with all features
        And I create an API Product with billing
        Then I should see the complete workflow finished