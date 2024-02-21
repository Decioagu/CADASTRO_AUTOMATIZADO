import re
import os
from pathlib import Path

# ============================= Funções ================================
def separar_arquivo_pdf_em_linhas(caminho_arquivo):
  print('separa em paragrafos...')

  paragrafos = []

  with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()

  for linha in texto.split("\n"):
    if linha:
      paragrafos.append(linha)
  return paragrafos

def selecionar_paragrafos_cadastro_de_clientes(paragrafos):
  print('selecionar paragrafo ...')

  lista_de_paragrafos = []
  adicionar = False
  frase = ''

  for linha in paragrafos:

    processo0 = re.findall(r'Fixados com validade a partir de.*', linha, flags=re.I)
    if processo0:
        frase = frase + linha
        adicionar = True
    elif adicionar:
        frase = frase + linha

    processo1 = re.findall(r'pro.?-?ce.?-?s.?-?so.*\.$', frase, flags=re.I)
    if processo1:
       lista_de_paragrafos.append(frase)
       adicionar = False
       frase = ''

    # ================= filtro de exceção a regra =================
    processo2 = re.findall(r'\d{2}/\d{2}/\d{3}.\d{3}/\d{4}', frase, flags=re.I)
    if processo2:
       lista_de_paragrafos.append(frase)
       adicionar = False
       frase = ''
    # ==============================================================
  return lista_de_paragrafos

# ======================== Iniciar programa ===========================

def selecionar_paragrafo():
    nova_pasta = Path() / 'cadastro'
    # criar pasta nova_pasat.
    nova_pasta.mkdir(exist_ok=True) # exist_ok=True para não da erro se existir pasta

    # caminho do arquivo
    PASTA_RAIZ = Path(__file__).parent
    PASTA_NOVA = PASTA_RAIZ / 'pdf_em_txt'

    caminho_arquivo = 'arquivo_texto.txt'

    # =========================== Gerar arquivo TXT ===========================

    for num , arquivo_txt in enumerate(os.listdir(PASTA_NOVA)):
        if arquivo_txt.endswith(".txt"):
            with open(os.path.join(PASTA_NOVA, arquivo_txt), "r") as f:

                ACESSO_ARQUIVOS = PASTA_NOVA / arquivo_txt

                print('Aguarde processamento...')

                arquivo_pdf_em_linhas_txt = separar_arquivo_pdf_em_linhas(ACESSO_ARQUIVOS)

                paragrafos_selecionados = selecionar_paragrafos_cadastro_de_clientes(arquivo_pdf_em_linhas_txt)

                for n, i in enumerate(paragrafos_selecionados):
                    print(f'{n + 1} = {i}\n\n')

                with open(nova_pasta / 'cadastro_texto.txt', 'a', encoding='utf8') as arquivo: # with (abre e fecha)
                    # arquivo.writelines(paragrafos_selecionados)
                    for n,p in enumerate(paragrafos_selecionados):
                        arquivo.write(f'{n + 1} = {p}\n\n')
        print('Processo finalizado...')

    print('FIM...')

if __name__ == '__main__':
    selecionar_paragrafo()
