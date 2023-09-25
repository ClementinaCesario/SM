# Classe para representar um nó na árvore de Huffman
class NoHuffman:
    def __init__(self, caractere=None, frequencia=None):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return f"Caractere: {self.caractere}, Frequência: {self.frequencia}"

# Função para calcular as frequências de cada caractere no arquivo de entrada
def calcular_frequencias(arquivo_entrada):
    frequencias = {}
    with open(arquivo_entrada, 'r') as arquivo:
        dados = arquivo.read()
        for caractere in dados:
            if caractere in frequencias:
                frequencias[caractere] += 1
            else:
                frequencias[caractere] = 1
    return frequencias

# Função para construir a árvore de Huffman
def construir_arvore_huffman(frequencias):
    nos = [NoHuffman(caractere, frequencia) for caractere, frequencia in frequencias.items()]

    while len(nos) > 1:
        nos.sort(key=lambda x: x.frequencia)
        esquerda = nos.pop(0)
        direita = nos.pop(0)
        pai = NoHuffman(frequencia=esquerda.frequencia + direita.frequencia)
        pai.esquerda = esquerda
        pai.direita = direita
        nos.append(pai)

    return nos[0]

# Função para gerar códigos de Huffman
def gerar_codigos_huffman(raiz, codigo_atual="", codigos={}):
    if raiz is None:
        return

    if raiz.caractere is not None:
        codigos[raiz.caractere] = codigo_atual
        return

    gerar_codigos_huffman(raiz.esquerda, codigo_atual + '0', codigos)
    gerar_codigos_huffman(raiz.direita, codigo_atual + '1', codigos)

# Função para imprimir a árvore Huffman
def imprimir_arvore_huffman(raiz, nivel=0):
    if raiz is not None:
        print("  " * nivel + str(raiz))
        imprimir_arvore_huffman(raiz.esquerda, nivel + 1)
        imprimir_arvore_huffman(raiz.direita, nivel + 1)

# Função para comprimir o arquivo de entrada
def huffman_comprimir(arquivo_entrada, arquivo_saida):
    frequencias = calcular_frequencias(arquivo_entrada)
    raiz = construir_arvore_huffman(frequencias)
    codigos = {}
    gerar_codigos_huffman(raiz, "", codigos)

    with open(arquivo_entrada, 'r') as arquivo_entrada, open(arquivo_saida, 'wb') as arquivo_saida:
        dados = arquivo_entrada.read()
        dados_comprimidos = ''.join([codigos[caractere] for caractere in dados])

        # Adicionar zeros à direita para preencher um múltiplo de 8 bits
        while len(dados_comprimidos) % 8 != 0:
            dados_comprimidos += '0'

        # Converter a sequência de bits em bytes e escrever no arquivo de saída
        array_de_bytes = bytearray()
        for i in range(0, len(dados_comprimidos), 8):
            byte = dados_comprimidos[i:i + 8]
            valor_do_byte = int(byte, 2)
            array_de_bytes.append(valor_do_byte)
        arquivo_saida.write(bytes(array_de_bytes))

# Função para descomprimir o arquivo
def huffman_descomprimir(arquivo_entrada, arquivo_saida, raiz):
    with open(arquivo_entrada, 'rb') as arquivo_entrada_bin, open(arquivo_saida, 'w') as arquivo_saida_texto:
        dados_comprimidos = ""
        byte = arquivo_entrada_bin.read(1)
        while byte:
            dados_comprimidos += bin(int.from_bytes(byte, byteorder='big'))[2:].rjust(8, '0')
            byte = arquivo_entrada_bin.read(1)

        no_atual = raiz
        for bit in dados_comprimidos:
            if bit == '0':
                no_atual = no_atual.esquerda
            else:
                no_atual = no_atual.direita

            if no_atual.caractere is not None:
                arquivo_saida_texto.write(no_atual.caractere)
                no_atual = raiz

# Exemplo de uso
arquivo_entrada = "SM - Huffman.txt"
arquivo_comprimido = "SM - Huffman_comprimido.bin"
arquivo_descomprimido = "SM - Huffman_descomprimido.txt"

frequencias = calcular_frequencias(arquivo_entrada)
raiz = construir_arvore_huffman(frequencias)

# Comprimir o arquivo de entrada
huffman_comprimir(arquivo_entrada, arquivo_comprimido)
print("Arquivo comprimido com sucesso.")

# Descomprimir o arquivo comprimido
huffman_descomprimir(arquivo_comprimido, arquivo_descomprimido, raiz)
print("Arquivo descomprimido com sucesso.\n")

# Exibir a árvore de Huffman
imprimir_arvore_huffman(raiz)