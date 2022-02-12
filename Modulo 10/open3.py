def main():
    try:
        configuration = open("config3.txt")
    except Exception:
        print("No se pudo encontrar el archivo config.txt")

if __name__ == '__main__':
    main()