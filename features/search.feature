Feature: Search functionality

  @smoke-testing
  Scenario: Search for valid product
    Given User enters product in search box
    When User clicks on search button
    Then Product should be displayed in search results


  Scenario: Search for invalid product
    Given User enters invalid product in search box
    When User clicks on search button
    Then Proper message for product not found should be displayed

  @smoke-testing
  Scenario: Search without any product name
    Given User enters nothing in search box
    When User clicks on search button
    Then Proper message for product not found should be displayed