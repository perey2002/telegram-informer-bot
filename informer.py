import sys
import requests

# Token de tu bot de Telegram
TOKEN = 'your bot token'

# ID del grupo al que quieres enviar mensajes (debes usar el ID numérico, no el nombre)
GROUP_ID = 'your group id'

# URL base para enviar mensajes a través de la API de Telegram
TELEGRAM_API_URL = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage'

def enviar_mensaje(mensaje):
    # Parámetros del mensaje
    params = {
        'chat_id': GROUP_ID,
        'text': mensaje
    }

    # Enviar el mensaje utilizando la API de Telegram
    try:
        response = requests.post(TELEGRAM_API_URL, params=params)
        if response.status_code == 200:
            print("Mensaje enviado al grupo de Telegram exitosamente.")
        else:
            print("Error al enviar el mensaje. Código de estado:", response.status_code)
    except Exception as e:
        print("Ocurrió un error al enviar el mensaje:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, proporciona un mensaje para enviar.")
        sys.exit(1)

    mensaje = ' '.join(sys.argv[1:])
    enviar_mensaje(mensaje)
