# telegram-informer-bot
![alt text](img/Informer.png)
# telegram-informer-bot
![UK FLAG](https://upload.wikimedia.org/wikipedia/commons/f/fc/Flag_of_Great_Britain_%28English_version%29.png){width=150px}
**Telegram Informer Bot**

This Python script serves as a Telegram bot to send messages or files to a specific group on Telegram using the Telegram API.

### Usage

1. **Get your Telegram bot token:**
   - Create a new bot on Telegram using the BotFather (https://core.telegram.org/bots#6-botfather).
   - Copy the access token provided by BotFather and paste it into the `TOKEN` variable in the script.

2. **Get the numeric ID of your Telegram group:**
   - Add your bot to the Telegram group where you want to send messages or files.
   - Send any message to the group, then visit the following URL in your web browser: `https://api.telegram.org/bot<TOKEN>/getUpdates` (replace `<TOKEN>` with your bot's token).
   - Look for the JSON object containing the chat ID of the group. This numeric ID is what you'll use for the `GROUP_ID` variable in the script.

3. **Sending Messages:**
   - Run the script with the message you want to send as an argument.
   - Example: `python script_name.py "Your message here"`
   - The script will send the specified message to the designated Telegram group.

4. **Sending Files:**
   - Use the `telegram_file_sender.py` script to send files.
   - Execute the script with the path of the file you want to send as an argument.
   - Example: `python telegram_file_sender.py /path/to/your/file`
   - Ensure the file path is correct and the file exists.
   - The script will send the specified file to the designated Telegram group.

Español
# telegram-informer-bot
![ES FLAG](https://upload.wikimedia.org/wikipedia/commons/6/6f/Spain_flag_300.png){width=150px}
**Bot Informador de Telegram**

Este script en Python sirve como un bot de Telegram para enviar mensajes o archivos a un grupo específico en Telegram utilizando la API de Telegram.

### Uso

1. **Obtener el token de tu bot de Telegram:**
   - Crea un nuevo bot en Telegram usando BotFather (https://core.telegram.org/bots#6-botfather).
   - Copia el token de acceso proporcionado por BotFather y pégalo en la variable `TOKEN` en el script.

2. **Obtener el ID numérico de tu grupo de Telegram:**
   - Agrega tu bot al grupo de Telegram donde deseas enviar mensajes o archivos.
   - Envía cualquier mensaje al grupo, luego visita la siguiente URL en tu navegador web: `https://api.telegram.org/bot<TOKEN>/getUpdates` (reemplaza `<TOKEN>` con el token de tu bot).
   - Busca el objeto JSON que contiene el ID de chat del grupo. Este ID numérico es lo que usarás para la variable `GROUP_ID` en el script.

3. **Enviar Mensajes:**
   - Ejecuta el script con el mensaje que deseas enviar como argumento.
   - Ejemplo: `python nombre_del_script.py "Tu mensaje aquí"`
   - El script enviará el mensaje especificado al grupo de Telegram designado.

4. **Enviar Archivos:**
   - Utiliza el script `telegram_file_sender.py` para enviar archivos.
   - Ejecuta el script con la ruta del archivo que deseas enviar como argumento.
   - Ejemplo: `python telegram_file_sender.py /ruta/a/tu/archivo`
   - Asegúrate de que la ruta del archivo sea correcta y que el archivo exista.
   - El script enviará el archivo especificado al grupo de Telegram designado.


Français
# telegram-informer-bot
![FR FLAG](https://upload.wikimedia.org/wikipedia/commons/6/62/Flag_of_France.png){width=150px}
**Bot Informateur de Telegram**

Ce script Python sert de bot Telegram pour envoyer des messages ou des fichiers à un groupe spécifique sur Telegram en utilisant l'API de Telegram.

### Utilisation

1. **Obtenez le jeton de votre bot Telegram :**
   - Créez un nouveau bot sur Telegram en utilisant BotFather (https://core.telegram.org/bots#6-botfather).
   - Copiez le jeton d'accès fourni par BotFather et collez-le dans la variable `TOKEN` dans le script.

2. **Obtenez l'identifiant numérique de votre groupe Telegram :**
   - Ajoutez votre bot au groupe Telegram où vous souhaitez envoyer des messages ou des fichiers.
   - Envoyez n'importe quel message au groupe, puis rendez-vous à l'URL suivante dans votre navigateur web : `https://api.telegram.org/bot<TOKEN>/getUpdates` (remplacez `<TOKEN>` par le jeton de votre bot).
   - Recherchez l'objet JSON contenant l'identifiant de chat du groupe. Cet identifiant numérique est ce que vous utiliserez pour la variable `GROUP_ID` dans le script.

3. **Envoyer des Messages :**
   - Exécutez le script avec le message que vous souhaitez envoyer en tant qu'argument.
   - Exemple : `python nom_du_script.py "Votre message ici"`
   - Le script enverra le message spécifié au groupe Telegram désigné.

4. **Envoyer des Fichiers :**
   - Utilisez le script `telegram_file_sender.py` pour envoyer des fichiers.
   - Exécutez le script avec le chemin du fichier que vous souhaitez envoyer en tant qu'argument.
   - Exemple : `python telegram_file_sender.py /chemin/vers/votre/fichier`
   - Assurez-vous que le chemin du fichier est correct et que le fichier existe.
   - Le script enverra le fichier spécifié au groupe Telegram désigné.
# telegram-informer-bot
![alt text](img/image.png)