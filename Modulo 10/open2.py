def main():
    try:
        configuration = open("config2.txt")
    except FileNotFoundError:
        print("No se pudo encontrar el archivo config.txt")

if __name__ == '__main__':
    main()