class Nodo:
    def __init__(self, data):
        self.item = data
        self.ref = None


class List:
    def __init__(self):
        #  Inicia el nodo
        self.start_node = None

    #  Para moverse por la lista
    def traverse_list(self):
        #  Si el primer elemento es null, se entiende que esta vacio el resto
        if self.start_node is None:
            print("Esta vacia")
            return
        else:
            #  Sino recorre el nodo y muestra en consola su contenido
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Nodo(data) #  Ingresa datos en el nodo desde el principio
        new_node.ref = self.start_node
        self.start_node = new_node #  Pide memoria

    def delete_at_start(self):
        if self.start_node is None:
            print("La lista no tiene elementos a eliminar")
            return
        # Elimina toda la lista volviendo el inicio como None
        self.start_node = self.start_node.ref