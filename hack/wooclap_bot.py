import time
import pyautogui

## Intento de bot para responder preguntas en Wooclap

def tomar_captura():
    """Toma captura de la pregunta en la pantalla"""
    screenshot = pyautogui.screenshot()
    screenshot.save("pregunta.png")
    return "pregunta.png"


def extraer_texto(imagen):
    """Extrae texto de la imagen usando OCR (simulado con texto fijo)"""
    return "Pregunta de ejemplo: ¿Cuál es la capital de Francia?"


def seleccionar_respuesta():
    """Busca la respuesta en la pantalla y hace clic en ella"""
    # Aquí, debes tener una imagen que corresponda con una respuesta.
    # Asumimos que las respuestas son imágenes con nombres como 'respuesta1.png', 'respuesta2.png', etc.

    # Busca la imagen de la respuesta correcta en la pantalla (esto depende de las imágenes de respuesta que tengas)
    respuesta_img = pyautogui.locateCenterOnScreen("respuesta_paris.png",
                                                   confidence=0.8)  # Cambia "respuesta_paris.png" por la imagen correspondiente

    if respuesta_img:
        print(f"Respuesta encontrada en: {respuesta_img}")
        pyautogui.click(respuesta_img)
    else:
        print("No se encontró la respuesta en la pantalla.")


def validar_respuesta():
    """Busca el botón de validar y lo presiona"""
    # Busca el botón "Enviar" (ajusta la imagen según el botón que tengas en la interfaz)
    boton_validar = pyautogui.locateCenterOnScreen("boton_enviar.png",
                                                   confidence=0.8)  # Cambia "boton_enviar.png" por la imagen del botón "Enviar"

    if boton_validar:
        print(f"Botón 'Enviar' encontrado en: {boton_validar}")
        pyautogui.click(boton_validar)
    else:
        print("No se encontró el botón 'Enviar'.")


def main():
    tiempo_total = 10  # Ajusta según el tiempo de la pregunta
    tiempo_validar = tiempo_total - 5

    print("Esperando para validar...")
    time.sleep(2)

    print("Tomando captura...")
    imagen = tomar_captura()

    print("Extrayendo texto...")
    pregunta = extraer_texto(imagen)

    print(f"Pregunta extraída: {pregunta}")

    print("Seleccionando respuesta...")
    seleccionar_respuesta()

    print("Esperando para validar...")
    time.sleep(tiempo_validar)

    print("Validando respuesta...")
    validar_respuesta()


if __name__ == "__main__":
    main()
