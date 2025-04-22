#Script_BigTree
#Ricardo Sneyder Rincón Gamboa - 2210639
# Importamos las funciones necesarias de la biblioteca bigtree
from bigtree import Node, print_tree

#Ejemplo:

#Crear el nodo raíz
reino = Node("Reino Animal")

#Agregar nodos hijos(ramas) al nodo reino
mamifero = Node("Mamífero", parent=reino)  # Primera clase principal
ave = Node("Ave", parent=reino)  # Segunda clase principal
reptil = Node("Reptil", parent=reino)  # Tercera clase principal

#Agregar subnodos(hojas) a uno de los nodos hijos
carnivoro = Node("Carnívoro", parent=mamifero)  # Primera orden del Mamífero
primates = Node("Primates", parent=mamifero)  # Segunda orden del Mamífero

print_tree(reino)