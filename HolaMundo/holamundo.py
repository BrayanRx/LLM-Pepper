import qi

def main():
    # IP y puerto del robot Pepper
    pepper_ip = "172.17.198.140"  # Cambia esto por la IP de tu robot
    pepper_port = 9559

    # Crear una conexion con el robot
    session = qi.Session()
    try:
        session.connect("tcp://" + pepper_ip + ":" + str(pepper_port))
        tts = session.service("ALTextToSpeech")
    except Exception as e:
        print("Error al conectar con el robot:", e)
        return

    # Decir "Hola Mundo"
    try:
        tts.say("Hola soy Pepper")
        print("Pepper dijo: Hola soy Pepper")
    except Exception as e:
        print("Error al hacer que Pepper diga 'Hola soy Pepper':", e)

if __name__ == "__main__":
    main()

