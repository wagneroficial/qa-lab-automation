Feature: User Login - Simple
  As a user
  I want to login to the system
  So that I can access my dashboard

  @smoke @login
  Scenario: Login with valid credentials
    Given I am on the login page
    When I login with valid credentials
    Then I should see welcome message

  @login
  Scenario: Logout from system
    Given I am logged in
    When I click the logout button
    Then I should be on login page