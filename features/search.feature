Feature: Search functionality

  @smoke-testing
  Scenario: Search for valid product
    Given User navigates to app home-page
    When User enters product in search box
    And User clicks on search button
    Then Product should be displayed in search results
    And User closes the browser


  Scenario: Search for invalid product
    Given User navigates to app home-page
    When User enters invalid product in search box
    And User clicks on search button
    Then Proper message for product not found should be displayed
    And User closes the browser

  @smoke-testing
  Scenario: Search without any product name
    Given User navigates to app home-page
    When User enters nothing in search box
    And User clicks on search button
    Then Proper message for product not found should be displayed
    And User closes the browser