

"""
EJERCICIO 1: Contar elementos
Dificultad: 🟢 Básico
Tiempo estimado: 10 minutos

Implementa un método count(elem) en SLinkedList que cuente cuántas veces
aparece un elemento en la lista.

Ejemplo:
    lista = [1, 2, 3, 2, 4, 2]
    lista.count(2)  # Retorna: 3
    lista.count(5)  # Retorna: 0     
"""

class Nodo:
    """
    Representa un nodo de una lista simplemente enlazada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    """
    Implementación de una lista simplemente enlazada.
    """
    def __init__(self, valores=None):
        self.head = None

        # Inicialización automática con valores dados
        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        """
        Agrega un nuevo elemento al final de la lista.
        """
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo_nodo

    def count(self, elemento):
        """
        Cuenta cuántas veces aparece un elemento en la lista.
        """
        contador = 0
        actual = self.head

        while actual:
            if actual.dato == elemento:
                contador += 1
            actual = actual.next

        return contador


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

valores_iniciales = [0, 2, 3, 2, 4, 2]
lista = SLinkedList(valores_iniciales)

# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    lista = SLinkedList([0, 2, 3, 2, 4, 2])
    assert lista.count(2) == 3
    assert lista.count(5) == 0

    lista_vacia = SLinkedList()
    assert lista_vacia.count(1) == 0

    lista_uno = SLinkedList([10])
    assert lista_uno.count(10) == 1
    assert lista_uno.count(3) == 0


_pruebas_internas()


print("\n" + "=" * 30)
print("=== EJERCICIO 1 ===")
print("=" * 30)

lista = SLinkedList([0, 2, 3, 2, 4, 2])
print("count(2) esperado 3 ->", lista.count(2))
print("count(5) esperado 0 ->", lista.count(5))

lista_vacia = SLinkedList()
print("Lista vacía count(1) esperado 0 ->", lista_vacia.count(1))

lista_uno = SLinkedList([10])
print("count(10) esperado 1 ->", lista_uno.count(10))
print("count(3) esperado 0 ->", lista_uno.count(3))

"""
EJERCICIO 2: Obtener elemento por índice
Dificultad: 🟢 Básico
Tiempo estimado: 15 minutos

Implementa un método get(index) que retorne el elemento en la posición index.

Ejemplo:
    lista = ['A', 'B', 'C', 'D']
    lista.get(0)   # Retorna: 'A'
    lista.get(2)   # Retorna: 'C'
    lista.get(10)  # Lanza: IndexError
"""

class Nodo:
    """
    Representa un nodo de una lista simplemente enlazada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    """
    Implementación de una lista simplemente enlazada.
    """
    def __init__(self, valores=None):
        self.head = None

        # Inicialización opcional con valores dados
        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        """
        Agrega un nuevo elemento al final de la lista.
        """
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo_nodo

    def get(self, index):
        """
        Retorna el elemento en la posición indicada.
        Lanza IndexError si el índice es inválido.
        """
        if index < 0:
            raise IndexError("Índice fuera de rango")

        actual = self.head
        posicion = 0

        while actual:
            if posicion == index:
                return actual.dato
            actual = actual.next
            posicion += 1

        raise IndexError("Índice fuera de rango")


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 2 ===")
print("=" * 30)

lista = SLinkedList(['A', 'B', 'C', 'D'])

print("Resultado 1 (get 0):", lista.get(0))   # 'A'
print("Resultado 2 (get 2):", lista.get(2))   # 'C'

try:
    lista.get(10)
except IndexError:
    print("Resultado 3 (get 10): IndexError")


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    lista = SLinkedList(['A', 'B', 'C', 'D'])
    assert lista.get(0) == 'A'
    assert lista.get(3) == 'D'

    lista_uno = SLinkedList(['X'])
    assert lista_uno.get(0) == 'X'

    lista_vacia = SLinkedList()
    try:
        lista_vacia.get(0)
        assert False
    except IndexError:
        pass

    try:
        lista.get(-1)
        assert False
    except IndexError:
        pass


_pruebas_internas()


"""
EJERCICIO 3: Encontrar índice de elemento
Dificultad: 🟢 Básico
Tiempo estimado: 15 minutos

Implementa un método index_of(elem) que retorne el índice de la primera
ocurrencia del elemento, o -1 si no existe.

Ejemplo:
    lista = ['A', 'B', 'C', 'B', 'D']
    lista.index_of('B')  # Retorna: 1
    lista.index_of('D')  # Retorna: 4
    lista.index_of('Z')  # Retorna: -1
"""

class Nodo:
    """
    Representa un nodo de una lista simplemente enlazada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    """
    Implementación de una lista simplemente enlazada.
    """
    def __init__(self, valores=None):
        self.head = None

        # Inicialización con valores
        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        """
        Agrega un nuevo elemento al final de la lista.
        """
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo_nodo

    def index_of(self, elem):
        """
        Retorna el índice de la primera aparición del elemento.
        Si no existe, retorna -1.
        """
        actual = self.head
        indice = 0

        # Recorremos la lista hasta encontrar el elemento
        while actual:
            if actual.dato == elem:
                return indice
            actual = actual.next
            indice += 1

        return -1


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 3 ===")
print("=" * 30)

lista = SLinkedList(['A', 'B', 'C', 'B', 'D'])

print("Resultado 1 (index_of 'B'):", lista.index_of('B'))  # 1
print("Resultado 2 (index_of 'D'):", lista.index_of('D'))  # 4
print("Resultado 3 (index_of 'Z'):", lista.index_of('Z'))  # -1


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    # Resultado 1: lista normal
    lista = SLinkedList(['A', 'B', 'C', 'B', 'D'])
    assert lista.index_of('A') == 0
    assert lista.index_of('B') == 1
    assert lista.index_of('D') == 4
    assert lista.index_of('Z') == -1

    # Resultado 2: lista vacía
    lista_vacia = SLinkedList()
    assert lista_vacia.index_of('X') == -1

    # Resultado 3: lista con un solo elemento
    lista_uno = SLinkedList(['Q'])
    assert lista_uno.index_of('Q') == 0
    assert lista_uno.index_of('W') == -1


_pruebas_internas()


"""
EJERCICIO 4: Lista a array
Dificultad: 🟢 Básico
Tiempo estimado: 10 minutos

Implementa un método to_list() que convierta la lista enlazada a una
lista de Python (array).

Ejemplo:
    linked_list = SLinkedList con [1, 2, 3, 4]
    linked_list.to_list()  # Retorna: [1, 2, 3, 4]
"""

class Nodo:
    """
    Representa un nodo de una lista simplemente enlazada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    """
    Implementación de una lista simplemente enlazada.
    """
    def __init__(self, valores=None):
        self.head = None

        # Inicialización con valores
        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        """
        Agrega un nuevo elemento al final de la lista.
        """
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo_nodo

    def to_list(self):
        """
        Convierte la lista enlazada en una lista de Python.
        """
        resultado = []
        actual = self.head

        # Recorremos la lista y agregamos cada dato al array
        while actual:
            resultado.append(actual.dato)
            actual = actual.next

        return resultado


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 4 ===")
print("=" * 30)

linked_list = SLinkedList([1, 2, 3, 4])

print("Resultado 1:", linked_list.to_list())  # [1, 2, 3, 4]


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    # Resultado 1: lista normal
    lista = SLinkedList([1, 2, 3, 4])
    assert lista.to_list() == [1, 2, 3, 4]

    # Resultado 2: lista vacía
    lista_vacia = SLinkedList()
    assert lista_vacia.to_list() == []

    # Resultado 3: lista con un solo elemento
    lista_uno = SLinkedList([10])
    assert lista_uno.to_list() == [10]


_pruebas_internas()


"""
EJERCICIO 5: Limpiar lista
Dificultad: 🟢 Básico
Tiempo estimado: 5 minutos

Implementa un método clear() que elimine todos los elementos de la lista.

Ejemplo:
    lista = [1, 2, 3, 4, 5]
    lista.clear()
    len(lista)  # Retorna: 0
"""

class Nodo:
    """
    Representa un nodo de una lista simplemente enlazada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    """
    Implementación de una lista simplemente enlazada.
    """
    def __init__(self, valores=None):
        self.head = None
        self.size = 0

        # Inicialización con valores
        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        """
        Agrega un nuevo elemento al final de la lista.
        """
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo

        self.size += 1

    def clear(self):
        """
        Elimina todos los elementos de la lista.
        """
        # Al eliminar la referencia al primer nodo,
        # el recolector de basura libera el resto
        self.head = None
        self.size = 0


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 5 ===")
print("=" * 30)

# Resultado 1: lista con varios elementos
lista1 = SLinkedList([1, 2, 3, 4, 5])
lista1.clear()
print("Resultado 1 (lista con elementos): tamaño =", lista1.size)

# Resultado 2: lista con un solo elemento
lista2 = SLinkedList([10])
lista2.clear()
print("Resultado 2 (un elemento): tamaño =", lista2.size)

# Resultado 3: lista vacía
lista3 = SLinkedList()
lista3.clear()
print("Resultado 3 (lista vacía): tamaño =", lista3.size)


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    # Resultado 1: lista con elementos
    lista = SLinkedList([1, 2, 3])
    lista.clear()
    assert lista.size == 0
    assert lista.head is None

    # Resultado 2: lista vacía
    lista_vacia = SLinkedList()
    lista_vacia.clear()
    assert lista_vacia.size == 0
    assert lista_vacia.head is None

    # Resultado 3: lista con un elemento
    lista_uno = SLinkedList([5])
    lista_uno.clear()
    assert lista_uno.size == 0
    assert lista_uno.head is None


_pruebas_internas()


"""
EJERCICIO 6: Invertir lista
Dificultad: 🟡 Intermedio
Tiempo estimado: 25 minutos

Implementa un método reverse() que invierta el orden de los elementos
EN LA MISMA LISTA (no crear una nueva).
"""

class Nodo:
    """
    Representa un nodo de una lista simplemente enlazada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    """
    Implementación de una lista simplemente enlazada.
    """
    def __init__(self, valores=None):
        self.head = None
        self.size = 0

        # Inicialización opcional
        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        """
        Agrega un nuevo elemento al final de la lista.
        """
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo

        self.size += 1

    def reverse(self):
        """
        Invierte la lista enlazada en el mismo objeto.
        Complejidad: O(n)
        """
        anterior = None
        actual = self.head

        # Recorremos la lista cambiando los punteros next
        while actual:
            siguiente = actual.next
            actual.next = anterior
            anterior = actual
            actual = siguiente

        # El nuevo inicio de la lista
        self.head = anterior

    def to_string(self):
        """
        Representación visual de la lista.
        """
        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        return " → ".join(resultado) + " → None"


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 6 ===")
print("=" * 30)

# Resultado 1: lista con varios elementos
lista1 = SLinkedList([1, 2, 3, 4, 5])
lista1.reverse()
print("Resultado 1 (lista normal):", lista1.to_string())

# Resultado 2: lista con un solo elemento
lista2 = SLinkedList([10])
lista2.reverse()
print("Resultado 2 (un elemento):", lista2.to_string())

# Resultado 3: lista vacía
lista3 = SLinkedList()
lista3.reverse()
print("Resultado 3 (lista vacía):", lista3.to_string())


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    # Resultado 1: lista normal
    lista = SLinkedList([1, 2, 3])
    lista.reverse()
    assert lista.to_string() == "3 → 2 → 1 → None"

    # Resultado 2: un solo elemento
    lista_uno = SLinkedList([10])
    lista_uno.reverse()
    assert lista_uno.to_string() == "10 → None"

    # Resultado 3: lista vacía
    lista_vacia = SLinkedList()
    lista_vacia.reverse()
    assert lista_vacia.to_string() == " → None"


_pruebas_internas()


"""
EJERCICIO 7: Detectar ciclo
Dificultad: 🟡 Intermedio
Tiempo estimado: 30 minutos

Implementa un método has_cycle() que detecte si la lista tiene un ciclo
(usando el algoritmo de Floyd: tortuga y liebre).
"""

class Nodo:
    """
    Representa un nodo de una lista simplemente enlazada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    """
    Implementación de una lista simplemente enlazada.
    """
    def __init__(self, valores=None):
        self.head = None

        # Inicialización opcional
        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        """
        Agrega un nuevo elemento al final de la lista.
        """
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo_nodo

    def has_cycle(self):
        """
        Detecta si la lista tiene un ciclo usando
        el algoritmo de Floyd (tortuga y liebre).
        """
        lento = self.head
        rapido = self.head

        # Mientras el puntero rápido pueda avanzar
        while rapido and rapido.next:
            lento = lento.next          # avanza 1
            rapido = rapido.next.next   # avanza 2

            # Si se encuentran, hay ciclo
            if lento == rapido:
                return True

        # Si el rápido llega a None, no hay ciclo
        return False


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 7 ===")
print("=" * 30)

# Resultado 1: lista normal
lista1 = SLinkedList([1, 2, 3, 4])
print("Resultado 1 (lista normal):", lista1.has_cycle())

# Resultado 2: lista con un solo elemento
lista2 = SLinkedList([10])
print("Resultado 2 (un elemento):", lista2.has_cycle())

# Resultado 3: lista con ciclo
lista3 = SLinkedList()
n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)

lista3.head = n1
n1.next = n2
n2.next = n3
n3.next = n2   # ciclo hacia atrás

print("Resultado 3 (lista con ciclo):", lista3.has_cycle())


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    # Resultado 1: lista normal
    lista = SLinkedList([1, 2, 3, 4])
    assert lista.has_cycle() is False

    # Resultado 2: lista con un elemento
    lista_uno = SLinkedList([10])
    assert lista_uno.has_cycle() is False

    # Resultado 3: lista vacía
    lista_vacia = SLinkedList()
    assert lista_vacia.has_cycle() is False

    # Caso 4: lista con ciclo
    n1 = Nodo(1)
    n2 = Nodo(2)
    n3 = Nodo(3)

    lista_ciclo = SLinkedList()
    lista_ciclo.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n1

    assert lista_ciclo.has_cycle() is True


_pruebas_internas()


"""
EJERCICIO 8: Encontrar el medio
Dificultad: 🟡 Intermedio
Tiempo estimado: 20 minutos

Implementa un método get_middle() que retorne el elemento del medio de la lista.
Si hay número par de elementos, retorna el segundo del medio.
"""

class Nodo:
    """
    Representa un nodo de una lista simplemente enlazada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    """
    Implementación de una lista simplemente enlazada.
    """
    def __init__(self, valores=None):
        self.head = None

        # Inicialización opcional
        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        """
        Agrega un nuevo elemento al final de la lista.
        """
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo_nodo

    def get_middle(self):
        """
        Retorna el valor del nodo central.
        En listas pares, retorna el segundo elemento del medio.
        """
        if self.head is None:
            return None

        lento = self.head
        rapido = self.head

        # El rápido avanza de dos en dos y el lento de uno en uno
        while rapido and rapido.next:
            lento = lento.next
            rapido = rapido.next.next

        return lento.dato


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 8 ===")
print("=" * 30)

# Resultado 1: lista con número impar de elementos
lista1 = SLinkedList([1, 2, 3, 4, 5])
print("Resultado 1 (impar):", lista1.get_middle())  # 3

# Resultado 2: lista con número par de elementos
lista2 = SLinkedList([1, 2, 3, 4])
print("Resultado 2 (par):", lista2.get_middle())    # 3

# Resultado 3: lista con un solo elemento
lista3 = SLinkedList([10])
print("Resultado 3 (un elemento):", lista3.get_middle())  # 10


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    assert SLinkedList([1]).get_middle() == 1
    assert SLinkedList([1, 2]).get_middle() == 2
    assert SLinkedList([1, 2, 3]).get_middle() == 2
    assert SLinkedList([1, 2, 3, 4]).get_middle() == 3
    assert SLinkedList().get_middle() is None


_pruebas_internas()

"""
EJERCICIO 9: Eliminar duplicados
Dificultad: 🟡 Intermedio
Tiempo estimado: 25 minutos

Implementa un método remove_duplicates() que elimine todos los elementos
duplicados de la lista, dejando solo la primera ocurrencia.
"""

class Nodo:
    """
    Representa un nodo de una lista simplemente enlazada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    """
    Implementación de una lista simplemente enlazada.
    """
    def __init__(self, valores=None):
        self.head = None

        # Inicialización opcional
        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        """
        Agrega un nuevo elemento al final de la lista.
        """
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo_nodo

    def __str__(self):
        """
        Representación visual de la lista.
        """
        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        return " → ".join(resultado) + " → None"

    def remove_duplicates(self):
        """
        Elimina valores duplicados manteniendo la primera aparición.
        Usa un conjunto auxiliar.
        Complejidad: O(n) tiempo, O(n) espacio.
        """
        vistos = set()
        actual = self.head
        anterior = None

        while actual:
            if actual.dato in vistos:
                anterior.next = actual.next
            else:
                vistos.add(actual.dato)
                anterior = actual

            actual = actual.next


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 9 ===")
print("=" * 30)

lista = SLinkedList([1, 2, 3, 2, 4, 1, 5])

print("Antes:")
print(lista)

lista.remove_duplicates()

print("Después:")
print(lista)


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    lista = SLinkedList([1, 2, 3, 2, 4, 1, 5])
    lista.remove_duplicates()
    assert str(lista) == "1 → 2 → 3 → 4 → 5 → None"

    lista_uno = SLinkedList([1, 1, 1])
    lista_uno.remove_duplicates()
    assert str(lista_uno) == "1 → None"

    lista_vacia = SLinkedList()
    lista_vacia.remove_duplicates()
    assert str(lista_vacia) == " → None"


_pruebas_internas()

"""
EJERCICIO 10: Fusionar dos listas ordenadas
Dificultad: 🟡 Intermedio
Tiempo estimado: 30 minutos

Implementa una función merge_sorted(list1, list2) que tome dos listas
enlazadas ORDENADAS y retorne una nueva lista enlazada también ordenada
con todos los elementos de ambas.
"""


class Nodo:
    """
    Nodo de la lista simplemente enlazada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    """
    Implementación de lista simplemente enlazada.
    """
    def __init__(self, valores=None):
        self.head = None

        # Inicialización opcional
        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        """
        Agrega un elemento al final de la lista.
        """
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo_nodo

    def __str__(self):
        """
        Representación visual de la lista.
        """
        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        return " → ".join(resultado) + " → None"


def merge_sorted(list1, list2):
    """
    Une dos listas enlazadas ORDENADAS en una nueva lista ordenada.
    Usa dos punteros para recorrer ambas listas.
    Complejidad: O(n + m)
    """
    nueva_lista = SLinkedList()

    p1 = list1.head
    p2 = list2.head

    # Comparar elementos mientras ambas listas tengan nodos
    while p1 and p2:
        if p1.dato <= p2.dato:
            nueva_lista.agregar(p1.dato)
            p1 = p1.next
        else:
            nueva_lista.agregar(p2.dato)
            p2 = p2.next

    # Agregar los elementos restantes de list1
    while p1:
        nueva_lista.agregar(p1.dato)
        p1 = p1.next

    # Agregar los elementos restantes de list2
    while p2:
        nueva_lista.agregar(p2.dato)
        p2 = p2.next

    return nueva_lista


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 10 ===")
print("=" * 30)

list1 = SLinkedList([1, 3, 5, 7])
list2 = SLinkedList([2, 4, 6, 8])
print("lista sin fusionar #1:" )
print(list1)
print("lista sin fusionar #2:" )
print(list2)
resultado = merge_sorted(list1, list2)
print("Resultado de la fusión:")
print(resultado)
# 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → None


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    l1 = SLinkedList([1, 3, 5])
    l2 = SLinkedList([2, 4, 6])
    assert str(merge_sorted(l1, l2)) == "1 → 2 → 3 → 4 → 5 → 6 → None"

    l1 = SLinkedList()
    l2 = SLinkedList([1, 2])
    assert str(merge_sorted(l1, l2)) == "1 → 2 → None"

    l1 = SLinkedList([1, 2])
    l2 = SLinkedList()
    assert str(merge_sorted(l1, l2)) == "1 → 2 → None"

    l1 = SLinkedList()
    l2 = SLinkedList()
    assert str(merge_sorted(l1, l2)) == " → None"


_pruebas_internas()


"""
EJERCICIO 11: Palíndromo
Dificultad: 🔴 Avanzado
Tiempo estimado: 35 minutos

Implementa un método is_palindrome() que determine si la lista es un palíndromo
(se lee igual de adelante hacia atrás).

Complejidad: O(n) tiempo, O(1) espacio
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self, valores=None):
        self.head = None

        # Inicialización opcional
        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo_nodo

    def __str__(self):
        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        return " → ".join(resultado) + " → None"

    def is_palindrome(self):
        """
        Verifica si la lista enlazada es un palíndromo.
        """
        if self.head is None or self.head.next is None:
            return True

        # 1. Encontrar el medio (dos punteros)
        lento = self.head
        rapido = self.head

        while rapido and rapido.next:
            lento = lento.next
            rapido = rapido.next.next

        # Si la lista es impar, saltar el nodo central
        if rapido:
            lento = lento.next

        # 2. Invertir la segunda mitad
        prev = None
        actual = lento

        while actual:
            siguiente = actual.next
            actual.next = prev
            prev = actual
            actual = siguiente

        # 3. Comparar ambas mitades
        p1 = self.head
        p2 = prev
        es_palindromo = True

        while p2:
            if p1.dato != p2.dato:
                es_palindromo = False
                break
            p1 = p1.next
            p2 = p2.next

        # 4. Restaurar la segunda mitad (opcional, pero elegante)
        actual = prev
        prev = None

        while actual:
            siguiente = actual.next
            actual.next = prev
            prev = actual
            actual = siguiente

        return es_palindromo


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 11 ===")
print("=" * 30)

lista1 = SLinkedList([1, 2, 3, 2, 1])
print(lista1)
print(lista1.is_palindrome())  # True

lista2 = SLinkedList([1, 2, 3, 4, 5])
print(lista2)
print(lista2.is_palindrome())  # False

lista3 = SLinkedList([9, 8, 7, 8, 9])
print(lista3)
print(lista3.is_palindrome())  # True

lista4 = SLinkedList([9, 8, 7, 6, 5])
print(lista4)
print(lista4.is_palindrome())  # False


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    assert SLinkedList([1, 2, 3, 2, 1]).is_palindrome() is True
    assert SLinkedList([1, 2, 2, 1]).is_palindrome() is True
    assert SLinkedList([1, 2, 3]).is_palindrome() is False
    assert SLinkedList([1]).is_palindrome() is True
    assert SLinkedList().is_palindrome() is True


_pruebas_internas() 


"""
EJERCICIO 12: Rotar lista
Dificultad: 🔴 Avanzado
Tiempo estimado: 30 minutos
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self, valores=None):
        self.head = None
        self.size = 0

        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo

        self.size += 1

    def __str__(self):
        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        return " → ".join(resultado) + " → None"

    def rotate(self, k):
        """
        Rota la lista a la derecha k posiciones.
        Complejidad: O(n)
        """
        if self.head is None or self.size <= 1:
            return

        # Ajustar k si es mayor que el tamaño
        k = k % self.size
        if k == 0:
            return

        # 1️⃣ Encontrar el último nodo
        tail = self.head
        while tail.next:
            tail = tail.next

        # 2️⃣ Hacer la lista circular
        tail.next = self.head

        # 3️⃣ Encontrar el nuevo tail
        pasos = self.size - k
        nuevo_tail = self.head
        for _ in range(pasos - 1):
            nuevo_tail = nuevo_tail.next

        # 4️⃣ Romper el ciclo
        self.head = nuevo_tail.next
        nuevo_tail.next = None


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 12 ===")
print("=" * 30)

# Resultado 1
lista1 = SLinkedList([1, 2, 3, 4, 5])
print("Resultado 1 - Antes:", lista1)
lista1.rotate(2)
print("Resultado 1 - Después:", lista1)

print("-" * 30)

# Resultado 2
lista2 = SLinkedList([1, 2, 3])
print("Resultado 2 - Antes:", lista2)
lista2.rotate(4)
print("Resultado 2 - Después:", lista2)

print("-" * 30)

# Resultado 3
lista3 = SLinkedList([10])
print("Resultado 3 - Antes:", lista3)
lista3.rotate(10)
print("Resultado 3 - Después:", lista3)


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    lista = SLinkedList([1, 2, 3, 4, 5])
    lista.rotate(2)
    assert str(lista) == "4 → 5 → 1 → 2 → 3 → None"

    lista = SLinkedList([1, 2, 3])
    lista.rotate(3)
    assert str(lista) == "1 → 2 → 3 → None"

    lista = SLinkedList([1, 2, 3])
    lista.rotate(4)
    assert str(lista) == "3 → 1 → 2 → None"

    lista = SLinkedList([1])
    lista.rotate(10)
    assert str(lista) == "1 → None"

    lista = SLinkedList()
    lista.rotate(5)
    assert str(lista) == " → None"


_pruebas_internas()


"""
EJERCICIO 13: Particionar lista
Dificultad: 🔴 Avanzado
Tiempo estimado: 35 minutos
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self, valores=None):
        self.head = None

        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
            return

        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = nuevo_nodo

    def __str__(self):
        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        return " → ".join(resultado) + " → None"

    def partition(self, x):
        """
        Reordena la lista colocando primero los elementos < x
        y luego los elementos >= x.
        Complejidad: O(n)
        """
        menores_head = menores_tail = None
        mayores_head = mayores_tail = None

        actual = self.head

        while actual:
            siguiente = actual.next
            actual.next = None  # Desconectar el nodo actual

            if actual.dato < x:
                if menores_head is None:
                    menores_head = menores_tail = actual
                else:
                    menores_tail.next = actual
                    menores_tail = actual
            else:
                if mayores_head is None:
                    mayores_head = mayores_tail = actual
                else:
                    mayores_tail.next = actual
                    mayores_tail = actual

            actual = siguiente

        # Unir las dos listas
        if menores_tail:
            menores_tail.next = mayores_head
            self.head = menores_head
        else:
            self.head = mayores_head


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 13 ===")
print("=" * 30)

# Resultado 1
lista1 = SLinkedList([3, 5, 8, 5, 10, 2, 1])
print("Resultado 1 - Antes:", lista1)
lista1.partition(5)
print("Resultado 1 - Después:", lista1)

print("-" * 30)

# Resultado 2
lista2 = SLinkedList([1, 2, 3])
print("Resultado 2 - Antes:", lista2)
lista2.partition(5)
print("Resultado 2 - Después:", lista2)

print("-" * 30)

# Resultado 3
lista3 = SLinkedList([5, 6, 7])
print("Resultado 3 - Antes:", lista3)
lista3.partition(5)
print("Resultado 3 - Después:", lista3)


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    lista = SLinkedList([3, 5, 8, 5, 10, 2, 1])
    lista.partition(5)
    assert str(lista) == "3 → 2 → 1 → 5 → 8 → 5 → 10 → None"

    lista = SLinkedList([1, 2, 3])
    lista.partition(5)
    assert str(lista) == "1 → 2 → 3 → None"

    lista = SLinkedList([5, 6, 7])
    lista.partition(5)
    assert str(lista) == "5 → 6 → 7 → None"

    lista = SLinkedList()
    lista.partition(3)
    assert str(lista) == " → None"


_pruebas_internas()


"""
EJERCICIO 14: Suma de dos listas (números)
Dificultad: 🔴 Avanzado
Tiempo estimado: 40 minutos
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self, valores=None):
        self.head = None

        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.head is None:
            self.head = nuevo_nodo
            return

        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = nuevo_nodo

    def __str__(self):
        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        return " → ".join(resultado) + " → None"


def add_numbers(list1, list2):
    resultado = SLinkedList()

    p1 = list1.head
    p2 = list2.head
    carry = 0

    while p1 or p2 or carry:
        suma = carry

        if p1:
            suma += p1.dato
            p1 = p1.next

        if p2:
            suma += p2.dato
            p2 = p2.next

        carry = suma // 10
        resultado.agregar(suma % 10)

    return resultado


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 14 ===")
print("=" * 30)

print("Resultado 1")
lista1 = SLinkedList([2, 4, 3])
lista2 = SLinkedList([5, 6, 4])
print(add_numbers(lista1, lista2))
print("==========")

print("Resultado 2")
lista1 = SLinkedList([0])
lista2 = SLinkedList([0])
print(add_numbers(lista1, lista2))
print("==========")

print("Resultado 3")
lista1 = SLinkedList([9, 9, 9])
lista2 = SLinkedList([1])
print(add_numbers(lista1, lista2))
print("==========")

print("Resultado 4")
ista1 = SLinkedList([1])
lista2 = SLinkedList([9, 9])
print(add_numbers(lista1, lista2))


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    l1 = SLinkedList([2, 4, 3])
    l2 = SLinkedList([5, 6, 4])
    assert str(add_numbers(l1, l2)) == "7 → 0 → 8 → None"

    l1 = SLinkedList([0])
    l2 = SLinkedList([0])
    assert str(add_numbers(l1, l2)) == "0 → None"

    l1 = SLinkedList([9, 9, 9])
    l2 = SLinkedList([1])
    assert str(add_numbers(l1, l2)) == "0 → 0 → 0 → 1 → None"

    l1 = SLinkedList([1])
    l2 = SLinkedList([9, 9])
    assert str(add_numbers(l1, l2)) == "0 → 0 → 1 → None"


_pruebas_internas()


"""
EJERCICIO 15: Intersección de dos listas
Dificultad: 🔴 Avanzado
Tiempo estimado: 45 minutos
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self, valores=None):
        self.head = None

        if valores:
            for valor in valores:
                self.agregar(valor)

    def agregar(self, dato):
        nuevo = Nodo(dato)

        if self.head is None:
            self.head = nuevo
            return

        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = nuevo


def longitud(lista):
    actual = lista.head
    contador = 0

    while actual:
        contador += 1
        actual = actual.next

    return contador


def get_intersection_node(list1, list2):
    if not list1.head or not list2.head:
        return None

    len1 = longitud(list1)
    len2 = longitud(list2)

    p1 = list1.head
    p2 = list2.head

    if len1 > len2:
        for _ in range(len1 - len2):
            p1 = p1.next
    else:
        for _ in range(len2 - len1):
            p2 = p2.next

    while p1 and p2:
        if p1 is p2:
            return p1
        p1 = p1.next
        p2 = p2.next

    return None


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 15 ===")
print("=" * 30)

print("CASO 1: Intersección en el nodo 7")

n7 = Nodo(7)
n8 = Nodo(8)
n9 = Nodo(9)

n7.next = n8
n8.next = n9

list1 = SLinkedList([1, 2, 3])
actual = list1.head
while actual.next:
    actual = actual.next
actual.next = n7

list2 = SLinkedList([4, 5, 6])
actual = list2.head
while actual.next:
    actual = actual.next
actual.next = n7

nodo = get_intersection_node(list1, list2)
print("Resultado:", nodo.dato if nodo else None)

print("CASO 2: Intersección al inicio")

n1 = Nodo(100)
n2 = Nodo(200)
n1.next = n2

list1 = SLinkedList()
list2 = SLinkedList()

list1.head = n1
list2.head = n1

nodo = get_intersection_node(list1, list2)
print("Resultado:", nodo.dato if nodo else None)

print("CASO 3: Sin intersección")

list1 = SLinkedList([1, 2, 3])
list2 = SLinkedList([4, 5, 6])

nodo = get_intersection_node(list1, list2)
print("Resultado:", nodo.dato if nodo else None)

print("CASO 4: Una lista vacía")

list1 = SLinkedList()
list2 = SLinkedList([1, 2, 3])

nodo = get_intersection_node(list1, list2)
print("Resultado:", nodo.dato if nodo else None)


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    n1 = Nodo(10)
    n2 = Nodo(20)
    n1.next = n2

    l1 = SLinkedList([1, 2])
    l2 = SLinkedList([3])

    l1.head.next.next = n1
    l2.head.next = n1

    assert get_intersection_node(l1, l2) is n1

    l1 = SLinkedList([1, 2, 3])
    l2 = SLinkedList([4, 5, 6])
    assert get_intersection_node(l1, l2) is None

    l1 = SLinkedList()
    l2 = SLinkedList([1])
    assert get_intersection_node(l1, l2) is None


_pruebas_internas()


"""
EJERCICIO 16: Navegador Web
Dificultad: 🟡 Intermedio
Tiempo estimado: 40 minutos
"""

class Nodo:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    """
    Historial de navegador usando lista doblemente enlazada.
    """

    def __init__(self, homepage):
        self.current = Nodo(homepage)

    def visit(self, url):
        nuevo = Nodo(url)

        # eliminar historial futuro
        self.current.next = None

        # enlazar nuevo nodo
        nuevo.prev = self.current
        self.current.next = nuevo

        # mover actual
        self.current = nuevo

    def atras(self, steps):
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def adelante(self, steps):
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url

    def get_current(self):
        return self.current.url


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 16 ===")
print("=" * 30)

browser = BrowserHistory("google.com")
print("Inicio:", browser.get_current())

browser.visit("youtube.com")
print("Visita:", browser.get_current())

browser.visit("facebook.com")
print("Visita:", browser.get_current())

browser.atras(1)
print("atras 1:", browser.get_current())

browser.adelante(1)
print("Adelante 1:", browser.get_current())


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    browser = BrowserHistory("inicio.com")
    assert browser.get_current() == "inicio.com"

    browser.visit("a.com")
    browser.visit("b.com")
    browser.visit("c.com")

    assert browser.atras(1) == "b.com"
    assert browser.atras(1) == "a.com"
    assert browser.atras(5) == "inicio.com"

    assert browser.adelante(2) == "b.com"

    browser.visit("x.com")
    assert browser.adelante(2) == "x.com"  # historial futuro eliminado
    

_pruebas_internas()


"""
EJERCICIO 17: LRU Cache
Dificultad: 🔴 Avanzado
Tiempo estimado: 60 minutos

Implementa una estructura de datos LRU Cache (Least Recently Used Cache)
usando una lista doblemente enlazada + diccionario.
"""

# =========================
# IMPLEMENTACIÓN
# =========================

class Nodo:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    Implementación de una caché LRU (Least Recently Used).
    Usa:
    - Diccionario para acceso O(1)
    - Lista doblemente enlazada para mantener el orden de uso
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> Nodo

        # Nodos ficticios (dummy) para simplificar la lógica
        self.head = Nodo(0, 0)  # LRU
        self.tail = Nodo(0, 0)  # MRU
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, nodo):
        """
        Elimina un nodo de la lista doblemente enlazada.
        Complejidad: O(1)
        """
        nodo.prev.next = nodo.next
        nodo.next.prev = nodo.prev

    def _add_to_end(self, nodo):
        """
        Agrega un nodo justo antes del tail (más recientemente usado).
        Complejidad: O(1)
        """
        last = self.tail.prev
        last.next = nodo
        nodo.prev = last
        nodo.next = self.tail
        self.tail.prev = nodo

    def get(self, key):
        """
        Retorna el valor asociado a la clave.
        Si no existe, retorna -1.
        Complejidad: O(1)
        """
        if key not in self.cache:
            return -1

        nodo = self.cache[key]
        # Mover a más recientemente usado
        self._remove(nodo)
        self._add_to_end(nodo)
        return nodo.value

    def put(self, key, value):
        """
        Inserta o actualiza un valor en la caché.
        Si se excede la capacidad, elimina el LRU.
        Complejidad: O(1)
        """
        if key in self.cache:
            nodo = self.cache[key]
            nodo.value = value
            self._remove(nodo)
            self._add_to_end(nodo)
        else:
            if len(self.cache) == self.capacity:
                # Eliminar el menos recientemente usado
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]

            nuevo = Nodo(key, value)
            self.cache[key] = nuevo
            self._add_to_end(nuevo)


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 17 ===")
print("=" * 30)

cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)
print("get(1):", cache.get(1))  # 10

cache.put(3, 30)  # elimina key 2 (LRU)

print("get(2):", cache.get(2))  # -1
print("get(3):", cache.get(3))  # 30
print("get(1):", cache.get(1))  # 10


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

    cache.put(3, 3)  # elimina 2
    assert cache.get(2) == -1

    cache.put(4, 4)  # elimina 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    cache = LRUCache(1)
    cache.put(1, 10)
    cache.put(2, 20)
    assert cache.get(1) == -1
    assert cache.get(2) == 20


_pruebas_internas()


"""
EJERCICIO 18: Editor Multi-cursor
Dificultad: 🔴 Avanzado
Tiempo estimado: 50 minutos

Extiende el TextEditor para soportar múltiples cursores (como en VS Code).
Cada cursor puede estar en una posición diferente del documento.
"""

# =========================
# IMPLEMENTACIÓN
# =========================

class Action:
    def __init__(self, cursor_id, position, text):
        self.cursor_id = cursor_id
        self.position = position
        self.text = text


class MultiCursorEditor:
    """
    Editor de texto con múltiples cursores.
    Soporta inserción de texto, undo y redo global.
    """

    def __init__(self):
        self.document = ""
        self.cursors = {}          # cursor_id -> position
        self.next_cursor_id = 1
        self.undo_stack = []
        self.redo_stack = []

    def add_cursor(self, position):
        """
        Agrega un cursor en una posición dada.
        Complejidad: O(1)
        """
        cursor_id = self.next_cursor_id
        self.next_cursor_id += 1
        self.cursors[cursor_id] = position
        return cursor_id

    def remove_cursor(self, cursor_id):
        """
        Elimina un cursor existente.
        Complejidad: O(1)
        """
        if cursor_id in self.cursors:
            del self.cursors[cursor_id]

    def type_at_cursor(self, cursor_id, text):
        """
        Inserta texto en la posición del cursor indicado.
        Guarda la acción para undo/redo.
        Complejidad: O(n + c)
        """
        if cursor_id not in self.cursors:
            return

        pos = self.cursors[cursor_id]

        # Insertar texto en el documento
        self.document = self.document[:pos] + text + self.document[pos:]

        # Actualizar posiciones de todos los cursores
        for cid in self.cursors:
            if self.cursors[cid] > pos:
                self.cursors[cid] += len(text)

        # Mover el cursor actual
        self.cursors[cursor_id] += len(text)

        # Registrar acción
        self.undo_stack.append(Action(cursor_id, pos, text))
        self.redo_stack.clear()

    def undo_all(self):
        """
        Revierte la última acción realizada.
        Complejidad: O(n + c)
        """
        if not self.undo_stack:
            return

        action = self.undo_stack.pop()
        pos = action.position
        length = len(action.text)

        # Eliminar texto
        self.document = self.document[:pos] + self.document[pos + length:]

        # Ajustar cursores
        for cid in self.cursors:
            if self.cursors[cid] > pos:
                self.cursors[cid] -= length

        self.redo_stack.append(action)

    def redo_all(self):
        """
        Reaplica la última acción deshecha.
        Complejidad: O(n + c)
        """
        if not self.redo_stack:
            return

        action = self.redo_stack.pop()
        pos = action.position
        text = action.text

        # Reinsertar texto
        self.document = self.document[:pos] + text + self.document[pos:]

        # Ajustar cursores
        for cid in self.cursors:
            if self.cursors[cid] > pos:
                self.cursors[cid] += len(text)

        self.undo_stack.append(action)


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 18 ===")
print("=" * 30)

editor = MultiCursorEditor()

c1 = editor.add_cursor(0)
c2 = editor.add_cursor(0)

editor.type_at_cursor(c1, "Hola")
editor.type_at_cursor(c2, "Hey ")

print("Documento:", editor.document)  # Hey Hola

editor.undo_all()
print("Undo:", editor.document)        # Hola

editor.redo_all()
print("Redo:", editor.document)        # Hey Hola


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():

    editor = MultiCursorEditor()
    c1 = editor.add_cursor(0)
    c2 = editor.add_cursor(0)

    editor.type_at_cursor(c1, "A")
    editor.type_at_cursor(c2, "B ")
    assert editor.document == "B A"

    editor.undo_all()
    assert editor.document == "A"
    editor.redo_all()
    assert editor.document == "B A"

    editor.undo_all()
    editor.undo_all()
    assert editor.document == ""

    editor.redo_all()
    editor.redo_all()
    assert editor.document == "B A"

_pruebas_internas()

"""
EJERCICIO 19: Benchmark de operaciones
Dificultad: 🟡 Intermedio
Tiempo estimado: 30 minutos

Compara el rendimiento de:
- Arrays (listas de Python)
- Listas simplemente enlazadas
- Listas doblemente enlazadas

Para distintos tamaños de operaciones:
100, 500, 1000 y 2000
"""

import time
import random


# =========================
# ESTRUCTURAS DE DATOS
# =========================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class ListaSimpleEnlazada:
    """Lista simplemente enlazada."""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node

    def insert_end(self, value):
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove_start(self):
        if self.head:
            self.head = self.head.next
            if not self.head:
                self.tail = None

    def remove_end(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return

        current = self.head
        while current.next != self.tail:
            current = current.next
        current.next = None
        self.tail = current

    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data


class ListaDobleEnlazada:
    """Lista doblemente enlazada."""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def insert_end(self, value):
        node = Node(value)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        else:
            self.head = node
        self.tail = node

    def remove_start(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

    def remove_end(self):
        if not self.tail:
            return
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data


# =========================
# BENCHMARK
# =========================

def benchmark_for_size(N):
    indices = [random.randint(0, N - 1) for _ in range(N)]
    results = {}

    # ===== ARRAY =====
    arr = []
    start = time.time()
    for i in range(N):
        arr.insert(0, i)
    results["Array insert start"] = time.time() - start

    arr = []
    start = time.time()
    for i in range(N):
        arr.append(i)
    results["Array insert end"] = time.time() - start

    start = time.time()
    for _ in range(N):
        arr.pop(0)
    results["Array remove start"] = time.time() - start

    arr = list(range(N))
    start = time.time()
    for _ in range(N):
        arr.pop()
    results["Array remove end"] = time.time() - start

    arr = list(range(N))
    start = time.time()
    for i in indices:
        _ = arr[i]
    results["Array access"] = time.time() - start

    # ===== Lista Simple Enlazada =====
    LSE = ListaSimpleEnlazada()
    start = time.time()
    for i in range(N):
        LSE.insert_start(i)
    results["LSE insert start"] = time.time() - start

    LSE = ListaSimpleEnlazada()
    start = time.time()
    for i in range(N):
        LSE.insert_end(i)
    results["LSE insert end"] = time.time() - start

    start = time.time()
    for _ in range(N):
        LSE.remove_start()
    results["LSE remove start"] = time.time() - start

    LSE = ListaSimpleEnlazada()
    for i in range(N):
        LSE.insert_end(i)
    start = time.time()
    for _ in range(N):
        LSE.remove_end()
    results["LSE remove end"] = time.time() - start

    LSE = ListaSimpleEnlazada()
    for i in range(N):
        LSE.insert_end(i)
    start = time.time()
    for i in indices:
        _ = LSE.get(i)
    results["LSE access"] = time.time() - start

    # ===== Lista Doble Enlazada =====
    LDE = ListaDobleEnlazada()
    start = time.time()
    for i in range(N):
        LDE.insert_start(i)
    results["LDE insert start"] = time.time() - start

    LDE = ListaDobleEnlazada()
    start = time.time()
    for i in range(N):
        LDE.insert_end(i)
    results["LDE insert end"] = time.time() - start

    start = time.time()
    for _ in range(N):
        LDE.remove_start()
    results["LDE remove start"] = time.time() - start

    LDE = ListaDobleEnlazada()
    for i in range(N):
        LDE.insert_end(i)
    start = time.time()
    for _ in range(N):
        LDE.remove_end()
    results["LDE remove end"] = time.time() - start

    LDE = ListaDobleEnlazada()
    for i in range(N):
        LDE.insert_end(i)
    start = time.time()
    for i in indices:
        _ = LDE.get(i)
    results["LDE access"] = time.time() - start

    # ===== PRINT =====
    print(f"\n--- BENCHMARK ({N} operaciones) ---")
    for k, v in results.items():
        print(f"{k:25} {v:.6f} s")


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

print("\n" + "=" * 30)
print("=== EJERCICIO 19 ===")
print("=" * 30)

for size in [100, 500, 1000, 2000]:
    benchmark_for_size(size)


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():

    LSE = ListaSimpleEnlazada()
    LSE.insert_end(1)
    LSE.insert_end(2)
    LSE.insert_end(3)
    assert LSE.get(1) == 2
    LSE.remove_start()
    assert LSE.get(0) == 2

    LDE = ListaDobleEnlazada()
    LDE.insert_start(1)
    LDE.insert_end(2)
    LDE.insert_end(3)
    LDE.remove_end()
    assert LDE.get(1) == 2


_pruebas_internas()



"""
EJERCICIO 20: Análisis de casos de uso

Para cada uno de los siguientes escenarios, determina qué estructura
es más apropiada (Array, Lista Simple, Lista Doble) y justifica tu respuesta:

1. Sistema de colas de impresión (FIFO estricto)
2. Historial de navegación de un navegador
3. Sistema de undo/redo con límite de 100 acciones
4. Base de datos que necesita acceso rápido por ID
5. Playlist de música con navegación adelante/atrás
6. Sistema de gestión de memoria del OS
7. Editor de texto que solo permite append al final
8. Implementación de una pila (Stack)
9. Juego que necesita insertar/eliminar enemigos frecuentemente
10. Sistema de logs que solo escribe al final y lee todo

Escribe tus respuestas en comentarios con justificación.
"""

def analisis_casos_uso():
    """
    Análisis de casos de uso para diferentes estructuras de datos
    """
    casos = [
        """1. Sistema de colas de impresión (FIFO estricto)
Estructura apropiada: Lista Simple
Justificación:
Se insertan elementos al final y se eliminan al inicio.
Ambas operaciones pueden hacerse en O(1) usando head y tail.
Un Array sería ineficiente al eliminar al inicio (O(n)).""",
        
        """2. Historial de navegación de un navegador
Estructura apropiada: Lista Doble
Justificación:
Se necesita navegar hacia atrás y hacia adelante.
La lista doble permite moverse en ambas direcciones en O(1).
Es el modelo clásico usado en navegadores.""",
        
        """3. Sistema de undo/redo con límite de 100 acciones
Estructura apropiada: Array
Justificación:
El tamaño es pequeño y fijo.
Acceso rápido al último elemento.
Push y pop en O(1) usando el final del array.
Más simple que usar listas enlazadas.""",
        
        """4. Base de datos que necesita acceso rápido por ID
Estructura apropiada: Array
Justificación:
Acceso directo por índice en O(1).
Ideal cuando el ID puede mapearse a una posición.
Las listas enlazadas tienen acceso O(n), por lo que no son adecuadas.""",
        
        """5. Playlist de música con navegación adelante/atrás
Estructura apropiada: Lista Doble
Justificación:
Se requiere moverse al siguiente y al anterior.
Inserciones y eliminaciones dinámicas.
Navegación bidireccional eficiente en O(1).""",
        
        """6. Sistema de gestión de memoria del OS
Estructura apropiada: Lista Doble
Justificación:
Permite dividir y unir bloques de memoria.
Eliminaciones e inserciones frecuentes.
Navegación hacia adelante y atrás entre bloques.""",
        
        """7. Editor de texto que solo permite append al final
Estructura apropiada: Array
Justificación:
Solo se insertan elementos al final.
Append es O(1) amortizado.
Mejor rendimiento de memoria y caché que listas enlazadas.""",
        
        """8. Implementación de una pila (Stack)
Estructura apropiada: Array
Justificación:
Operaciones push y pop al final en O(1).
Implementación sencilla.
No se necesita inserción/eliminación en medio.""",
        
        """9. Juego que necesita insertar/eliminar enemigos frecuentemente
Estructura apropiada: Lista Simple
Justificación:
Inserciones y eliminaciones frecuentes.
No importa el acceso por índice.
Evita el costo O(n) de desplazar elementos como en arrays.""",
        
        """10. Sistema de logs que solo escribe al final y lee todo
Estructura apropiada: Array
Justificación:
Escritura secuencial al final.
Lectura completa eficiente.
Mejor uso de memoria y rendimiento que listas enlazadas."""
    ]
    
    print("\n" + "="*80)
    print("ANÁLISIS DE CASOS DE USO Ejercicio #20")
    print("="*80)
    
    for caso in casos:
        print("\n" + caso)
        print("\n" + "="*50)

analisis_casos_uso()
