def calcular_probabilidades_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()
    frequencias = {}
    total_caracteres = len(texto)

    for caractere in texto:
        if caractere in frequencias:
            frequencias[caractere] += 1
        else:
            frequencias[caractere] = 1

    probabilidades = {simbolo: frequencia / total_caracteres for simbolo, frequencia in frequencias.items()}
    return probabilidades

def comprimir(texto, tabela):
    codigo_comprimido = ""
    for caractere in texto:
        codigo_comprimido += tabela[caractere]
    return codigo_comprimido

def descomprimir(codigo_comprimido, tabela):
    texto_descomprimido = ""
    codigo_temporario = ""
    for bit in codigo_comprimido:
        codigo_temporario += bit
        for simbolo, codigo in tabela.items():
            if codigo_temporario == codigo:
                texto_descomprimido += simbolo
                codigo_temporario = ""
                break
    return texto_descomprimido

def criar_tabela_shannon_fano(probabilidades):
    simbolos_ordenados = sorted(probabilidades.keys(), key=lambda simbolo: probabilidades[simbolo], reverse=True)
    tabela = {}

    def construir_tabela(simbolos):
        if len(simbolos) == 1:
            return

        meio = len(simbolos) // 2
        for simbolo in simbolos[:meio]:
            tabela[simbolo] = tabela.get(simbolo, '') + '0'
        for simbolo in simbolos[meio:]:
            tabela[simbolo] = tabela.get(simbolo, '') + '1'

        construir_tabela(simbolos[:meio])
        construir_tabela(simbolos[meio:])

    construir_tabela(simbolos_ordenados)
    return tabela

def comprimir_arquivo(nome_arquivo, tabela, nome_arquivo_comprimido):
    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()

    codigo_comprimido = comprimir(texto, tabela)

    with open(nome_arquivo_comprimido, 'w') as arquivo_comprimido:
        arquivo_comprimido.write(codigo_comprimido)

def descomprimir_arquivo(nome_arquivo_comprimido, tabela, nome_arquivo_descomprimido):
    with open(nome_arquivo_comprimido, 'r') as arquivo_comprimido:
        codigo_comprimido = arquivo_comprimido.read()

    texto_descomprimido = descomprimir(codigo_comprimido, tabela)

    with open(nome_arquivo_descomprimido, 'w') as arquivo_descomprimido:
        arquivo_descomprimido.write(texto_descomprimido)


# Exemplo de uso:
nome_arquivo_original = 'SM - Shanon Fano.txt'
probabilidades = calcular_probabilidades_arquivo(nome_arquivo_original)
tabela = criar_tabela_shannon_fano(probabilidades)

# Impressao da tabela
print(tabela)

nome_arquivo_comprimido = 'SM - Shanon Fano_comprimido.txt'
comprimir_arquivo(nome_arquivo_original, tabela, nome_arquivo_comprimido)
print("Arquivo comprimido com sucesso.")

nome_arquivo_descomprimido = 'SM - Shanon Fano_descomprimido.txt'
descomprimir_arquivo(nome_arquivo_comprimido, tabela, nome_arquivo_descomprimido)
print("Arquivo descomprimido com sucesso.")