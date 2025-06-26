
from Produto import Produto

class Produto_alimenticio(Produto):
    def __init__(self, nome, preco, quantidade, data_validade):
        super().__init__(nome, preco, quantidade)
        self.data_validade = data_validade

    def exibir_produtos(self):
        super().exibir_produtos()
        print(f'Data de validade: {self.data_validade}')
