import re

# ======================== Funções principais ===========================
def filtrar_portaria():
    _filtrar_portaria_ = str(*portaria)

    portaria.clear()

    _filtrar_portaria_ = eliminar_virgula_no_texto(_filtrar_portaria_)

    portaria.append(_filtrar_portaria_)

def filtrar_matricula():
    _filtrar_matricula_ = re.sub(r'[a-zA-ZÀ-ú:,]', '' ,str(*matricula), flags=re.I)

    matricula.clear()

    # ================= filtro de exceção a regra =================
    variavel_auxiliar = ''
    for n, i in enumerate(_filtrar_matricula_):
        if n == 16:
            break
        variavel_auxiliar += i
    # ==============================================================

    matricula.append(variavel_auxiliar.strip())

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
        _filtrar_nome_ = re.findall(r'[A-ZÀ-ú-]+.,?', str(*nome))

        nome_filtrado = []
        for n1 in _filtrar_nome_:
            nome_filtrado.append(n1)
            if ',' in n1:
                nome.clear()
                break

        unir_nome = unir_lista_em_um_texto(nome_filtrado)

        eliminar_virgula = eliminar_virgula_no_texto(unir_nome)

        nome.append(eliminar_virgula)

def separar_em_paragrafo(caminho_arquivo):
    paragrafos = []

    with open(caminho_arquivo, 'r', encoding='utf8') as arquivo: # with (abre e fecha)
        texto = arquivo.read()

    for linha in texto.split("\n"):
        if linha:
            paragrafos.append(linha)
    return paragrafos

# ======================== Funções auxiliar ==========================
def eliminar_virgula_no_texto(texto_string):
    eliminar_virgula_texto_string = ''

    for letra in texto_string:
        if letra == ',':
            break

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
caminho_arquivo = 'aula2.txt'
minha_lista = separar_em_paragrafo(caminho_arquivo)

for texto in minha_lista:
    # ============================= inatividade ===============================
    inatividade = re.findall(r'inat.*-?e',texto, flags=re.I)
    if inatividade:
        inatividade = ['inatividade']
        print(inatividade)
    else:
        inatividade = ['NÃO inatividade']
        print(inatividade)
    # =============================== nome =====================================
    nome = re.findall(r'prov.+[A-ZÀ-ú]+.?,', texto)
    filtrar_nome()
    print(nome)
    # =============================== profissão ================================
    profissao = re.findall(r',.?[0-9A-ZÀ-ú,-].+',texto)
    filtrar_profissao()
    print(profissao)

    # ============================== matricula =================================
    matricula = re.findall(r'matr.+Apo', texto, flags=re.I)
    filtrar_matricula()
    print(matricula)

    # ============================= aposentando ================================
    aposentado = re.findall(r'apos.*-?ado',texto, flags=re.I)
    aposentada = re.findall(r'apos.*-?ada',texto, flags=re.I)
    if aposentada:
        aposentada = ['aposentada']
        print(aposentada)
    elif aposentado:
        aposentado = ['aposentado']
        print(aposentado)
    else:
        aposentada = ['NÃO aposentado(a)']
        print(aposentada)

    # ============================== portaria =================================
    portaria = re.findall(r'Por.?-?ta.?-?ria.*',texto, flags=re.I)
    filtrar_portaria()
    print(portaria) # Portaria

    # =============================== processo ================================
    processo = re.findall(r'pro.?-?ce.?-?s.?-?so.*',texto, flags=re.I)
    print(processo)
    # =========================================================================
    print('\n===========================================================\n')

# escrever arquivo CSV (como dicionário)
# import csv

# with open('data2.csv', 'w', newline='' , encoding='utf8') as arquivo_csv:
#     inatividade
#     dados = ['nome', 'idade', 'cidade']
#     writer = csv.DictWriter(arquivo_csv, fieldnames=dados) # modo de gravação
#     writer.writeheader() # método para escrever a linha de cabeçalho de um arquivo CSV (fieldnames=)
#     writer.writerow({'nome': 'Alice', 'idade': 30, 'cidade': 'Seattle'}) # escrever uma linha
#     writer.writerow({'nome': 'Bob', 'idade': 25, 'cidade': 'New York'}) # escrever uma linha

