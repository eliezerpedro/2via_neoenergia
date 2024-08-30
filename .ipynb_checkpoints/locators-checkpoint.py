from selenium.webdriver.common.by import By

class Locators:
    URL_2_VIA = "https://servicos.neoenergiapernambuco.com.br/servicos-ao-cliente/Pages/2-via-conta_anti.aspx"
    CPF_FIELD = (By.XPATH, "//input[@class='cpfcnpj required']")
    PASSWORD_FIELD = (By.XPATH, "//input[@class='password required']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='btn']")
    CONTRACT_FIELD = lambda contrato: (By.XPATH, f"//td[contains(text(), '{contrato}' )]//..//td//input")
    IMPRIMIR_FIELD = (By.XPATH, "//table[@class='neoNNtab00']//tbody//tr//td//img")
    NAO_FATURA_MAO_BUTTON = (By.XPATH, "//input[@id='btn_naofaturamao']")
    SERVICE_UNAVAILABLE = (By.XPATH, "//center[contains(text(), 'O serviço não está disponível atualmente.')]")
