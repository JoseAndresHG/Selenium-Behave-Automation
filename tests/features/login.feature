Feature: Realizar login

  Scenario: El usuario hace login correctamente
    Given Abrir pagina https://demowebshop.tricentis.com/
    When hago click en el botón de "LOG_IN"
    And diligencio "cedojay777@pazuric.com" en el campo "TXT_EMAIL"
    And diligencio "Test1234*" en el campo "TXT_PASSWORD"
    Then hago click en el botón de "BTN_LOG_IN"