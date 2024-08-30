import time
import logging
import os

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import CPF, PASSWORD, CONTRATO, chrome_prefs
from locators import Locators


class NeoenergiaAutomation:
    def __init__(self, cpf, password, contrato, chrome_prefs):
        self.cpf = cpf
        self.password = password
        self.contrato = contrato
        self.chrome_prefs = chrome_prefs
        self.browser = self._init_browser()
        self.wait = WebDriverWait(self.browser, 30)
        self.logger = self._setup_logger()

    def _init_browser(self):
        options = uc.ChromeOptions()
        options.add_experimental_option("prefs", self.chrome_prefs)
        return uc.Chrome(options=options)

    def _setup_logger(self):
        logger = logging.getLogger("NeoenergiaAutomation")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def login(self):
        self.browser.get(Locators.URL_2_VIA)

        cpf_field = self.wait.until(EC.element_to_be_clickable(Locators.CPF_FIELD))
        cpf_field.send_keys(self.cpf)

        password_field = self.wait.until(EC.element_to_be_clickable(Locators.PASSWORD_FIELD))
        password_field.send_keys(self.password)

        login_button = self.wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        login_button.click()

    def select_contract(self):
        contract_field = self.wait.until(EC.element_to_be_clickable(Locators.CONTRACT_FIELD(self.contrato)))
        contract_field.click()

    def switch_to_pdf_frame(self):
        iframe = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        self.browser.switch_to.frame(iframe)

    def download_pdf(self):
        imprimir_field = self.wait.until(EC.element_to_be_clickable(Locators.IMPRIMIR_FIELD))
        imprimir_field.click()

        window_handles = self.browser.window_handles
        self.browser.switch_to.window(window_handles[1])

        nao_fatura_mao_button = self.wait.until(EC.element_to_be_clickable(Locators.NAO_FATURA_MAO_BUTTON))
        nao_fatura_mao_button.click()

    def check_for_pdf_and_quit(self):
        output_dir = os.path.join(os.getcwd(), 'output')
        
        time.sleep(10)
        
        pdf_files = [f for f in os.listdir(output_dir) if f.endswith('.pdf')]
        
        if pdf_files:
            self.logger.info(f"Arquivos PDF encontrados: {pdf_files}. Fechando o navegador...")
            self.browser.quit()
        else:
            self.logger.warning("Nenhum arquivo PDF encontrado na pasta /output.")

    def run(self):
        try:
            self.login()
            self.select_contract()
            self.switch_to_pdf_frame()
            self.download_pdf()
        finally:
            self.check_for_pdf_and_quit()


if __name__ == "__main__":
    automation = NeoenergiaAutomation(CPF, PASSWORD, CONTRATO, chrome_prefs)
    automation.run()
