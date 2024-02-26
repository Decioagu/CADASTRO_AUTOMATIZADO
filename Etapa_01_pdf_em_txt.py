import os
import fitz
from pathlib import Path

def pdf_em_txt():

    # caminho da pasta raiz
    PASTA_RAIZ = Path(__file__).parent

    nova_pasta = PASTA_RAIZ / 'PDF_EM_TXT' # criar pasta nova_pasta.
    nova_pasta.mkdir(exist_ok=True) # exist_ok=True para não da erro se existir pasta

    PASTA_NOVA = nova_pasta # caminho nova_pasta.

    PASTA_ORIGINAIS = PASTA_RAIZ / 'PDF' # caminho do arquivo

    if not os.path.exists(f'{PASTA_ORIGINAIS}'):
        return

    for num , arquivo_pdf in enumerate(os.listdir(PASTA_ORIGINAIS), start=1):
        if arquivo_pdf.endswith(".pdf"):
            with open(os.path.join(PASTA_ORIGINAIS, arquivo_pdf), "r") as f:

                ACESSO_ARQUIVOS = PASTA_ORIGINAIS / arquivo_pdf

                doc = fitz.open(ACESSO_ARQUIVOS) # abrir documento

                print('Aguarde processamento...')

                out = open(PASTA_NOVA / f"arquivo_{arquivo_pdf}_texto_{num}.txt", "wb") # criar arquivo em texto
                for page in doc: # iterar as páginas do documento
                    text = page.get_text().encode("utf8") # obter texto simples (em UTF-8)
                    out.write(text) # escrever o texto da página
                    out.write(bytes((12,))) # escrever delimitador de página (feed de formulário 0x0C)
                out.close()
                print('Processo finalizado...')

print('FIM Etapa_01_pdf_em_txt...')

if __name__ == '__main__':
    pdf_em_txt()
