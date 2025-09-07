Feature: Place Order feature

  Scenario: Verify details on 'Order Details' page.
    Given An Order is already placed using API
    And The user is on the landing page
    When User login to applicaiton
    And Navigate to the Orders page
    And Selects the order
    Then Verify the Order details
