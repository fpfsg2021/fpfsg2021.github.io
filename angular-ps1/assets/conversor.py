import json

if __name__ == "__main__":
    print("Iniciando conversión...")
    ljuegos = []
    with open("gameboy_covers_original.json", encoding="UTF-8") as file:
        juegos = file.read()
        jjuegos = json.loads(juegos)
        for value in jjuegos.values():
            juego = {"name":value[0],"cover":value[1]}
            ljuegos.append(juego)
    with open("gameboy_covers.json", mode="w", encoding="UTF-8") as file:
        file.write(json.dumps(ljuegos))