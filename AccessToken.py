import base64
import requests

client_id = "808fe35cc2ca479c8ae6c0a4619eedf4"
client_secret = "a14b06f0e1f84376925b6c98ad3478f7"

# Codificar las credenciales en Base64
credentials = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")

# Configurar los parámetros de la solicitud POST
payload = {
    "grant_type": "client_credentials"
}

headers = {
    "Authorization": f"Basic {credentials}"
}

# Realizar la solicitud POST
response = requests.post("https://accounts.spotify.com/api/token", data=payload, headers=headers)

# Obtener el token de acceso de la respuesta
access_token = response.json()["access_token"]
print(f"Token de acceso: {access_token}")
