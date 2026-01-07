


#Eddy Alexander Vera Bailon
#fecha: 18/12/2025
#Ejercicios: Todos


# EJERCICIOS PRÁCTICOS - LISTAS ENLAZADAS
# Unidad 3: Estructura de Datos
# ULEAM - Ingeniería en Software



# ============================================================
# ARCHIVO ÚNICO – LISTAS ENLAZADAS Y APLICACIONES
# EJERCICIOS 1 AL 20
# ============================================================
# =============================
# ESTRUCTURAS BASE UNIFICADAS
# =============================

# Clase Nodo: representa un elemento de la lista enlazada
class Nodo:
    def __init__(self, data=None):
        self.data = data      # Dato almacenado en el nodo
        self.next = None      # Referencia al siguiente nodo


# Clase de Lista Enlazada Simple
class SLinkedList:
    def __init__(self):
        self.head = None      # Referencia al primer nodo de la lista

    # Verifica si la lista está vacía
    def is_empty(self):
        return self.head is None

    # Agrega un elemento al final de la lista
    def append(self, data):
        nuevo = Nodo(data)
        if self.is_empty():
            self.head = nuevo
        else:
            actual = self.head
            # Recorre la lista hasta el último nodo
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def to_list(self):
        resultado = []
        actual = self.head
        while actual:
            resultado.append(actual.data)
            actual = actual.next
        return resultado

    # Devuelve una representación visual de la lista
    def to_string(self):
        if self.is_empty():
            return "None"
        actual = self.head
        s = ""
        while actual:
            s += str(actual.data) + " -> "
            actual = actual.next
        return s + "None"


# ============================================================
# EJERCICIO 1
# Insertar un elemento al inicio de la lista
# ============================================================

# Inserta un nuevo nodo al inicio de la lista
def insert_at_beginning(lista, valor):
    nuevo = Nodo(valor)        # Se crea el nuevo nodo
    nuevo.next = lista.head   # El nuevo nodo apunta al antiguo head
    lista.head = nuevo        # El nuevo nodo se convierte en el head


print("\n=== EJERCICIO 1 ===")
lista1 = SLinkedList()
lista1.append(10)
lista1.append(20)
insert_at_beginning(lista1, 5)
print("Resultado original:", lista1.to_string())

# Resultados adicionales
lista1b = SLinkedList()
insert_at_beginning(lista1b, 100)
print("Resultado 1:", lista1b.to_string())

lista1c = SLinkedList()
lista1c.append(1)
insert_at_beginning(lista1c, 0)
print("Resultado 2:", lista1c.to_string())

lista1d = SLinkedList()
lista1d.append(7)
lista1d.append(8)
insert_at_beginning(lista1d, -1)
print("Resultado 3:", lista1d.to_string())


# ============================================================
# EJERCICIO 2
# Contar nodos de la lista
# ============================================================

# Cuenta la cantidad de nodos en la lista
def count_nodes(lista):
    contador = 0
    actual = lista.head
    # Recorre la lista incrementando el contador
    while actual:
        contador += 1
        actual = actual.next
    return contador


print("\n=== EJERCICIO 2 ===")
lista2 = SLinkedList()
lista2.append(1)
lista2.append(2)
lista2.append(3)
print("Resultado original:", count_nodes(lista2))

# Resultados adicionales
print("Resultado 1 (lista vacía):", count_nodes(SLinkedList()))

lista2b = SLinkedList()
lista2b.append(99)
print("Resultado 2:", count_nodes(lista2b))

lista2c = SLinkedList()
for i in range(10):
    lista2c.append(i)
print("Resultado 3:", count_nodes(lista2c))


# ============================================================
# EJERCICIO 3
# Buscar un elemento en la lista
# ============================================================

# Busca un valor específico dentro de la lista
def search(lista, valor):
    actual = lista.head
    # Recorre la lista comparando cada dato
    while actual:
        if actual.data == valor:
            return True        # Se encontró el valor
        actual = actual.next
    return False               # No se encontró el valor


print("\n=== EJERCICIO 3 ===")
lista3 = SLinkedList()
lista3.append(4)
lista3.append(8)
lista3.append(15)
print("Resultado original:", search(lista3, 8))

# Resultados adicionales
print("Resultado 1:", search(lista3, 100))
print("Resultado 2:", search(lista3, 4))
print("Resultado 3:", search(SLinkedList(), 1))


# ============================================================
# EJERCICIO 4
# Eliminar un elemento de la lista
# ============================================================

# Elimina la primera aparición de un valor en la lista
def delete_value(lista, valor):
    # Caso 1: lista vacía
    if lista.is_empty():
        return

    # Caso 2: el valor está en el primer nodo
    if lista.head.data == valor:
        lista.head = lista.head.next
        return

    # Caso 3: el valor está en otro nodo
    actual = lista.head
    while actual.next:
        if actual.next.data == valor:
            actual.next = actual.next.next
            return
        actual = actual.next


print("\n=== EJERCICIO 4 ===")
lista4 = SLinkedList()
lista4.append(1)
lista4.append(2)
lista4.append(3)
delete_value(lista4, 2)
print("Resultado original:", lista4.to_string())

# Resultados adicionales
lista4b = SLinkedList()
lista4b.append(5)
delete_value(lista4b, 5)
print("Resultado 1:", lista4b.to_string())

lista4c = SLinkedList()
lista4c.append(7)
lista4c.append(8)
delete_value(lista4c, 100)
print("Resultado 2:", lista4c.to_string())

lista4d = SLinkedList()
delete_value(lista4d, 1)
print("Resultado 3:", lista4d.to_string())


# ============================================================
# EJERCICIO 5
# Invertir la lista
# ============================================================

# Invierte el orden de los nodos de la lista
def reverse_list(lista):
    prev = None
    current = lista.head
    # Recorre la lista cambiando las referencias
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    lista.head = prev



print("\n=== EJERCICIO 5 ===")
lista5 = SLinkedList()
for i in [1, 2, 3]:
    lista5.append(i)
reverse_list(lista5)
print("Resultado original:", lista5.to_string())

# Aquí se imprime el estado FINAL de la lista luego de aplicar
# la función reverse_list(lista5)

# to_string() se usa para mostrar el contenido de la lista enlazada
# de forma legible (nodo por nodo) después de invertir

lista5b = SLinkedList()
reverse_list(lista5b)
print("Resultado 1:", lista5b.to_string())

lista5c = SLinkedList()
lista5c.append(9)
reverse_list(lista5c)
print("Resultado 2:", lista5c.to_string())

lista5d = SLinkedList()
for i in range(5):
    lista5d.append(i)
reverse_list(lista5d)
print("Resultado 3:", lista5d.to_string())


# ============================================================
# EJERCICIO 6
# Obtener el valor máximo
# ============================================================

# Devuelve el valor máximo almacenado en la lista
def max_value(lista):
    # Si la lista está vacía, no hay máximo
    if lista.is_empty():
        return None

    actual = lista.head
    maximo = actual.data
    # Recorre la lista comparando valores
    while actual:
        if actual.data > maximo:
            maximo = actual.data
        actual = actual.next
    return maximo


print("\n=== EJERCICIO 6 ===")
lista6 = SLinkedList()
for i in [4, 9, 1]:
    lista6.append(i)
print("Resultado original:", max_value(lista6))

print("Resultado 1:", max_value(SLinkedList()))

lista6b = SLinkedList()
lista6b.append(-10)
lista6b.append(-3)
print("Resultado 2:", max_value(lista6b))

lista6c = SLinkedList()
for i in range(100):
    lista6c.append(i)
print("Resultado 3:", max_value(lista6c))

# ============================================================
# EJERCICIO 7
# Comparar dos listas
# ============================================================

def compare_lists(l1, l2):
    """
    Compara dos listas enlazadas nodo por nodo.
    Retorna True si tienen los mismos valores en el mismo orden
    y además tienen la misma longitud.
    """
    a = l1.head   # Apunta al primer nodo de la lista 1
    b = l2.head   # Apunta al primer nodo de la lista 2

    # Mientras ambas listas tengan nodos por recorrer
    while a and b:
        # Si los datos no coinciden, las listas son distintas
        if a.data != b.data:
            return False
        # Avanzamos en ambas listas
        a = a.next
        b = b.next

    # Si ambas llegaron al final al mismo tiempo, son iguales
    # Si una terminó antes que la otra, no lo son
    return a is None and b is None


print("\n=== EJERCICIO 7 ===")

# Caso base: dos listas iguales
l7a = SLinkedList()
l7b = SLinkedList()
for i in [1, 2, 3]:
    l7a.append(i)
    l7b.append(i)
print("Resultado original:", compare_lists(l7a, l7b))  # True

# Caso: dos listas vacías
l7c = SLinkedList()
l7d = SLinkedList()
print("Resultado 1:", compare_lists(l7c, l7d))  # True

# Caso: mismo tamaño, distinto contenido
l7e = SLinkedList()
l7f = SLinkedList()
l7e.append(1)
l7f.append(2)
print("Resultado 2:", compare_lists(l7e, l7f))  # False

# Caso: distinto tamaño
l7g = SLinkedList()
l7h = SLinkedList()
l7g.append(1)
print("Resultado 3:", compare_lists(l7g, l7h))  # False


# ============================================================
# EJERCICIO 8
# Concatenar dos listas
# ============================================================

def concatenate(l1, l2):
    """
    Une la lista l2 al final de la lista l1.
    No crea nodos nuevos, solo conecta referencias.
    """
    # Si la primera lista está vacía, simplemente apunta a la segunda
    if l1.is_empty():
        l1.head = l2.head
        return

    # Recorremos l1 hasta llegar al último nodo
    actual = l1.head
    while actual.next:
        actual = actual.next

    # El último nodo de l1 ahora apunta al inicio de l2
    actual.next = l2.head


print("\n=== EJERCICIO 8 ===")

# Caso normal: concatenar dos listas con datos
l8a = SLinkedList()
l8b = SLinkedList()
for i in [1, 2]:
    l8a.append(i)
for i in [3, 4]:
    l8b.append(i)
concatenate(l8a, l8b)
print("Resultado original:", l8a.to_string())  
# to_string() muestra la lista visualmente: 1 -> 2 -> 3 -> 4 -> None

# Caso: primera lista vacía
l8c = SLinkedList()
l8d = SLinkedList()
l8d.append(9)
concatenate(l8c, l8d)
print("Resultado 1:", l8c.to_string())

# Caso: ambas listas vacías
l8e = SLinkedList()
l8f = SLinkedList()
concatenate(l8e, l8f)
print("Resultado 2:", l8e.to_string())

# Caso: segunda lista vacía
l8g = SLinkedList()
for i in range(3):
    l8g.append(i)
concatenate(l8g, SLinkedList())
print("Resultado 3:", l8g.to_string())


# ============================================================
# EJERCICIO 9
# Eliminar duplicados
# ============================================================

def remove_duplicates(lista):
    """
    Elimina valores repetidos de la lista enlazada.
    Usa un set para recordar qué valores ya aparecieron.
    """
    vistos = set()      # Guarda los valores ya encontrados
    actual = lista.head
    prev = None         # Nodo anterior, necesario para eliminar

    while actual:
        if actual.data in vistos:
            # Si el valor ya existe, saltamos el nodo actual
            prev.next = actual.next
        else:
            # Si es nuevo, lo guardamos y avanzamos prev
            vistos.add(actual.data)
            prev = actual
        actual = actual.next


print("\n=== EJERCICIO 9 ===")

lista9 = SLinkedList()
for i in [1, 2, 2, 3]:
    lista9.append(i)
remove_duplicates(lista9)
print("Resultado original:", lista9.to_string())

# Lista vacía
lista9b = SLinkedList()
remove_duplicates(lista9b)
print("Resultado 1:", lista9b.to_string())

# Todos los elementos duplicados
lista9c = SLinkedList()
for i in [5, 5, 5]:
    lista9c.append(i)
remove_duplicates(lista9c)
print("Resultado 2:", lista9c.to_string())

# Lista sin duplicados
lista9d = SLinkedList()
for i in range(5):
    lista9d.append(i)
remove_duplicates(lista9d)
print("Resultado 3:", lista9d.to_string())


# ============================================================
# EJERCICIO 10
# Obtener el elemento del medio
# ============================================================

def middle_element(lista):
    """
    Devuelve el elemento central de la lista.
    Usa dos punteros:
    - slow avanza de uno en uno
    - fast avanza de dos en dos
    Cuando fast llega al final, slow está en el medio.
    """
    slow = lista.head
    fast = lista.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Si la lista está vacía, slow será None
    return slow.data if slow else None


print("\n=== EJERCICIO 10 ===")

# Lista impar
l10 = SLinkedList()
for i in [1, 2, 3, 4, 5]:
    l10.append(i)
print("Resultado original:", middle_element(l10))  # 3

# Lista vacía
print("Resultado 1:", middle_element(SLinkedList()))

# Lista con un solo elemento
l10b = SLinkedList()
l10b.append(10)
print("Resultado 2:", middle_element(l10b))

# Lista par (devuelve el segundo del centro)
l10c = SLinkedList()
for i in [1, 2, 3, 4]:
    l10c.append(i)
print("Resultado 3:", middle_element(l10c))


# ============================================================
# EJERCICIO 11
# Detectar ciclo en la lista
# ============================================================

def has_cycle(lista):
    """
    Detecta si una lista tiene un ciclo.
    Usa el algoritmo de Floyd (tortuga y liebre).
    """
    slow = lista.head
    fast = lista.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # Si se encuentran, hay ciclo
        if slow == fast:
            return True

    return False


print("\n=== EJERCICIO 11 ===")

# Lista sin ciclo
l11 = SLinkedList()
for i in [1, 2, 3]:
    l11.append(i)
print("Resultado original:", has_cycle(l11))  # False

# Crear un ciclo manualmente:
# el último nodo apunta al primero
l11.head.next.next.next = l11.head
print("Resultado 1 (con ciclo):", has_cycle(l11))

# Lista vacía
print("Resultado 2:", has_cycle(SLinkedList()))

# Ciclo en un solo nodo
l11b = SLinkedList()
l11b.append(1)
l11b.head.next = l11b.head
print("Resultado 3:", has_cycle(l11b))


# ============================================================
# EJERCICIO 12
# Historial del navegador (BrowserHistory)
# ============================================================

class BrowserHistory:
    """
    Simula el historial de un navegador usando dos pilas:
    - back_stack: páginas anteriores
    - forward_stack: páginas siguientes
    """

    def __init__(self, homepage):
        self.back_stack = []      # Historial hacia atrás
        self.forward_stack = []   # Historial hacia adelante
        self.current = homepage  # Página actual

    def visit(self, url):
        # Guardamos la página actual en el historial atrás
        self.back_stack.append(self.current)
        self.current = url
        # Al visitar una nueva página, se borra el forward
        self.forward_stack.clear()

    def back(self):
        # Volver atrás si es posible
        if self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
        return self.current

    def forward(self):
        # Avanzar si es posible
        if self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
        return self.current


print("\n=== EJERCICIO 12 ===")

bh = BrowserHistory("google.com")
bh.visit("youtube.com")
bh.visit("github.com")

# Volver una página
print("Resultado original:", bh.back())  # youtube.com

# Volver otra vez
print("Resultado 1:", bh.back())         # google.com

# Avanzar
print("Resultado 2:", bh.forward())      # youtube.com

# Visitar nueva página invalida el forward
bh.visit("openai.com")
print("Resultado 3:", bh.current)

# ============================================================
# EJERCICIO 13
# Caché LRU (Least Recently Used)
# ============================================================

class LRUCache:
    def __init__(self, capacity):
        # Capacidad máxima del caché
        self.capacity = capacity
        # Diccionario que almacena los pares clave-valor
        # El orden importa: el primer elemento es el menos usado
        self.cache = {}

    def get(self, key):
        # Si la clave no existe, se devuelve -1 (convención del ejercicio)
        if key not in self.cache:
            return -1

        # Se elimina y se vuelve a insertar para marcarla como "recientemente usada"
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key, value):
        # Si la clave ya existe, se elimina primero
        if key in self.cache:
            self.cache.pop(key)

        # Si se supera la capacidad, se elimina el elemento menos usado
        # next(iter(self.cache)) obtiene la primera clave del diccionario
        elif len(self.cache) >= self.capacity:
            self.cache.pop(next(iter(self.cache)))

        # Se inserta el nuevo valor como el más recientemente usado
        self.cache[key] = value


print("\n=== EJERCICIO 13 ===")
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print("Resultado original:", cache.get(1))

cache.put(3, 3)
print("Resultado 1:", cache.get(2))

cache.put(4, 4)
print("Resultado 2:", cache.get(1))
print("Resultado 3:", cache.get(4))


# ============================================================
# EJERCICIO 14
# Editor de texto con cursor
# ============================================================

class TextEditor:
    def __init__(self):
        # Lista de caracteres que forman el texto
        self.text = []
        # Posición actual del cursor
        self.cursor = 0

    def insert(self, char):
        # Inserta el carácter en la posición del cursor
        self.text.insert(self.cursor, char)
        # Avanza el cursor después de insertar
        self.cursor += 1

    def move_left(self):
        # Mueve el cursor a la izquierda si es posible
        if self.cursor > 0:
            self.cursor -= 1

    def move_right(self):
        # Mueve el cursor a la derecha si no se pasa del texto
        if self.cursor < len(self.text):
            self.cursor += 1

    def get_text(self):
        # Convierte la lista de caracteres en una cadena
        return "".join(self.text)


print("\n=== EJERCICIO 14 ===")
ed = TextEditor()
ed.insert('H')
ed.insert('i')
print("Resultado original:", ed.get_text())

ed.move_left()
ed.insert('!')
print("Resultado 1:", ed.get_text())

ed.move_right()
ed.insert('?')
print("Resultado 2:", ed.get_text())

ed2 = TextEditor()
print("Resultado 3:", ed2.get_text())


# ============================================================
# EJERCICIO 15
# Sumar todos los elementos de una lista enlazada
# ============================================================

def sum_list(lista):
    total = 0
    # Se empieza desde la cabeza de la lista enlazada
    actual = lista.head

    # Recorre nodo por nodo hasta llegar al final
    while actual:
        total += actual.data
        actual = actual.next

    return total


print("\n=== EJERCICIO 15 ===")
l15 = SLinkedList()
for i in [1, 2, 3]:
    l15.append(i)
print("Resultado original:", sum_list(l15))

# Lista vacía, la suma es 0
print("Resultado 1:", sum_list(SLinkedList()))

l15b = SLinkedList()
l15b.append(10)
print("Resultado 2:", sum_list(l15b))

l15c = SLinkedList()
for i in range(1, 11):
    l15c.append(i)
print("Resultado 3:", sum_list(l15c))


# ============================================================
# EJERCICIO 16
# Insertar un valor en una posición específica
# ============================================================

def insert_at_position(lista, valor, posicion):
    # Si la posición es inválida o la lista está vacía,
    # se inserta al inicio
    if posicion <= 0 or lista.is_empty():
        insert_at_beginning(lista, valor)
        return

    actual = lista.head
    indice = 0

    # Se avanza hasta llegar a la posición anterior a la deseada
    while actual.next and indice < posicion - 1:
        actual = actual.next
        indice += 1

    # Se crea el nuevo nodo
    nuevo = Nodo(valor)
    # Se ajustan los enlaces
    nuevo.next = actual.next
    actual.next = nuevo


print("\n=== EJERCICIO 16 ===")
l16 = SLinkedList()
for i in [1, 2, 4]:
    l16.append(i)
insert_at_position(l16, 3, 2)
# to_string() convierte la lista enlazada en texto legible
print("Resultado original:", l16.to_string())

l16b = SLinkedList()
insert_at_position(l16b, 5, 0)
print("Resultado 1:", l16b.to_string())

l16c = SLinkedList()
l16c.append(1)
insert_at_position(l16c, 2, 5)
print("Resultado 2:", l16c.to_string())

l16d = SLinkedList()
for i in [10, 20]:
    l16d.append(i)
insert_at_position(l16d, 15, 1)
print("Resultado 3:", l16d.to_string())


# ============================================================
# EJERCICIO 17
# Intersección de dos listas enlazadas
# ============================================================

def intersection(l1, l2):
    # Convierte la primera lista en un set para búsqueda rápida
    set1 = set(l1.to_list())

    resultado = SLinkedList()
    actual = l2.head

    # Recorre la segunda lista
    while actual:
        # Si el valor existe en la primera lista, se agrega
        if actual.data in set1:
            resultado.append(actual.data)
        actual = actual.next

    return resultado


print("\n=== EJERCICIO 17 ===")
l17a = SLinkedList()
l17b = SLinkedList()
for i in [1, 2, 3]:
    l17a.append(i)
for i in [2, 3, 4]:
    l17b.append(i)

res17 = intersection(l17a, l17b)
print("Resultado original:", res17.to_string())

print("Resultado 1:", intersection(SLinkedList(), SLinkedList()).to_string())

l17c = SLinkedList()
l17d = SLinkedList()
for i in [5, 6]:
    l17c.append(i)
for i in [7, 8]:
    l17d.append(i)
print("Resultado 2:", intersection(l17c, l17d).to_string())

print("Resultado 3:", intersection(l17a, l17a).to_string())


# ============================================================
# EJERCICIO 18
# Sistema de acciones con undo y redo
# ============================================================

class Action:
    def __init__(self, description):
        # Descripción textual de la acción realizada
        self.description = description


class ActionHistory:
    def __init__(self):
        # Pila de acciones realizadas
        self.undo_stack = []
        # Pila de acciones deshechas
        self.redo_stack = []

    def do(self, action):
        # Se registra una nueva acción
        self.undo_stack.append(action)
        # Al hacer algo nuevo, se invalida el redo
        self.redo_stack.clear()

    def undo(self):
        # Si no hay acciones, no se puede deshacer
        if not self.undo_stack:
            return None

        # Se mueve la acción de undo a redo
        action = self.undo_stack.pop()
        self.redo_stack.append(action)
        return action.description

    def redo(self):
        # Si no hay acciones para rehacer
        if not self.redo_stack:
            return None

        # Se recupera la acción y vuelve a undo
        action = self.redo_stack.pop()
        self.undo_stack.append(action)
        return action.description


print("\n=== EJERCICIO 18 ===")
hist = ActionHistory()
hist.do(Action("Escribir A"))
hist.do(Action("Escribir B"))
print("Resultado original (undo):", hist.undo())

print("Resultado 1 (undo):", hist.undo())
print("Resultado 2 (redo):", hist.redo())
hist.do(Action("Escribir C"))
print("Resultado 3 (nuevo action, redo invalido):", hist.redo())

# ============================================================
# EJERCICIO 19
# Benchmark de operaciones
# ============================================================
# Este ejercicio compara el rendimiento (tiempo de ejecución)
# de distintas operaciones en:
# - Arreglos (listas de Python)
# - Listas enlazadas simples
# - Listas enlazadas dobles

import time     # Para medir el tiempo de ejecución
import random   # Para generar índices aleatorios


# ============================================================
# Clase Nodo
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data    # Valor almacenado
        self.next = None    # Referencia al siguiente nodo
        self.prev = None    # Referencia al nodo anterior (solo en lista doble)


# ============================================================
# Lista Enlazada Simple
# ============================================================

class SinglyLinkedList:
    def __init__(self):
        self.head = None    # Primer nodo
        self.tail = None    # Último nodo (para insertar rápido al final)

    def insert_start(self, value):
        # Inserta un nodo al inicio (O(1))
        node = Node(value)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node

    def insert_end(self, value):
        # Inserta un nodo al final (O(1) gracias a tail)
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove_start(self):
        # Elimina el primer nodo (O(1))
        if self.head:
            self.head = self.head.next
            if not self.head:
                self.tail = None

    def remove_end(self):
        # Elimina el último nodo (O(n) porque hay que recorrer)
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
        # Acceso por índice (O(n))
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data


# ============================================================
# Lista Enlazada Doble
# ============================================================

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, value):
        # Inserta al inicio (O(1))
        node = Node(value)
        if self.head:
            node.next = self.head
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def insert_end(self, value):
        # Inserta al final (O(1))
        node = Node(value)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        else:
            self.head = node
        self.tail = node

    def remove_start(self):
        # Elimina el primer nodo (O(1))
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

    def remove_end(self):
        # Elimina el último nodo (O(1))
        if not self.tail:
            return
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

    def get(self, index):
        # Acceso por índice (O(n))
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data


# ============================================================
# FUNCIÓN BENCHMARK
# ============================================================
# Ejecuta N operaciones y mide cuánto tiempo toma cada una
# en las distintas estructuras de datos.

def benchmark(N):
    # Lista de índices aleatorios para simular accesos reales
    indices = [random.randint(0, N - 1) for _ in range(N)]

    # Diccionario para almacenar los resultados
    results = {}

    # =======================
    # ARREGLOS (listas Python)
    # =======================

    arr = []
    start = time.time()
    for i in range(N):
        arr.insert(0, i)   # Insertar al inicio (lento)
    results["Array - Insertar al inicio"] = time.time() - start

    arr = []
    start = time.time()
    for i in range(N):
        arr.append(i)     # Insertar al final (rápido)
    results["Array - Insertar al final"] = time.time() - start

    start = time.time()
    for _ in range(N):
        arr.pop(0)        # Eliminar al inicio (lento)
    results["Array - Eliminar al inicio"] = time.time() - start

    arr = list(range(N))
    start = time.time()
    for _ in range(N):
        arr.pop()         # Eliminar al final (rápido)
    results["Array - Eliminar al final"] = time.time() - start

    arr = list(range(N))
    start = time.time()
    for i in indices:
        _ = arr[i]        # Acceso directo por índice (O(1))
    results["Array - Acceso por índice"] = time.time() - start

    # =======================
    # LISTA ENLAZADA SIMPLE
    # =======================

    sll = SinglyLinkedList()
    start = time.time()
    for i in range(N):
        sll.insert_start(i)
    results["Lista simple - Insertar al inicio"] = time.time() - start

    sll = SinglyLinkedList()
    start = time.time()
    for i in range(N):
        sll.insert_end(i)
    results["Lista simple - Insertar al final"] = time.time() - start

    start = time.time()
    for _ in range(N):
        sll.remove_start()
    results["Lista simple - Eliminar al inicio"] = time.time() - start

    sll = SinglyLinkedList()
    for i in range(N):
        sll.insert_end(i)
    start = time.time()
    for _ in range(N):
        sll.remove_end()
    results["Lista simple - Eliminar al final"] = time.time() - start

    sll = SinglyLinkedList()
    for i in range(N):
        sll.insert_end(i)
    start = time.time()
    for i in indices:
        _ = sll.get(i)
    results["Lista simple - Acceso por índice"] = time.time() - start

    # =======================
    # LISTA ENLAZADA DOBLE
    # =======================

    dll = DoublyLinkedList()
    start = time.time()
    for i in range(N):
        dll.insert_start(i)
    results["Lista doble - Insertar al inicio"] = time.time() - start

    dll = DoublyLinkedList()
    start = time.time()
    for i in range(N):
        dll.insert_end(i)
    results["Lista doble - Insertar al final"] = time.time() - start

    start = time.time()
    for _ in range(N):
        dll.remove_start()
    results["Lista doble - Eliminar al inicio"] = time.time() - start

    dll = DoublyLinkedList()
    for i in range(N):
        dll.insert_end(i)
    start = time.time()
    for _ in range(N):
        dll.remove_end()
    results["Lista doble - Eliminar al final"] = time.time() - start

    dll = DoublyLinkedList()
    for i in range(N):
        dll.insert_end(i)
    start = time.time()
    for i in indices:
        _ = dll.get(i)
    results["Lista doble - Acceso por índice"] = time.time() - start

    # =======================
    # MOSTRAR RESULTADOS
    # =======================

    print(f"\n--- BENCHMARK ({N} operaciones) ---")
    for k, v in results.items():
        # Muestra el nombre de la operación y el tiempo en segundos
        print(f"{k:40} {v:.6f} s")


# ============================================================
# EJECUCIÓN DEL EJERCICIO 19
# ============================================================

print("\n=== EJERCICIO 19 ===")
benchmark(1000)   # Resultado original
benchmark(100)    # Resultado 1
benchmark(5000)   # Resultado 2
benchmark(1000)   # Resultado 3



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

"""