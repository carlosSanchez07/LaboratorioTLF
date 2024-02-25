from matplotlib import pyplot as plt
from matplotlib_venn import venn3


#Se crean los sets(conjuntos) para realizar las operaciones
a = {1, 2, 3, 4, 5}
b = {3, 5, 6, 8, 9}
d = {5, 3, 8, 7, 10}

#Al metodo venn 3 se le mandan los 3 sets y sus respectivas etiquetas
venn3((a,b,d),("a","b","d"))
#Se muestra el diagrama por el entorno gráfico
plt.show()

# -------- METODOS -------------

# Método para la Unión de dos conjuntos
def unionConjuntos(a, b):
    c = []
    for elemento in a:
        c.append(elemento)

    for i in b:
        if i not in c:
            c.append(i)
    return c
#Resultado de la unión
print("U:", unionConjuntos(a, b))

#Método para la interseccion de dos conjuntos
def interseccion(a,b):
    c = []
    for i in a:
      if i in b:
         c.append(i)
    return(c)
print("n: ",interseccion(a,b))

# ejemplo de complemento con caracteres
def realizarCompleto():
    u = ["a","e","i","o","u"]
    a = ["a","i","u"]
    b = []
    for i in u:
      if i not in a:
        b.append(i)
    return b
print("Complemento de a: ", realizarCompleto())

# Método para la diferencia de dos conjuntos
def restarConjuntos(a, b):
    c = []
    for elemento in a:
        c.append(elemento)

    for i in c:
        if i in b:
            c.remove(i)
    return c
#Resultado de la diferencia
print("A-B: ",restarConjuntos(a, b))

# Combinación entre operaciones
r = []
# a u (b - d)
r = restarConjuntos(b, d)
#Resultado de  a u (b - d)
print("a u (b - d): ",unionConjuntos(a, r))

# Cardinalidad
print("cardinalidad de a: ", len(a))

# Subconjuntos
def definirSubConjunto(a, b):
    f = False
    for i in a:
        if i not in b:
            return f
    f = True
    return f
#Definimos si a es subconjunto de b
if definirSubConjunto(a, b) is False:
    print("No es subconjunto")
else:
    print("Si es subconjunto")

#Metodo para determinar si es un Disjunto
def definirDisjunto(a, b):
    for i in a:
        if i in b:
            return True
    return False
#Definimos si a es disjunto de b
if definirDisjunto(a, b) is False:
    print("Si es disjunto")
else:
    print("No es disjunto")

ventana_principal.mainloop()