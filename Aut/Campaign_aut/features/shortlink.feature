Feature: Creación de campañas en Yellow Push

  Background:
    Given I am on the Yellow Push login page
    And I log in with valid credentials

  Scenario: Selección de la opción "shortlinks"
    When I select the "shortlinks" option in the campaigns menu
    Then I am redirected to the campaign creation page

  Scenario: Selección de una empresa
    Given I am on the campaign creation page
    When I select a valid company from the dropdown list
    Then the selected company is displayed on the page

  Scenario: Ingreso de nombre de campaña y selección de opción "send now"
    Given I am on the campaign creation page
    When I enter a valid campaign name and select "send now"
    Then the campaign is created and sent immediately

  Scenario: Ingreso de nombre de campaña y selección de opción "schedule"
    Given I am on the campaign creation page
    When I enter a valid campaign name and select "schedule"
    Then the campaign is created and scheduled for future delivery

  Scenario: Carga de archivo CSV y selección de campo número y wildcards
    Given I am on the campaign creation page
    When I upload a valid CSV file with numerical data and select the "number" field and appropriate wildcards
    Then the data is displayed correctly on the page

  Scenario: Ingreso de ID, URL y mensaje
    Given I am on the campaign creation page
    When I enter a valid campaign ID, valid shortlink URL, valid message, and valid phone number
    Then the cost of the message is displayed correctly on the page

  Scenario: Visualización de datos de campaña y envío
    Given I am on the campaign creation page
    When I review the campaign data and send the campaign
    Then the campaign is sent successfully

  Scenario Outline: Inicio de sesión con credenciales <credenciales>
    Given I am on the Yellow Push login page
    When I log in with <credenciales>
    Then I am logged in successfully or I receive an error message

    Examples:
      | credenciales        |
      | cbarbosa@identidadtech.com    |
      | usuario inválido    |
      | CamiloBarbosa08   |
      | contraseña inválida |


