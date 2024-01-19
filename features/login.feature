Feature: Login functionality

  @smoke-testing
  Scenario: Valid user login
    Given User navigates to login page
    When User enters credentials
    And User clicks on login button
    Then User should be logged in

  @smoke-testing
  Scenario: Invalid user login
    Given User navigates to login page
    When User enters wrong credentials
    And User clicks on login button
    Then Proper warning message should be displayed