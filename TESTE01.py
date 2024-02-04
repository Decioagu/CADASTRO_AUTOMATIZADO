import fitz
from pathlib import Path

# caminho do arquivo
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'pdfs_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'rio_de_janeiro_2024-01-10_completo.pdf'

doc = fitz.open(RELATORIO_BACEN) # abrir documento
print('Aguarde processamento...')
out = open("arquivo_texto.txt", "wb") # criar arquivo em texto
for page in doc: # iterar as páginas do documento
	text = page.get_text().encode("utf8") # obter texto simples (em UTF-8)
	out.write(text) # escrever o texto da página
	out.write(bytes((12,))) # escrever delimitador de página (feed de formulário 0x0C)
out.close()
print('FIM')
