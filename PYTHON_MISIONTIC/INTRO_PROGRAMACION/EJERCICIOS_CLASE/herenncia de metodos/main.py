from dominio.clase_perro import Perro
from dominio.clase_abeja import Abeja
from dominio.clase_vaca import Vaca

mi_perro = Perro("mamífero", 10)
mi_vaca = Vaca("mamífero", 23)
mi_abeja = Abeja("insecto", 1)

mi_perro.hablar()
mi_vaca.hablar()
# Guau!
# Muuu!

mi_vaca.describeme()
mi_abeja.describeme()
# Soy un Animal del tipo Vaca
# Soy un Animal del tipo Abeja

mi_abeja.picar()
# Picar!
