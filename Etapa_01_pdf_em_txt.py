import os
import fitz
from pathlib import Path

'''
pip install fitz
A instrução em Python traz o módulo da biblioteca PyMuPDF para o seu código atual.
PyMuPDF é uma biblioteca poderosa que lhe permite interagir com documentos PDF
de várias maneiras.import fitz

Módulo "fitz" é parcialmente instalado ao instalar "pip install PyMuPDF"
'''

def pdf_em_txt():

    # caminho da pasta raiz
    PASTA_RAIZ = Path(__file__).parent

    nova_pasta = PASTA_RAIZ / 'PDF_EM_TXT' # criar pasta nova_pasta.
    nova_pasta.mkdir(exist_ok=True)  # exist_ok=True para não da erro se existir pasta (criar nova pasta)
    PASTA_NOVA = nova_pasta # caminho nova_pasta.

    PASTA_ORIGINAIS = PASTA_RAIZ / 'PDF' # caminho do arquivo

    # finalizar caso pasta não exista pasta
    if not os.path.exists(f'{PASTA_ORIGINAIS}'):
        return

    # transforma em lista todos os arquivos existente na pasta
    for num , arquivo_pdf in enumerate(os.listdir(PASTA_ORIGINAIS), start=1):
        print('<=====================================================>')
        print(f'Analizar arquivo {num} =', arquivo_pdf)

        # se extensão do arquivo for ".pdf"
        if arquivo_pdf.endswith(".pdf"):
            # abrir e fechar arquivo
            with open(os.path.join(PASTA_ORIGINAIS, arquivo_pdf), "r") as f:

                ACESSO_ARQUIVOS = PASTA_ORIGINAIS / arquivo_pdf # caminho

                doc = fitz.open(ACESSO_ARQUIVOS) # abrir documento PDF

                print('Aguarde processamento...')

                out = open(PASTA_NOVA / f"arquivo_{arquivo_pdf}_texto_{num}.txt", "wb") # abrir e criar "arquivo em texto"
                for page in doc: # iterar as páginas do documento
                    text = page.get_text().encode("utf8") # obter texto simples (em UTF-8)
                    out.write(text) # escrever o texto da página
                    out.write(bytes((12,))) # escrever delimitador de página (feed de formulário 0x0C)
                out.close() # fechar ao finalizar "arquivo em texto"
                print('Processo finalizado...')

# mensagem final
print('FIM Etapa_01_pdf_em_txt...')

if __name__ == '__main__':
    pdf_em_txt()
