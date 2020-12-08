# Para importar todo el modulo y cambiar el nombre
#import modulos as pr 
from modulos import saludo
from camelcase import CamelCase
# print(pr.lista) funciona si accede a todo el modulo
saludo("Jean")

c = CamelCase()
s = "Esta oracion necesita camelcase"

camelcased = c.hump(s)
print(camelcased)
