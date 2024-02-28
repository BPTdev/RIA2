Feature: Local Language Change
  As a user
  I want to change the application language without a network connection
  So I can use the application in my preferred language

  Scenario: Changing language in offline mode
    Given the user is on the application without a network connection
    When the user selects a new language
    Then the application interface changes to display the selected language
