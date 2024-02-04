import re
import os
from pathlib import Path
import csv

# ======================== Funções principais ===========================
def filtrar_portaria():
    _filtrar_portaria_ = str(*portaria)
    _filtrar_resolucao_ = str(*resolucao)

    portaria.clear()
    resolucao.clear()

    _filtrar_portaria_ = eliminar_virgula_no_texto_portaria(_filtrar_portaria_)
    _filtrar_resolucao_ = eliminar_virgula_no_texto_resolucao(_filtrar_resolucao_)

    if _filtrar_portaria_:
        portaria.append(_filtrar_portaria_)

    if _filtrar_resolucao_:
        portaria.append(_filtrar_resolucao_)

def filtrar_matricula():
    _filtrar_matricula_1 = re.sub(r'[a-zA-ZÀ-ú:,]', '' ,str(*matricula), flags=re.I)
    matricula.clear()
    _filtrar_matricula_2 = re.findall(r'\d{2}/\d{3}.\d{3}-\d', _filtrar_matricula_1)

    matricula.append(str(*_filtrar_matricula_2))

def filtrar_profissao():
    _filtrar_profissao_1 = re.findall(r'.+ matr', str(*profissao), flags=re.I)

    _filtrar_profissao_2 = re.sub(r'matr', '', str(*_filtrar_profissao_1), flags=re.I)

    profissao_string = _filtrar_profissao_2

    profissao.clear()
    variavel_auxiliar = ''
    for i in profissao_string:
        if i == ',':
            ...
        else:
            variavel_auxiliar += i

    profissao.append(variavel_auxiliar.strip())

def filtrar_nome():
        _filtrar_nome_ = str(*nome)
        nome.clear()

        variavel_auxiliar = ''
        iniciar = False
        for n1 in _filtrar_nome_:

            if n1.isupper():
                iniciar = True

            if n1 == ',':
                break

            if iniciar:
                if n1 == '-':
                    continue
                else:
                    variavel_auxiliar += n1

        nome.append(variavel_auxiliar)

def separar_em_paragrafo(caminho_arquivo):
    paragrafos = []

    with open(caminho_arquivo, 'r', encoding='utf8') as arquivo: # with (abre e fecha)
        texto = arquivo.read()

    for linha in texto.split("\n"):
        if linha:
            paragrafos.append(linha)
    return paragrafos

# ======================== Funções auxiliar ==========================
def eliminar_virgula_no_texto_portaria(texto_string):
    eliminar_virgula_texto_string = ''

    for letra in texto_string:
        if letra == ',':
            break

        eliminar_virgula_texto_string += letra

    return eliminar_virgula_texto_string.strip()

def eliminar_virgula_no_texto_resolucao(texto_string):
    eliminar_virgula_texto_string = ''

    for letra in texto_string:
        if letra == ',':
            continue
        else:
            eliminar_virgula_texto_string += letra

    return eliminar_virgula_texto_string.strip()

def unir_lista_em_um_texto(valor):
        lista = []
        variavel_auxiliar = ''
        for i in valor:
            variavel_auxiliar += i
            variavel_auxiliar += ' '
        lista = variavel_auxiliar.strip()
        return lista

# ======================== Iniciar ===========================

# caminho do arquivo
PASTA_RAIZ = Path(__file__).parent
PASTA_NOVA = PASTA_RAIZ / 'cadastro' / 'cadastro_texto.txt'

print(PASTA_NOVA)
minha_lista = separar_em_paragrafo(PASTA_NOVA)

for texto in minha_lista:
    # =============================== nome =====================================
    nome = re.findall(r'\bprov.+[\w]+', texto)
    filtrar_nome()
    print(nome)
    # ============================= inatividade ===============================
    inatividade = re.findall(r'inat.*-?e',texto, flags=re.I)
    if inatividade:
        inatividade = ['inativo']
        print(inatividade)
    else:
        inatividade = ['NÃO inativo']
        print(inatividade)
    # =============================== profissão ================================
    profissao = re.findall(r',.?[0-9A-ZÀ-ú,-].+',texto)
    filtrar_profissao()
    print(profissao)

    # ============================== matricula =================================
    matricula = re.findall(r'matr.+Apo', texto, flags=re.I)
    filtrar_matricula()
    print(matricula)

    # ============================= aposentando ================================
    aposentado = re.findall(r'\bapo.*do\b',texto, flags=re.I)
    aposentada = re.findall(r'\bapo.*da\b',texto, flags=re.I)
    if aposentada:
        aposentado = ['SIM aposentada']
        print(aposentado)
    elif aposentado:
        aposentado = ['SIM aposentado']
        print(aposentado)
    else:
        aposentado = ['NÃO aposentado(a)']
        print(aposentado)

    # ============================== portaria =================================
    portaria = re.findall(r'\bPor.*ria\b.*',texto, flags=re.I)
    resolucao = re.findall(r'\bres.*ão\b.*\d{4}\b\s?,',texto, flags=re.I)
    filtrar_portaria()
    print(portaria) # Portaria

    # =============================== processo ================================
    processo = re.findall(r'\bpro\s?-?ce\s?-?s\s?-?so\b.*',texto, flags=re.I)
    print(processo)
    # =========================================================================
    print('\n===========================================================\n')


    with open('meu_cadastro.txt', 'a', encoding='utf8') as arquivo: # with (abre e fecha)
        arquivo.write('\n===========================================================\n') # escrever no arquivo
        arquivo.write(f'Nome: {str(nome)}\n') # escrever no arquivo
        arquivo.write(f'Situação atual: {str(inatividade)}\n') # escrever no arquivo
        arquivo.write(f'Profissão: {str(profissao)}\n' ) # escrever no arquivo
        arquivo.write(f'Matricula: {str(matricula)}\n') # escrever no arquivo
        arquivo.write(f'Aposentadoria: {str(aposentado)}\n') # escrever no arquivo
        arquivo.write(f'Portaria ou Resolução: {str(portaria)}\n') # escrever no arquivo
        arquivo.write(f'Nome e data do processo: {str(processo)}\n') # escrever no arquivo






