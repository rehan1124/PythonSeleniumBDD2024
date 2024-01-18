Feature: Login functionality

  @smoke-testing
  Scenario: Valid user login
    Given User navigates to app home-page
    When User navigates to login page
    And User enters credentials
    And User clicks on login button
    Then User should be logged in
    And User closes the browser

  @smoke-testing
  Scenario: Invalid user login
    Given User navigates to app home-page
    When User navigates to login page
    And User enters wrong credentials
    And User clicks on login button
    Then Proper warning message should be displayed
    And User closes the browser