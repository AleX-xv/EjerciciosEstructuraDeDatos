# EJERCICIOS PRÁCTICOS - LISTAS ENLAZADAS
# Unidad 3: Estructura de Datos
# ULEAM - Ingeniería en Software

# ============================================================================
# 🟢 EJERCICIOS BÁSICOS - LISTA SIMPLEMENTE ENLAZADA
# ============================================================================

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

print(lista.count(2))  # Resultado: 3
print(lista.count(5))  # Resultado: 0


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
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self, valores=None):
        self.head = None

        # Inicialización opcional con valores dados
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

lista = SLinkedList(['A', 'B', 'C', 'D'])

print(lista.get(0))   # 'A'
print(lista.get(2))   # 'C'
print(lista.get(10))  # IndexError


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
    lista.index_of('B')  # Retorna: 1 (primera ocurrencia)
    lista.index_of('D')  # Retorna: 4
    lista.index_of('Z')  # Retorna: -1
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self, valores=None):
        self.head = None

        # Inicialización con valores
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

    def index_of(self, elem):
        """
        Retorna el índice de la primera aparición del elemento.
        Si no existe, retorna -1.
        """
        actual = self.head
        indice = 0

        while actual:
            if actual.dato == elem:
                return indice
            actual = actual.next
            indice += 1

        return -1


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

lista = SLinkedList(['A', 'B', 'C', 'B', 'D'])

print(lista.index_of('B'))  # 1
print(lista.index_of('D'))  # 4
print(lista.index_of('Z'))  # -1


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    lista = SLinkedList(['A', 'B', 'C', 'B', 'D'])
    assert lista.index_of('A') == 0
    assert lista.index_of('B') == 1
    assert lista.index_of('D') == 4
    assert lista.index_of('Z') == -1

    lista_vacia = SLinkedList()
    assert lista_vacia.index_of('X') == -1

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
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self, valores=None):
        self.head = None

        # Inicialización con valores
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

    def to_list(self):
        """
        Convierte la lista enlazada en una lista de Python.
        """
        resultado = []
        actual = self.head

        while actual:
            resultado.append(actual.dato)
            actual = actual.next

        return resultado


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

linked_list = SLinkedList([1, 2, 3, 4])
print(linked_list.to_list())  # [1, 2, 3, 4]


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    lista = SLinkedList([1, 2, 3, 4])
    assert lista.to_list() == [1, 2, 3, 4]

    lista_vacia = SLinkedList()
    assert lista_vacia.to_list() == []

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
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self, valores=None):
        self.head = None
        self.size = 0

        # Inicialización opcional con valores
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

    def clear(self):
        """
        Elimina todos los elementos de la lista.
        """
        self.head = None
        self.size = 0


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

lista = SLinkedList([1, 2, 3, 4, 5])
lista.clear()

print(lista.size)  # 0


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    lista = SLinkedList([1, 2, 3])
    lista.clear()
    assert lista.size == 0
    assert lista.head is None

    lista_vacia = SLinkedList()
    lista_vacia.clear()
    assert lista_vacia.size == 0
    assert lista_vacia.head is None


_pruebas_internas()



"""
EJERCICIO 6: Invertir lista
Dificultad: 🟡 Intermedio
Tiempo estimado: 25 minutos

Implementa un método reverse() que invierta el orden de los elementos
EN LA MISMA LISTA (no crear una nueva).

Ejemplo:
    lista = [1, 2, 3, 4, 5]
    lista.reverse()
    print(lista)  # Output: 5 → 4 → 3 → 2 → 1 → None

Pista: Necesitas cambiar los punteros next de cada nodo.
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self, valores=None):
        self.head = None
        self.size = 0

        # Inicialización opcional
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

    def reverse(self):
        """
        Invierte la lista enlazada en el mismo objeto.
        Complejidad: O(n)
        """
        anterior = None
        actual = self.head

        while actual:
            siguiente = actual.next
            actual.next = anterior
            anterior = actual
            actual = siguiente

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

lista = SLinkedList([1, 2, 3, 4, 5])
lista.reverse()

print(lista.to_string())  
# 5 → 4 → 3 → 2 → 1 → None


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    lista = SLinkedList([1, 2, 3])
    lista.reverse()
    assert lista.to_string() == "3 → 2 → 1 → None"

    lista_uno = SLinkedList([10])
    lista_uno.reverse()
    assert lista_uno.to_string() == "10 → None"

    lista_vacia = SLinkedList()
    lista_vacia.reverse()
    assert lista_vacia.to_string() == " → None"


_pruebas_internas()



"""
EJERCICIO 7: Detectar ciclo
Dificultad: 🟡 Intermedio
Tiempo estimado: 30 minutos

Implementa un método has_cycle() que detecte si la lista tiene un ciclo
(un nodo apunta a un nodo anterior, creando un bucle infinito).

Usa el algoritmo de Floyd (tortuga y liebre):
- Dos punteros: uno avanza 1 paso, otro avanza 2 pasos
- Si se encuentran, hay ciclo
- Si el rápido llega a None, no hay ciclo

Ejemplo:
    lista normal: 1 → 2 → 3 → None (retorna False)
    lista con ciclo: 1 → 2 → 3 → (vuelve a 2) (retorna True)
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

    def has_cycle(self):
        """
        Detecta si la lista tiene un ciclo usando
        el algoritmo de Floyd (tortuga y liebre).
        """
        lento = self.head
        rapido = self.head

        while rapido and rapido.next:
            lento = lento.next
            rapido = rapido.next.next

            if lento == rapido:
                return True

        return False


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

# Lista normal
lista1 = SLinkedList([1, 2, 3])
print(lista1.has_cycle())  # False


# Lista con ciclo
lista2 = SLinkedList()
n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)

lista2.head = n1
n1.next = n2
n2.next = n3
n3.next = n2   # ciclo

print(lista2.has_cycle())  # True


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    lista = SLinkedList([1, 2, 3, 4])
    assert lista.has_cycle() is False

    lista_uno = SLinkedList([10])
    assert lista_uno.has_cycle() is False

    lista_vacia = SLinkedList()
    assert lista_vacia.has_cycle() is False

    # Crear ciclo manual
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































