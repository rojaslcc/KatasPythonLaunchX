def main():
    try:
        configuration = open("config3.txt")
    except FileNotFoundError:
        print("No se pudo encontrar el archivo config.txt")
    except IsADirectoryError:
        print("config3.txt es un directorio, no puedo leerlo")
    except (BlockingIOError, TimeoutError, PermissionError):
        print("Error de lectura, revisar permisos")

if __name__ == '__main__':
    main()