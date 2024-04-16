class Trator:
  #criando o construtor da classe
  def __init__(self, marca, nome, torque, ano):
    self.marca = marca
    self.nome = nome
    self.torque = torque
    self.ano = ano
    self.__andando = True

  def imprimir(self):
    print(f'\n----------------')
    print(f"Marca.........: {self.marca}")
    print(f"Nome..........: {self.nome}")
    print(f'Torque........: {self.torque}')
    print(f'Ano........: {self.ano}')
    #print(f'Trator em movimento?........: {self.__andando}')
    print(f'\n----------------')


  def andar(self):
    self.__andando = True
    pass

  def parar(self):
    self.__andando = False
    pass

  def esta__andando (self):
   return self.__andando

  