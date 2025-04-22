##Taller-árboles: programa para la creación de árboles haciendo uso de listas enlazadas.
#Autor: [Ricardo Rincón-2210639]
#Código base
class NodoArbol:
    def __init__(self, valor):
        """
        Crea un nuevo nodo del árbol con el valor especificado.
        Cada nodo inicia con una lista vacía de hijos.
        """
        self.valor = valor
        self.hijos = []

class Arbol:
    def __init__(self, valor_raiz):
        """
        Construye un nuevo árbol a partir de un valor raíz.
        El árbol comienza con un solo nodo (la raíz) que contiene el valor dado.
        """
        self.raiz = NodoArbol(valor_raiz)
    
    def buscar_nodo(self, nodo, valor):
        """
        Busca un nodo que contenga el valor que estamos buscando.
        
        Explora el árbol de forma recursiva comenzando desde el nodo indicado.
        Si encuentra el valor, devuelve el nodo completo.
        Si no lo encuentra después de revisar todo el árbol, devuelve None.
        """
        if nodo.valor == valor:
            return nodo
        for hijo in nodo.hijos:
            encontrado = self.buscar_nodo(hijo, valor)
            if encontrado:
                return encontrado
        return None
    
    def agregar_nodo(self, padre_valor, nuevo_valor):
        """
        Añade un nuevo nodo hijo al árbol bajo un padre específico.

        Primero buscamos el nodo padre según su valor.
        Si encontramos al padre, creamos un nuevo nodo con el valor indicado y lo añadimos como hijo.
        Si no encontramos al padre, mostramos un mensaje de error.
        """
        padre = self.buscar_nodo(self.raiz, padre_valor)
        if padre:
            padre.hijos.append(NodoArbol(nuevo_valor))
        else:
            print(f"Nodo padre '{padre_valor}' no encontrado.")
    
    #Método para contar el peso del árbol
    def peso(self, nodo=None):
        """
        Cuenta cuántos nodos tiene el árbol en total.

        Si no especificamos un nodo, contamos desde la raíz.
        Para cada nodo, contamos 1 (el nodo mismo) más todos sus descendientes.
        """
        if nodo is None:
            nodo = self.raiz
        return 1 + sum(self.peso(hijo) for hijo in nodo.hijos)
    
    #Método para calcular el orden del árbol
    def orden(self, nodo=None):
        """
        Determina cuántos hijos tiene el nodo más "ocupado" del árbol.

        Si no especificamos un nodo, comenzamos desde la raíz.
        Comparamos cuántos hijos tiene cada nodo y nos quedamos con el número más grande.
        """
        if nodo is None:
            nodo = self.raiz
        max_orden = len(nodo.hijos)
        for hijo in nodo.hijos:
            max_orden = max(max_orden, self.orden(hijo))
        return max_orden
    
    #Método para calcular la altura del árbol
    def altura(self, nodo=None):
        """
        Mide qué tan "profundo" es el árbol.
        
        Si no especificamos un nodo, medimos desde la raíz.
        Para un nodo sin hijos, la altura es 1.
        Para un nodo con hijos, la altura es 1 más la mayor altura de sus hijos.
        """
        if nodo is None:
            nodo = self.raiz
        if not nodo.hijos:
            return 1
        return 1 + max(self.altura(hijo) for hijo in nodo.hijos)

def crear_arbol_desde_entrada():
    """
    Crea un árbol según la información que proporcione el usuario.
    
    Primero pedimos el valor para el nodo raíz.
    Luego, vamos pidiendo relaciones "padre-hijo" para construir el árbol.
    Al terminar, mostramos estadísticas del árbol creado: peso, orden y altura.
    """
    valor_raiz = input("Ingrese el valor del nodo raíz: ")
    arbol = Arbol(valor_raiz)
    
    while True:
        entrada = input("Ingrese el nodo padre y el nodo hijo a agregar ('padre hijo'), o fin para terminar: ")
        if entrada.lower() == 'fin':
            break
        try:
            padre, hijo = entrada.split()
            arbol.agregar_nodo(padre, hijo)
        except ValueError:
            print("Formato incorrecto. Use el formato: 'padre hijo'.")
    
    print("\n--- Estadísticas del Árbol ---")
    print(f"Peso del árbol: {arbol.peso()}")
    print(f"Orden del árbol: {arbol.orden()}")
    print(f"Altura del árbol: {arbol.altura()}")

if __name__ == "__main__":
    crear_arbol_desde_entrada()