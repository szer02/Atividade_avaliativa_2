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

    # Função 2: Percorrer a árvore, imprimindo os valores dos nós (em ordem)
    def em_ordem(self):
        self._em_ordem_recursivamente(self.raiz)

    def _em_ordem_recursivamente(self, no):
        if no is not None:
            self._em_ordem_recursivamente(no.esquerda)
            print(no.valor)
            self._em_ordem_recursivamente(no.direita)



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

# Percorre a árvore e imprime os valores dos nós (Função 2 - Em ordem)
print("Percorrendo a árvore em ordem:")
arvore.em_ordem()
