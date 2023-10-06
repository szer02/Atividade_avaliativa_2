class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    # Função para inserir elementos na árvore
    def inserir_elementos(self, elementos):
        for elemento in elementos:
            self.inserir(elemento)

    def inserir(self, valor):
        self.raiz = self._inserir_recursivamente(self.raiz, valor)

    def _inserir_recursivamente(self, no, valor):
        if no is None:
            return No(valor)
        if valor < no.valor:
            no.esquerda = self._inserir_recursivamente(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._inserir_recursivamente(no.direita, valor)
        return no

    # Função para calcular a média dos valores presentes na árvore
    def calcular_media(self):
        valores = []
        self._em_ordem(self.raiz, valores)
        if not valores:
            return None
        soma = sum(valores)
        return soma / len(valores)

    # Função auxiliar para percorrer a árvore em ordem
    def _em_ordem(self, no, valores):
        if no is not None:
            self._em_ordem(no.esquerda, valores)
            valores.append(no.valor)
            self._em_ordem(no.direita, valores)

# Cria uma instância da árvore
arvore = ArvoreBinariaBusca()

# Insere os elementos na árvore
elementos = [50, 30, 70, 20, 40, 60, 80]
arvore.inserir_elementos(elementos)

# Calcula a média dos valores na árvore
media = arvore.calcular_media()
print(f"A média dos valores na árvore é {media}.")
