import re

def separa_paragrafos(caminho_arquivo):

  paragrafos = []

  with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()

  for linha in texto.split("\n"):
    if linha:
      paragrafos.append(linha)
  return paragrafos

def encontra_paragrafos_selecionados(paragrafos):
  lista_de_paragrafos = []
  adicionar = False
  frase = ''

  for linha in paragrafos:

    if linha.startswith("Fixados com validade a partir de"):
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

caminho_arquivo = 'arquivo_texto.txt'

paginas = separa_paragrafos(caminho_arquivo)

paragrafos_selecionados = encontra_paragrafos_selecionados(paginas)

for n, i in enumerate(paragrafos_selecionados):
   print(f'{n + 1} = {i}\n\n')

caminho_arquivo = 'cadastro_texto.txt'
with open(caminho_arquivo, 'a', encoding='utf8') as arquivo: # with (abre e fecha)
    # arquivo.writelines(paragrafos_selecionados)
    for n,p in enumerate(paragrafos_selecionados):
      arquivo.write(f'{n + 1} = {p}\n\n')
