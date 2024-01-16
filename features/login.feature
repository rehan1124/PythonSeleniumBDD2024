Feature: Login functionality

  Scenario: Valid user login
    Given User navigates to app home-page
    When User navigates to login page
    And User enters credentials
    Then User should be logged in

  Scenario: Invalid user login
    Given User navigates to app home-page
    When User navigates to app home-page
    And User enters credentials
    Then Proper warning message should be displayed