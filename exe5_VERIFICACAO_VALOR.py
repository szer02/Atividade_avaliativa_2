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

    # Função 5: Verificar se um certo valor n está presente na árvore
    def busca(self, valor):
        return self._busca_recursivamente(self.raiz, valor)

    def _busca_recursivamente(self, no, valor):
        if no is None:
            return False
        if valor == no.valor:
            return True
        if valor < no.valor:
            return self._busca_recursivamente(no.esquerda, valor)
        return self._busca_recursivamente(no.direita, valor)
    

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

# Verifica se um valor está presente na árvore (Função 5)
valor = 40
if arvore.busca(valor):
    print(f"\nO valor {valor} está presente na árvore.")
else:
    print(f"\nO valor {valor} não está presente na árvore.")