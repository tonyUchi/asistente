import datetime
import json
import os
import uuid 

ARCHIVO_JSON = "log_sesiones.json"

def guardar_log_json(session_id, usuario_msg, respuesta_asistente):
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entrada = {
        "timestamp": fecha_hora,
        "usuario": usuario_msg,
        "asistente": respuesta_asistente
    }


    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}

    if session_id not in data:
        data[session_id] = []

    data[session_id].append(entrada)

    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def cargar_sesion(session_id):
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
        if session_id in data:
            print("interacción pasada")
            for entrada in data[session_id]:
                print(f"[{entrada['timestamp']}] Usuario: {entrada['usuario']}")
                print(f"[{entrada['timestamp']}] Asistente: {entrada['asistente']}")
            print("-" * 50)
        else:
            print("--- Nueva sesión iniciada ---")
    else:
        print("--- No hay sesiones previas ---")


#aqui defino las reglas, pero ya que no me pidieron muchas, solo puse las que ustedes me propusieron
def asistente_soporte():
    reglas = {
        "hola": "¡Hola! Soy tu asistente de soporte. ¿Cómo puedo ayudarte?",
        "consulta": "¿En qué puedo ayudarte con tu consulta?",
        "problema": "¿Que problema estas presentando?",
        "adios": "¡Hasta pronto!"
    }

    session_id = str(uuid.uuid4())

    print(f"--- Sesión: {session_id}) ---")
    cargar_sesion(session_id)

    while True:
        entrada = input("\nUsuario: ")
        usuario_msg = entrada.lower().strip()

        if usuario_msg in ["salir"]:
            print("Asistente: Disculpa si no pude ayudarte!!!")
            break

        respuesta = "Lo siento solo soy un asistente de prueba para tech company, no puedo ayudarte mas."
        for palabra, msg_soporte in reglas.items():
            if palabra in usuario_msg:
                respuesta = msg_soporte
                break

        print(f"Asistente: {respuesta}")
        guardar_log_json(session_id, entrada, respuesta)

if __name__ == "__main__":
    asistente_soporte()