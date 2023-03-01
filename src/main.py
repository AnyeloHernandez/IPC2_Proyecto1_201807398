from models import ListaEnlazada
from tkinter import Tk
from tkinter.filedialog import askopenfile

def load_file():
    print("Test")
    Tk().withdraw()
    path = askopenfile()
    file = open(path, 'r')

def menu():
    while True:
        print('==== Menu Principal ====')
        print('1. Cargar Archivo')
        print('2. Procesar Archivo')
        print('3. Generar gráfica')
        print('4. Salir')
        option = input('Seleccione una opción: ')

        if option == '1':
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            exit()
        else:
            print("Elija una opción válida. ")


if __name__ == '__main__':
    menu()