Feature: Login functionality

  @smoke-testing
  Scenario: Valid user login
    Given User navigates to login page
    When User enters credentials "bdd1@gmail.com" "bdd1"
    And User clicks on login button
    Then User should be logged in and see link "View your order history"

  @smoke-testing
  Scenario: Invalid user login
    Given User navigates to login page
    When User enters wrong credentials "bdd1" "bdd1"
    And User clicks on login button
    Then Proper warning message "Warning: No match for E-Mail Address and/or Password." should be displayed