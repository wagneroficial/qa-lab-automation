Feature: User Registration - Happy Path
  @smoke @registration
  Scenario: Successful registration
    Given I am on the home page
    When I complete registration with valid data
    Then I should be on dashboard