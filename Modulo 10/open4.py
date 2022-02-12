def main():
    try:
        configuration = open("config2.txt")
    except FileNotFoundError:
        print("No se pudo encontrar el archivo config.txt")
    except IsADirectoryError:
        print("config2.txt es un directorio, no puedo leerlo")

if __name__ == '__main__':
    main()