# manier 1 - importeer de volledige module
import math

# roep een functie uit de module aan door de naam van de module te gebruiken
math.sqrt(16)

# manier 2 - importeer de volledige module, gebruik een alias voor de module
import math as m
# dit maakt het mogelijk om de module aan te roepen met een kortere naam
m.sqrt

# manier 3 - importeer een specifieke functie uit de module
from math import sqrt
# roep de geïmporteerde functie rechstreeks aan zonder de naam van de module
sqrt(16)

