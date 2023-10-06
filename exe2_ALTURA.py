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
    
    
    # Função 12: Retornar a altura de uma árvore
    def altura(self):
        return self._calcular_altura(self.raiz)

    def _calcular_altura(self, no):
        if no is None:
            return 0
        altura_esquerda = self._calcular_altura(no.esquerda)
        altura_direita = self._calcular_altura(no.direita)
        return 1 + max(altura_esquerda, altura_direita)


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


# Retorna a altura da árvore (Função 12)
altura_arvore = arvore.altura()
print(f"A altura da árvore é {altura_arvore}.")