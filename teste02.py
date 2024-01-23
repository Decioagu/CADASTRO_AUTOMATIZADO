def separa_paragrafos(caminho_arquivo):
  
  paragrafos = []
  
  with open(caminho_arquivo, 'r', encoding='utf8') as arquivo: # with (abre e fecha)
    texto = arquivo.read() 
 
  for linha in texto.split("\n"):
    if linha:
      paragrafos.append(linha)
  return paragrafos


def encontra_paragrafos_fixados(paragrafos):
  paragrafos_fixados = []
  adicionar = False
  frase = ''
  for linha in paragrafos:
    
    if linha.startswith("Fixados com validade a partir de"):
        frase = frase + linha
        adicionar = True
    elif adicionar:
        frase = frase + linha

    if 'nº' in frase:
       paragrafos_fixados.append(frase)
       adicionar = False
       frase = ''

  return paragrafos_fixados




caminho_arquivo = 'aula1.txt'

paragrafos = separa_paragrafos(caminho_arquivo)
paragrafos_fixados = encontra_paragrafos_fixados(paragrafos)

for n, i in enumerate(paragrafos_fixados):
   print(f'{n + 1} = {i}\n\n')

caminho_arquivo = 'aula2.txt'
with open(caminho_arquivo, 'a', encoding='utf8') as arquivo: # with (abre e fecha)
    # arquivo.writelines(paragrafos_fixados)
    for n,p in enumerate(paragrafos_fixados):
      arquivo.write(f'{n + 1} = {p}\n\n')   
