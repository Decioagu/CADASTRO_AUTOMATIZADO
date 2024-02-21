import requests
url = "https://doweb.rio.rj.gov.br/"

def verifica_conexao_internet():
    try:
        # Faz uma requisição para o Google
        requests.get(url, timeout=5)
        return True
    except requests.ConnectionError:
        # Se a requisição falhar, retorna False
        return False

if verifica_conexao_internet():
    print("Conectado à internet!")
    texto = "Conectado à internet!"
else:
    print("Sem conexão com a internet.")
    texto = "Sem conexão com a internet."
