from fazenda import Fazenda
from trator import Trator  




if __name__ == '__main__':
  trator1 = Trator('Ford', 'F-150', 2021, '150')
  trator2 = Trator('John Deere', 'F-300', 2024, '350')

  faz1= Fazenda()
  faz1.nome = 'Fazenda Lambari'
  faz1.area_ha = 5000
  faz1.add_trator(trator1)
  faz1.add_trator(trator2)
  faz1.list_tratores()




