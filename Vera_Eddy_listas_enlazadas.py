
Eddy Alexander Vera Bailon
fecha: 18/12/2025
Ejercicios: Todos


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

        # Inicialización con valores
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





"""
EJERCICIO 8: Encontrar el medio
Dificultad: 🟡 Intermedio
Tiempo estimado: 20 minutos

Implementa un método get_middle() que retorne el elemento del medio de la lista.
Si hay número par de elementos, retorna el segundo del medio.

Usa el algoritmo de dos punteros:
- Un puntero lento (avanza 1 paso)
- Un puntero rápido (avanza 2 pasos)
- Cuando el rápido llega al final, el lento está en el medio

Ejemplo:
    [1, 2, 3, 4, 5] → retorna 3
    [1, 2, 3, 4] → retorna 3 (segundo del medio)
"""




class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self, valores=None):
        self.head = None

        # Inicialización 
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

    def get_middle(self):
        """
        Retorna el valor del nodo central.
        En listas pares, retorna el segundo elemento del medio.
        """
        if self.head is None:
            return None

        lento = self.head
        rapido = self.head

        while rapido and rapido.next:
            lento = lento.next
            rapido = rapido.next.next

        return lento.dato


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

# Lista con número impar de elementos
lista1 = SLinkedList([1, 2, 3, 4, 5])
print(lista1.get_middle())  # 3

# Lista con número par de elementos
lista2 = SLinkedList([1, 2, 3, 4])
print(lista2.get_middle())  # 3


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
duplicados de la lista, dejando solo la primera ocurrencia de cada elemento.

Ejemplo:
    [1, 2, 3, 2, 4, 1, 5] → [1, 2, 3, 4, 5]

Versión 1: Puedes usar un conjunto (set) auxiliar - O(n) tiempo, O(n) espacio
Versión 2: Sin espacio adicional (más difícil) - O(n²) tiempo, O(1) espacio
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self, valores=None):
        self.head = None

        # Inicialización 
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

    def remove_duplicates(self):
        """
        Elimina valores duplicados manteniendo la primera aparición.
        Complejidad: O(n)
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

Ejemplo:
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    merge_sorted(list1, list2) → [1, 2, 3, 4, 5, 6, 7, 8]

Pista: Usa dos punteros, uno para cada lista, y compara elementos.
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self, valores=None):
        self.head = None

        # Inicialización 
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


def merge_sorted(list1, list2):
    """
    Une dos listas enlazadas ordenadas en una nueva lista ordenada.
    """
    nueva_lista = SLinkedList()

    p1 = list1.head
    p2 = list2.head

    while p1 and p2:
        if p1.dato <= p2.dato:
            nueva_lista.agregar(p1.dato)
            p1 = p1.next
        else:
            nueva_lista.agregar(p2.dato)
            p2 = p2.next

    # Agregar los elementos restantes
    while p1:
        nueva_lista.agregar(p1.dato)
        p1 = p1.next

    while p2:
        nueva_lista.agregar(p2.dato)
        p2 = p2.next

    return nueva_lista


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

list1 = SLinkedList([1, 3, 5, 7])
list2 = SLinkedList([2, 4, 6, 8])

resultado = merge_sorted(list1, list2)
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

Ejemplo:
    [1, 2, 3, 2, 1] → True
    [1, 2, 3, 4, 5] → False

Solución eficiente:
1. Encuentra el medio (algoritmo dos punteros)
2. Invierte la segunda mitad
3. Compara primera mitad con segunda mitad invertida
4. Restaura la segunda mitad (opcional)

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
        Complejidad: O(n) tiempo, O(1) memoria.
        """
        if self.head is None or self.head.next is None:
            return True

        #  Encontrar el medio
        lento = self.head
        rapido = self.head

        while rapido and rapido.next:
            lento = lento.next
            rapido = rapido.next.next

        #  Invertir la segunda mitad
        prev = None
        actual = lento

        while actual:
            sig = actual.next
            actual.next = prev
            prev = actual
            actual = sig

        #  Comparar ambas mitades
        p1 = self.head
        p2 = prev
        es_palindromo = True

        while p2:
            if p1.dato != p2.dato:
                es_palindromo = False
                break
            p1 = p1.next
            p2 = p2.next

        #  Restaurar la lista
        actual = prev
        prev = None

        while actual:
            sig = actual.next
            actual.next = prev
            prev = actual
            actual = sig

        return es_palindromo


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

lista1 = SLinkedList([1, 2, 3, 2, 1])
print(lista1)
print(lista1.is_palindrome())  # True

lista2 = SLinkedList([1, 2, 3, 4, 5])
print(lista2)
print(lista2.is_palindrome())  # False


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

Implementa un método rotate(k) que rote la lista k posiciones a la derecha.

Ejemplo:
    lista = [1, 2, 3, 4, 5]
    lista.rotate(2)
    print(lista)  # Output: 4 → 5 → 1 → 2 → 3 → None

Pasos:
1. Conectar el último nodo con el primero (hacer circular)
2. Encontrar el nuevo head (en posición size - k)
3. Romper el círculo

Complejidad esperada: O(n)
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

        k = k % self.size
        if k == 0:
            return

        # 1️⃣ Encontrar el último nodo
        tail = self.head
        while tail.next:
            tail = tail.next

        # 2️⃣ Convertir en lista circular
        tail.next = self.head

        # 3️⃣ Encontrar el nuevo tail (size - k - 1)
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

lista = SLinkedList([1, 2, 3, 4, 5])

print("Antes:")
print(lista)

lista.rotate(2)

print("Después:")
print(lista)
# 4 → 5 → 1 → 2 → 3 → None


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

Implementa un método partition(x) que reorganice la lista de modo que
todos los elementos menores que x aparezcan antes que los elementos
mayores o iguales a x. El orden relativo dentro de cada grupo debe preservarse.

Ejemplo:
    lista = [3, 5, 8, 5, 10, 2, 1]
    lista.partition(5)
    # Resultado: [3, 2, 1] + [5, 8, 5, 10]
    # O cualquier permutación donde menores a 5 estén primero

Pista: Crea dos listas auxiliares (menores y mayores) y luego únelas.
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
            actual.next = None  # desconectar nodo

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

        # Unir ambas listas
        if menores_tail:
            menores_tail.next = mayores_head
            self.head = menores_head
        else:
            self.head = mayores_head


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

lista = SLinkedList([3, 5, 8, 5, 10, 2, 1])

print("Antes:")
print(lista)

lista.partition(5)

print("Después:")
print(lista)
# 3 → 2 → 1 → 5 → 8 → 5 → 10 → None


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

Tienes dos listas enlazadas que representan números (cada nodo es un dígito).
Los dígitos están almacenados en ORDEN INVERSO (el primer nodo es la unidad).

Implementa una función add_numbers(list1, list2) que sume ambos números
y retorne el resultado como una nueva lista enlazada.

Ejemplo:
    list1 = [2, 4, 3] representa 342
    list2 = [5, 6, 4] representa 465
    add_numbers(list1, list2) = [7, 0, 8] representa 807

Pista: Es como sumar manualmente, llevando el "carry".
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


def add_numbers(list1, list2):
    """
    Suma dos números representados por listas enlazadas.
    Cada nodo contiene un dígito y los dígitos están en orden inverso.
    Complejidad: O(n)
    """
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

lista1 = SLinkedList([2, 4, 3])   # 342
lista2 = SLinkedList([5, 6, 4])   # 465

resultado = add_numbers(lista1, lista2)

print("Resultado:")
print(resultado)
# 7 → 0 → 8 → None


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

Dadas dos listas enlazadas, determina si se intersectan (comparten nodos)
y encuentra el nodo donde se intersectan.

Ejemplo:
    list1: 1 → 2 → 3 ↘
                      7 → 8 → 9
    list2: 4 → 5 → 6 ↗
    
    Retorna el nodo con valor 7 (primer nodo compartido)

Solución eficiente:
1. Calcula la longitud de ambas listas
2. Alinea los inicios (avanza en la lista más larga)
3. Avanza simultáneamente hasta encontrar el nodo común

Complejidad: O(n + m) tiempo, O(1) espacio
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
        nuevo = Nodo(dato)

        if self.head is None:
            self.head = nuevo
            return

        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = nuevo


def longitud(lista):
    """
    Calcula la longitud de una lista enlazada.
    Complejidad temporal: O(n)
    Complejidad espacial: O(1)
    """
    actual = lista.head
    contador = 0

    while actual:
        contador += 1
        actual = actual.next

    return contador


def get_intersection_node(list1, list2):
    """
    Retorna el nodo de intersección entre dos listas enlazadas.
    Si no existe intersección, retorna None.

    Estrategia:
    1. Calcular longitudes
    2. Alinear los punteros
    3. Avanzar simultáneamente comparando nodos (no valores)

    Complejidad temporal: O(n + m)
    Complejidad espacial: O(1)
    """
    if not list1.head or not list2.head:
        return None

    len1 = longitud(list1)
    len2 = longitud(list2)

    p1 = list1.head
    p2 = list2.head

    # Alinear inicios
    if len1 > len2:
        for _ in range(len1 - len2):
            p1 = p1.next
    else:
        for _ in range(len2 - len1):
            p2 = p2.next

    # Avanzar simultáneamente
    while p1 and p2:
        if p1 is p2:   # comparación por referencia
            return p1
        p1 = p1.next
        p2 = p2.next

    return None


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

# Crear nodos compartidos
n7 = Nodo(7)
n8 = Nodo(8)
n9 = Nodo(9)

n7.next = n8
n8.next = n9

# Lista 1: 1 → 2 → 3 → 7 → 8 → 9
list1 = SLinkedList([1, 2, 3])
actual = list1.head
while actual.next:
    actual = actual.next
actual.next = n7

# Lista 2: 4 → 5 → 6 → 7 → 8 → 9
list2 = SLinkedList([4, 5, 6])
actual = list2.head
while actual.next:
    actual = actual.next
actual.next = n7

interseccion = get_intersection_node(list1, list2)

if interseccion:
    print("Nodo de intersección:", interseccion.dato)
else:
    print("No hay intersección")


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    # Caso con intersección
    n1 = Nodo(10)
    n2 = Nodo(20)
    n1.next = n2

    l1 = SLinkedList([1, 2])
    l2 = SLinkedList([3])

    l1.head.next.next = n1
    l2.head.next = n1

    assert get_intersection_node(l1, l2) is n1

    # Caso sin intersección
    l1 = SLinkedList([1, 2, 3])
    l2 = SLinkedList([4, 5, 6])
    assert get_intersection_node(l1, l2) is None

    # Caso lista vacía
    l1 = SLinkedList()
    l2 = SLinkedList([1])
    assert get_intersection_node(l1, l2) is None


_pruebas_internas()



"""
EJERCICIO 16: Navegador Web
Dificultad: 🟡 Intermedio
Tiempo estimado: 40 minutos

Implementa una clase BrowserHistory que simule el historial de un navegador
usando una lista doblemente enlazada.

Métodos requeridos:
- __init__(homepage): Inicia con la página de inicio
- visit(url): Visita una nueva URL (elimina historial futuro)
- back(steps): Retrocede 'steps' páginas (máximo hasta el inicio)
- forward(steps): Avanza 'steps' páginas (máximo hasta el final)
- get_current(): Retorna la URL actual

Ejemplo:
    browser = BrowserHistory("google.com")
    browser.visit("youtube.com")    # google.com → youtube.com
    browser.visit("facebook.com")   # ... → facebook.com
    browser.back(1)                 # Vuelve a youtube.com
    browser.forward(1)              # Regresa a facebook.com
"""


class Nodo:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    """
    Implementación de historial de navegador usando lista doblemente enlazada.
    Permite visitar páginas, retroceder y avanzar.
    """

    def __init__(self, homepage):
        self.current = Nodo(homepage)

    def visit(self, url):
        """
        Visita una nueva página.
        Elimina el historial futuro.
        Complejidad: O(1)
        """
        nuevo = Nodo(url)

        # eliminar historial futuro
        self.current.next = None

        # enlazar nuevo nodo
        nuevo.prev = self.current
        self.current.next = nuevo

        # mover actual
        self.current = nuevo

    def back(self, steps):
        """
        Retrocede hasta 'steps' páginas o hasta el inicio.
        Complejidad: O(steps)
        """
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps):
        """
        Avanza hasta 'steps' páginas o hasta el final.
        Complejidad: O(steps)
        """
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url

    def get_current(self):
        """Retorna la página actual."""
        return self.current.url


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

browser = BrowserHistory("google.com")

browser.visit("youtube.com")
browser.visit("facebook.com")

browser.back(1)        # youtube.com
browser.forward(1)     # facebook.com

print(browser.get_current())  # facebook.com


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    browser = BrowserHistory("inicio.com")
    assert browser.get_current() == "inicio.com"

    browser.visit("a.com")
    browser.visit("b.com")
    browser.visit("c.com")

    assert browser.back(1) == "b.com"
    assert browser.back(1) == "a.com"
    assert browser.back(5) == "inicio.com"

    assert browser.forward(2) == "b.com"

    browser.visit("x.com")
    assert browser.forward(2) == "x.com"  # historial futuro eliminado


_pruebas_internas()



"""
EJERCICIO 17: LRU Cache
Dificultad: 🔴 Avanzado
Tiempo estimado: 60 minutos

Implementa una estructura de datos LRU Cache (Least Recently Used Cache)
usando una lista doblemente enlazada + diccionario.

El cache tiene capacidad limitada. Cuando se llena, elimina el elemento
usado menos recientemente.

Métodos:
- __init__(capacity): Crea cache con capacidad dada
- get(key): Obtiene el valor (marca como usado recientemente)
- put(key, value): Inserta/actualiza (elimina LRU si está lleno)

Ambos métodos deben ser O(1).

Pista: 
- Diccionario: para acceso O(1) por key
- Lista doble: para mantener orden de uso (más reciente al final)
"""

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

        # Nodos ficticios (dummy)
        self.head = Nodo(0, 0)  # LRU
        self.tail = Nodo(0, 0)  # MRU
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, nodo):
        """
        Elimina un nodo de la lista.
        Complejidad: O(1)
        """
        prev = nodo.prev
        next = nodo.next
        prev.next = next
        next.prev = prev

    def _add_to_end(self, nodo):
        """
        Agrega un nodo antes del tail (más reciente).
        Complejidad: O(1)
        """
        prev = self.tail.prev
        prev.next = nodo
        nodo.prev = prev
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

        # mover a más recientemente usado
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
                # eliminar LRU
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]

            nuevo = Nodo(key, value)
            self.cache[key] = nuevo
            self._add_to_end(nuevo)


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))  # 10

cache.put(3, 30)     # elimina key 2 (LRU)

print(cache.get(2))  # -1
print(cache.get(3))  # 30
print(cache.get(1))  # 10


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

    cache.put(3, 3)     # elimina 2
    assert cache.get(2) == -1

    cache.put(4, 4)     # elimina 1
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

Funcionalidades:
- add_cursor(position): Agregar cursor en posición
- remove_cursor(cursor_id): Eliminar cursor
- type_at_cursor(cursor_id, text): Escribir en cursor específico
- undo_all(): Deshacer en todos los cursores
- redo_all(): Rehacer en todos los cursores

Esto requiere mantener múltiples historiales sincronizados.
"""


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

        # insertar texto
        self.document = self.document[:pos] + text + self.document[pos:]

        # actualizar posiciones de cursores
        for cid in self.cursors:
            if self.cursors[cid] > pos:
                self.cursors[cid] += len(text)

        # mover cursor actual
        self.cursors[cursor_id] += len(text)

        # registrar acción
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

        # eliminar texto
        self.document = self.document[:pos] + self.document[pos + length:]

        # ajustar cursores
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

        # reinsertar texto
        self.document = self.document[:pos] + text + self.document[pos:]

        # ajustar cursores
        for cid in self.cursors:
            if self.cursors[cid] > pos:
                self.cursors[cid] += len(text)

        self.undo_stack.append(action)


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

editor = MultiCursorEditor()

c1 = editor.add_cursor(0)
c2 = editor.add_cursor(0)

editor.type_at_cursor(c1, "Hola")
editor.type_at_cursor(c2, "Hey ")

print(editor.document)  # Hey Hola

editor.undo_all()
print(editor.document)  # Hola

editor.redo_all()
print(editor.document)  # Hey Hola


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

Escribe un programa que compare el rendimiento de:
- Arrays (listas de Python)
- Listas simplemente enlazadas
- Listas doblemente enlazadas

Para las siguientes operaciones:
1. Inserción al inicio (1000 elementos)
2. Inserción al final (1000 elementos)
3. Eliminación al inicio (1000 elementos)
4. Eliminación al final (1000 elementos)
5. Acceso por índice (1000 accesos aleatorios)

Usa el módulo 'time' para medir el tiempo.
Imprime los resultados en una tabla comparativa.
"""

import time
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SinglyLinkedList:
    """
    Lista simplemente enlazada.
    Inserciones eficientes al inicio y al final (con tail).
    """

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


class DoublyLinkedList:
    """
    Lista doblemente enlazada.
    Inserciones y eliminaciones eficientes en ambos extremos.
    """

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


def benchmark():
    """
    Compara el rendimiento entre:
    - Array (list)
    - Singly Linked List
    - Doubly Linked List

    Operaciones:
    - Insertar inicio
    - Insertar final
    - Eliminar inicio
    - Eliminar final
    - Acceso por índice
    """
    N = 1000
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

    # ===== SINGLY LINKED LIST =====
    sll = SinglyLinkedList()
    start = time.time()
    for i in range(N):
        sll.insert_start(i)
    results["SLL insert start"] = time.time() - start

    sll = SinglyLinkedList()
    start = time.time()
    for i in range(N):
        sll.insert_end(i)
    results["SLL insert end"] = time.time() - start

    start = time.time()
    for _ in range(N):
        sll.remove_start()
    results["SLL remove start"] = time.time() - start

    sll = SinglyLinkedList()
    for i in range(N):
        sll.insert_end(i)
    start = time.time()
    for _ in range(N):
        sll.remove_end()
    results["SLL remove end"] = time.time() - start

    sll = SinglyLinkedList()
    for i in range(N):
        sll.insert_end(i)
    start = time.time()
    for i in indices:
        _ = sll.get(i)
    results["SLL access"] = time.time() - start

    # ===== DOUBLY LINKED LIST =====
    dll = DoublyLinkedList()
    start = time.time()
    for i in range(N):
        dll.insert_start(i)
    results["DLL insert start"] = time.time() - start

    dll = DoublyLinkedList()
    start = time.time()
    for i in range(N):
        dll.insert_end(i)
    results["DLL insert end"] = time.time() - start

    start = time.time()
    for _ in range(N):
        dll.remove_start()
    results["DLL remove start"] = time.time() - start

    dll = DoublyLinkedList()
    for i in range(N):
        dll.insert_end(i)
    start = time.time()
    for _ in range(N):
        dll.remove_end()
    results["DLL remove end"] = time.time() - start

    dll = DoublyLinkedList()
    for i in range(N):
        dll.insert_end(i)
    start = time.time()
    for i in indices:
        _ = dll.get(i)
    results["DLL access"] = time.time() - start

    # ===== PRINT RESULTS =====
    print("\n--- BENCHMARK (1000 operaciones) ---")
    for k, v in results.items():
        print(f"{k:25} {v:.6f} s")


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

benchmark()


# =========================
# PRUEBAS INTERNAS
# =========================

def _pruebas_internas():
    sll = SinglyLinkedList()
    sll.insert_end(1)
    sll.insert_end(2)
    sll.insert_end(3)
    assert sll.get(1) == 2
    sll.remove_start()
    assert sll.get(0) == 2

    dll = DoublyLinkedList()
    dll.insert_start(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.remove_end()
    assert dll.get(1) == 2


_pruebas_internas()



"""
EJERCICIO 20: Análisis de casos de uso
Dificultad: 🟡 Intermedio
Tiempo estimado: 20 minutos

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


"""
EJERCICIO 20: Análisis de casos de uso
"""

1. Sistema de colas de impresión (FIFO estricto)
 Estructura apropiada: Lista Simple
 Justificación:
 Se insertan elementos al final y se eliminan al inicio.
 Ambas operaciones pueden hacerse en O(1) usando head y tail.
 Un Array sería ineficiente al eliminar al inicio (O(n)).


2. Historial de navegación de un navegador
Estructura apropiada: Lista Doble
Justificación:
Se necesita navegar hacia atrás y hacia adelante.
La lista doble permite moverse en ambas direcciones en O(1).
Es el modelo clásico usado en navegadores.


3. Sistema de undo/redo con límite de 100 acciones
Estructura apropiada: Array
Justificación:
El tamaño es pequeño y fijo.
Acceso rápido al último elemento.
Push y pop en O(1) usando el final del array.
Más simple que usar listas enlazadas.


4. Base de datos que necesita acceso rápido por ID
Estructura apropiada: Array
Justificación:
Acceso directo por índice en O(1).
Ideal cuando el ID puede mapearse a una posición.
Las listas enlazadas tienen acceso O(n), por lo que no son adecuadas.


5. Playlist de música con navegación adelante/atrás
Estructura apropiada: Lista Doble
Justificación:
Se requiere moverse al siguiente y al anterior.
Inserciones y eliminaciones dinámicas.
Navegación bidireccional eficiente en O(1).


6. Sistema de gestión de memoria del OS
Estructura apropiada: Lista Doble
Justificación:
Permite dividir y unir bloques de memoria.
Eliminaciones e inserciones frecuentes.
Navegación hacia adelante y atrás entre bloques.


7. Editor de texto que solo permite append al final
Estructura apropiada: Array
Justificación:
Solo se insertan elementos al final.
Append es O(1) amortizado.
Mejor rendimiento de memoria y caché que listas enlazadas.


8. Implementación de una pila (Stack)
Estructura apropiada: Array
Justificación:
Operaciones push y pop al final en O(1).
Implementación sencilla.
No se necesita inserción/eliminación en medio.


9. Juego que necesita insertar/eliminar enemigos frecuentemente
Estructura apropiada: Lista Simple
Justificación:
Inserciones y eliminaciones frecuentes.
No importa el acceso por índice.
Evita el costo O(n) de desplazar elementos como en arrays.


10. Sistema de logs que solo escribe al final y lee todo
Estructura apropiada: Array
Justificación:
Escritura secuencial al final.
Lectura completa eficiente.
Mejor uso de memoria y rendimiento que listas enlazadas.







