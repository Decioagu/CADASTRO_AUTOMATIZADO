import re
import os
from pathlib import Path

# ============================= Funções ================================
def separar_arquivo_pdf_em_linhas(caminho_arquivo):
    print('separa em paragrafos...')

    # separa cada linha do "arquivo_txt" em uma grande lista chama "paragrafos"
    paragrafos = []

    # abrir e fechar arquivo "caminho_arquivo" = "arquivo_txt"
    with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
        texto = arquivo.read() # ler arquivo

    for linha in texto.split("\n"): # quando houver quebra de linha
        if linha:
            paragrafos.append(linha) # adicionar na lista
            # print(paragrafos)

    return paragrafos # retornar lista

def selecionar_paragrafos_cadastro_de_clientes(paragrafos):
    print('selecionar paragrafo ...')

    # regra de negocio, separa os paragrafos na "lista_de_paragrafos" iniciado com "processo_1"
    lista_de_paragrafos = []
    adicionar = False
    frase = ''

    for linha in paragrafos:
        # 1º filtro: iniciar quando...
        processo_1 = re.findall(r'Fixados com validade a partir de.*', linha, flags=re.I)
        if processo_1:
            frase = frase + linha
            adicionar = True
        elif adicionar:
            frase = frase + linha

        # 2º filtro: finalizar quando...
        processo_2 = re.findall(r'pro.?-?ce.?-?s.?-?so.*\.$', frase, flags=re.I)
        if processo_2:
            lista_de_paragrafos.append(frase)
            adicionar = False
            frase = ''

        # ================= filtro de exceção a regra =================
        '''
        Hove texto que não finalizava do "." final
        '''
        # 3º filtro: finalizar quando...
        processo_3 = re.findall(r'\d{2}/\d{2}/\d{3}.\d{3}/\d{4}', frase, flags=re.I)
        if processo_3:
            lista_de_paragrafos.append(frase)
            adicionar = False
            frase = ''
    # ==============================================================
    return lista_de_paragrafos # retornar lista

# ======================== Iniciar Programa ===========================
def selecionar_paragrafo():

    # caminho da pasta raiz
    PASTA_RAIZ = Path(__file__).parent

    nova_pasta = PASTA_RAIZ / 'CADASTROS' # criar pasta nova_pasta.
    nova_pasta.mkdir(exist_ok=True) # exist_ok=True para não da erro se existir pasta

    # caminho do arquivo
    PASTA_NOVA = PASTA_RAIZ / 'PDF_EM_TXT'

    # finalizar caso pasta não exista pasta
    if not os.path.exists(f'{PASTA_NOVA}'):
        return

    # =========================== Gerar arquivo TXT ===========================
    # transforma em lista todos os arquivos existente na pasta
    for num , arquivo_txt in enumerate(os.listdir(PASTA_NOVA), start=1):
        print('<=====================================================>')
        print(f'Analizar arquivo {num} =', arquivo_txt)

        # se extensão do arquivo for ".txt"
        if arquivo_txt.endswith(".txt"):
            # abrir e fechar arquivo
            with open(os.path.join(PASTA_NOVA, arquivo_txt), "r") as f:

                # Caminho
                ACESSO_ARQUIVOS = PASTA_NOVA / arquivo_txt

                print('Aguarde processamento...')

                # Funções
                arquivo_pdf_em_linhas_txt = separar_arquivo_pdf_em_linhas(ACESSO_ARQUIVOS)

                # Funções
                paragrafos_selecionados = selecionar_paragrafos_cadastro_de_clientes(arquivo_pdf_em_linhas_txt)

                # separa "paragrafos_selecionados" com duas quebra de linhas
                for n, i in enumerate(paragrafos_selecionados):
                    print(f'{n + 1} = {i}\n\n')

                # abrir e fechar arquivo
                with open(nova_pasta / 'cadastro_texto.txt', 'a', encoding='utf8') as arquivo:
                    # salvar arquivo texto "cadastro_texto.txt"
                    for n,p in enumerate(paragrafos_selecionados):
                        arquivo.write(f'{n + 1} = {p}\n\n')
        print('Processo finalizado...')

# mensagem final
print('FIM Etapa_02_selecionar_paragrafo...')

if __name__ == '__main__':
    selecionar_paragrafo()
