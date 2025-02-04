
from talhao import Talhao 
from trator import Trator
from typing import List, Optional

class Fazenda:
   def __init__(self):
    self.nome: str = ""
    self.area_ha: float = 0.0
    self.__tratores:List[Trator] = []

   def add_trator(self, trator: Trator):
    if int (trator.ano) < 2020:
      print ('Trator deve ser de 2020 ou mais...')
      pass

      self.__tratores.append(trator)
      print('Trator adicionado com sucesso!')

   def rem_trator(self, trator: Trator):
     self.__tratores.remove(trator)

   def list_tratores(self):
     if not self.__tratores:
       print(f'\n[{self.nome}] Não há tratores cadatrados\n')
     else:
      v_titulo = f'[{self.nome}] Lista de Tratores:'
      print(v_titulo)
      for t in self.__tratores:
        print('.'*len(v_titulo))
        t.imprimir()

      print('_'*len(v_titulo))

   

 





