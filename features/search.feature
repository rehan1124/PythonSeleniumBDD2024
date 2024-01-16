Feature: Search functionality

  Scenario: Search for valid product
    Given User navigates to app home-page
    When User enters product in search box
    And User clicks on search button
    Then Product should be displayed in search results


  Scenario: Search for invalid product
    Given User navigates to app home-page
    When User enters product in search box
    And User clicks on search button
    Then Proper message for product not found should be displayed

  Scenario: Search without any product name
    Given User navigates to app home-page
    When User enters nothing in search box
    And User clicks on search button
    Then Proper message for product not found should be displayed