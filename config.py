import os

# Configurações principais
CPF = "CPF"
PASSWORD = "PASSWORD"
CONTRATO = "CONTRATO"

# Diretório de saída para downloads
current_dir = os.getcwd()
output_dir = os.path.join(current_dir, 'output')

# Garantindo que a pasta "output" exista
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Configurações do Chrome
chrome_prefs = {
    "download.prompt_for_download": False,
    "plugins.plugins_disabled": ["Chrome PDF Viewer"],
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True,
    "safebrowsing.enabled": False,
    "safebrowsing.disable_download_protection": True,
    "profile.default_content_settings.popups": 0,
    "download.default_directory": output_dir
}
