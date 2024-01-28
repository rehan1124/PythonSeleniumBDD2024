Feature: Search functionality

  Scenario: Search for valid product
    Given User enters product "HP" in search box
    When User clicks on search button
    Then Product "HP LP3065" should be displayed in search results

  @smoke-testing
  Scenario Outline: Search for invalid product
    Given User enters invalid product "<product_name>" in search box
    When User clicks on search button
    Then Message for product not found should be displayed "There is no product that matches the search criteria."
    Examples:
      | product_name |
      | JALALALALA   |
      | 1234ABCD     |

  Scenario: Search without any product name
    Given User enters nothing in search box
    When User clicks on search button
    Then Message for product not found should be displayed "There is no product that matches the search criteria."