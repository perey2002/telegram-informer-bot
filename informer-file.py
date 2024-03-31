import sys
import requests

# Token de tu bot de Telegram
TOKEN = 'your bot token'

# ID del grupo al que quieres enviar mensajes (debes usar el ID numérico, no el nombre)
GROUP_ID = 'your group id'

# URL base para enviar mensajes a través de la API de Telegram
TELEGRAM_API_URL = 'https://api.telegram.org/bot' + TOKEN + '/sendDocument'

def enviar_archivo(archivo):
    try:
        with open(archivo, 'rb') as file:
            files = {'document': file}
            params = {'chat_id': GROUP_ID}
            response = requests.post(TELEGRAM_API_URL, files=files, data=params)
            if response.status_code == 200:
                print("Archivo enviado al grupo de Telegram exitosamente.")
            else:
                print("Error al enviar el archivo. Código de estado:", response.status_code)
    except Exception as e:
        print("Ocurrió un error al enviar el archivo:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, proporciona la ruta del archivo para enviar.")
        sys.exit(1)

    archivo = sys.argv[1]
    enviar_archivo(archivo)
