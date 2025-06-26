
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def exibir_produtos(self):
        print('-'*45)
        print(f'Nome: {self.nome}\nPreço: {self.preco} \nQuantidade: {self.quantidade}\n')

    def repor_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f'Estoque de {self.nome} atualizado. Nova quantidade: {self.quantidade}')

    def vender(self, quantidade):
        if self.quantidade >= quantidade:
            self.quantidade -= quantidade
            print(f'Venda realizada. {quantidade} unidades de {self.nome} vendidas.')
        else:
            print(f'Estoque insuficiente para {self.nome}. Quantidade disponível: {self.quantidade}')
