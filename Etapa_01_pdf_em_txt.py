import os
import fitz
from pathlib import Path

def pdf_em_txt():
    nova_pasta = Path() / 'pdf_em_txt'
    # criar pasta nova_pasta.
    nova_pasta.mkdir(exist_ok=True) # exist_ok=True para não da erro se existir pasta


    # caminho do arquivo
    PASTA_RAIZ = Path(__file__).parent
    PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
    PASTA_NOVA = PASTA_RAIZ / 'pdf_em_txt'

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

    ('FIM')

if __name__ == '__main__':
    pdf_em_txt()
