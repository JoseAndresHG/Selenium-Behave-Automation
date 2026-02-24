Feature: Abrir pagina

  Scenario: El usuario abre la pagina exitosamente
    Given Abrir pagina https://demowebshop.tricentis.com/
    When hago click en el botón de "Registro"
    And hago click en el botón de "Genero"
    And diligencio "Jose" en el campo "TXT_FIRSTNAME"
    And diligencio "Hernandez" en el campo "TXT_LASTNAME"
    And diligencio "evalina25@onestiqu.com" en el campo "TXT_EMAIL"
    And diligencio "Test1234*" en el campo "TXT_PASSWORD"
    And diligencio "Test1234*" en el campo "TXT_CONFIRM_PASSWORD"
    Then hago click en el botón de "BTN_REGISTER_SUBMIT"




