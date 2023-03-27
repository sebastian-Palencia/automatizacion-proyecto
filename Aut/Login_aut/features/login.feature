Feature: Login

  As a user
  I want to be able to log in to the system
  So that I can access my personal information

  Background:
    Given I am on the login page

  Scenario: Successful login
    When I enter my valid username and password
    And I click on the login button
    Then I should see my personal dashboard

  Scenario: Failed login with incorrect username and password
    When I enter an invalid username and password
    And I click on the login button
    Then I should see an error message "Please enter a valid email address." indicating that the credentials are incorrect

  Scenario: Failed login with incorrect password
    When I enter my valid username and an invalid password
    And I click on the login button
    Then I should see an error message Your password is incorrect indicating that the your password is incorrect

  Scenario: Failed login with incorrect username
    When I enter an invalid username and a valid password
    And I click on the login button
    Then I should see an error message We can´t seem to find your account indicating that the user account was not found


