# -*- coding: utf-8 -*-
"""FARM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t-DfECCVkxBq-IHHuE0ZqcwuBY7VKSET
"""

class Farmacia:
    def __init__(self, nomefarm, numerofarm, emailfarm, horariofuncionamento, registrofarm, CNPJ, licencasanitaria,
                 resptec, numresptec, ultimoganho, ganhos):
        self.nomefarm = nomefarm
        self.numerofarm = numerofarm
        self.emailfarm = emailfarm
        self.horariofuncionamento = horariofuncionamento
        self.registrofarm = registrofarm
        self.CNPJ = CNPJ
        self.licencasanitaria = licencasanitaria
        self.resptec = resptec
        self.numresptec = numresptec
        self.ultimoganho = ultimoganho
        self.ganhos = ganhos

    def atualizar_ganhos(self, preco):
        self.ultimoganho = self.ganhos
        self.ganhos += preco

paguemais= Farmacia("Paguemais", "85 99242-4132", "Paguemaislevemais@gmail.com", "8:00 - > 12:00, 14:00 -> 22:00", "06.626.253/0001-51" ,"30.680.478/0001-70", "licença poggers", "Rycharlisson", "85 99242-4131", 00.00, 00.00)

class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def compra(self, Produto, funcionario):
        print(f"{self.nome} está comprando {Produto.nome}")
        quantidade = int(input("digite a quantidade para a compra: "))
        quantidadedada = True
        funcionario.vender(quantidade, Produto, quantidadedada)

    def exibeinfo(self):
        print(f'o nome do cliente é {self.nome}, o cpf dele é {self.cpf}, o endereço é {self.endereco}')

alucar = Cliente('ronaldo' , '093.364.195.46' , 'umirim')
alucar.compra(citalopram, edu)

quantidadedada = False
comprafeita= False
class Funcionario(Farmacia):
  def __init__(self, nome, cpf, num_crachar, atendendo=False):
        self.nome = nome
        self.cpf = cpf
        self.num_crachar = num_crachar
        self.atendendo = atendendo
        super().__init__(nomefarm='', numerofarm='', emailfarm='', horariofuncionamento='', registrofarm='',
                         CNPJ='', licencasanitaria='', resptec='', numresptec='', ultimoganho=0, ganhos=0)


  def atender(self):
    if self.atendendo == False:
      self.atendendo = True
    else:
      print(f'o {self.nome} não pode atender agora.')

  def vender(self, quantidade, Produto, quantidadedada):
    while comprafeita == False:
      if quantidadedada == True:
        preco = Produto.get_preco() * quantidade
        paguemais.atualizar_ganhos(preco)
      else:
        quantidade = int(input(f"Digite a quantidade de {Produto.nome} para a venda: "))
        preco = Produto.get_preco() * quantidade
        paguemais.atualizar_ganhos(preco)

      if quantidade > 1:
        print(f'foram vendidas {quantidade} unidades de {Produto.nome}, faturando R${preco:.2f}')
        break
      elif quantidade == 1:
        print(f'foi vendida {quantidade} unidade de {Produto.nome}, faturando R${preco:.2f}')
        break
      else:
          print(f'Erro, tente novamente')

edu = Funcionario('Eduardo', '753.153.257.09', '53892', paguemais)

edu.vender(1, citalopram, quantidadedada)
print("o ganho da farmacia atualmente é:", paguemais.ganhos)
print(paguemais.ultimoganho)

class Fornecedora:
  def __init__(self,nomefornecedora,cnpj,endereco):
    self.nomefornecedora = nomefornecedora
    self.cpnj = cnpj
    self.endereco = endereco

fornecedora_do_governo = Fornecedora("Gover", "0390", "29188")

class Produto:
  def __init__(self,nome,descricao,preco,fornecedora,dataV):
    self.fornecedora = fornecedora.nomefornecedora
    self.nome = nome
    self.descricao = descricao
    self.preco = preco
    self.dataV = dataV

  def get_preco(self):
    return self.preco

citalopram = Produto("citalopram", "Remedio usado para tratamento antidepressivo", 10.00, fornecedora_do_governo, "20/12/2024")