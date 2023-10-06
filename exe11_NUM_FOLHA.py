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

    # Função 11: Retornar o número de folhas de uma árvore
    def numero_folhas(self):
        return self._contar_folhas_recursivamente(self.raiz)

    def _contar_folhas_recursivamente(self, no):
        if no is None:
            return 0
        if no.esquerda is None and no.direita is None:
            return 1
        return self._contar_folhas_recursivamente(no.esquerda) + self._contar_folhas_recursivamente(no.direita)


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


# Retorna o número de folhas na árvore (Função 11)
numero_folhas = arvore.numero_folhas()
print(f"O número de folhas na árvore é {numero_folhas}.")
