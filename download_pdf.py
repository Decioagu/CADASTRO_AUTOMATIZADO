from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from time import sleep
import requests
from datetime import date

hoje = (date.today().strftime('%d/%m/%Y')) # campo de inserção de data (dd/mm/aaaa)

def download_pfd(data = str(hoje)):
    print(data)

    # caminho da pasta raiz
    PASTA_RAIZ = Path(__file__).parent

    nova_pasta = PASTA_RAIZ / 'PDF' # criar pasta nova_pasta.
    nova_pasta.mkdir(exist_ok=True) # exist_ok=True para não da erro se existir pasta

    PASTA_NOVA = PASTA_RAIZ / nova_pasta # caminho nova_pasta.

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
    sleep(20)

    # 7. Fechar o navegador:
    driver.quit()

print('FIM download_pdf...')

def verifica_conexao_internet():
    try:
        # Faz uma requisição para o Google
        requests.get('https://www.google.com.br/', timeout=5)
        print("Conectado à internet!")
        texto_conexao = "Conectado à internet!"
        return texto_conexao
    except requests.ConnectionError:
        # Se a requisição falhar, retorna False
        print("Sem conexão com a internet.")
        texto_conexao = "Sem conexão com a internet."
        return texto_conexao

if __name__ == '__main__':
    download_pfd()

