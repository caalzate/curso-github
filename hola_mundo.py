import os

def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde GitHub actions 2da ejecucion!")

if __name__ == "__main__":
    main()
