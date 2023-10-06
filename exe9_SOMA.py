class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    # Função 1: Inserir um elemento em uma árvore binária de busca
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

    # Função 9: Retornar a soma dos valores dos nós
    def _obter_valores_em_ordem(self, no, valores):
        if no is not None:
            self._obter_valores_em_ordem(no.esquerda, valores)
            valores.append(no.valor)
            self._obter_valores_em_ordem(no.direita, valores)

    def soma_valores(self):
        valores = []
        self._obter_valores_em_ordem(self.raiz, valores)
        return sum(valores) if valores else 0

# Cria uma instância da árvore
arvore = ArvoreBinariaBusca()

# Insere elementos na árvore (Função 1)
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

# Retorna a soma dos valores dos nós (Função 9)
soma = arvore.soma_valores()
print(f"A soma dos valores na árvore é {soma}.")
