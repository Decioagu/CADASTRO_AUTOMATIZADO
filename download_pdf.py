from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from time import sleep
import os
from Etapa_01_pdf_em_txt import pdf_em_txt

def download_pfd():

    # 1. Definir a URL e o local de download:
    PASTA_RAIZ = Path(__file__).parent
    PASTA_NOVA = PASTA_RAIZ / 'pdfs_originais'

    # 2. Definir a pasta de download padrão antes de iniciar a automação.
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"download.default_directory": str(PASTA_NOVA)})

    # 3. Abrir o navegador e navegar até a página:
    driver = webdriver.Chrome(options=options) # (options=options) = # 1.
    url = "https://doweb.rio.rj.gov.br/"
    driver.get(url)

    # 4. Localizar o link de download:
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//img[@id="imagemCapa"]'))
    )

    # 5. Clicar no link de download:
    ActionChains(driver).move_to_element(link).click().perform()

    # 6. Esperar o download terminar:
    while not os.path.exists(os.path.join(PASTA_NOVA, "arquivo.pdf")):
        sleep(5)
        # 7. Fechar o navegador:
        driver.quit()

if __name__ == '__main__':
    download_pfd()

