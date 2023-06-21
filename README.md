## **Guía paso a paso para realizar una ETL con Power Query y obtener información de artistas de Spotify**
En esta guía, aprenderemos a realizar una ETL (Extracción, Transformación y Carga) utilizando Power Query en Microsoft Excel o Power BI para obtener información de artistas de Spotify a través de su API. Seguiremos los siguientes pasos:
### **1. Registro en Spotify Developer Dashboard**
- Para comenzar, registrémonos en el Spotify Developer Dashboard (<https://developer.spotify.com>) para obtener nuestras credenciales de API.
### **2. Crear una nueva aplicación**
- Una vez registrados y en el Dashboard, creemos una nueva aplicación haciendo clic en el botón "Crear una nueva aplicación".
- Asignemos un nombre y descripción a nuestra aplicación, por ejemplo:
  - App name: ETL Spotify
  - App description: ETL Spotify
- En el campo "Redirect URIs", ingresamos la siguiente URL:
  - Redirect URIs: [http://localhost:3000](http://localhost:3000/)

![Interfaz de usuario gráfica, Texto Descripción generada automáticamente](Aspose.Words.6be16035-2bd3-4526-8fba-30f7129950cf.001.png)
### **3. Obtener las credenciales de la aplicación**
- Después de crear la aplicación, copiemos el "Client ID" y el "Client secret". Los necesitaremos más adelante.

![](Aspose.Words.6be16035-2bd3-4526-8fba-30f7129950cf.002.png)
### **4. Obtener el Access Token mediante Python**
- Descarguemos el archivo "AccessToken.py" proporcionado y ejecutémoslo.
- Ingresamos el "Client ID" y el "Client secret" cuando se solicite.
- El script de Python nos devolverá el Access Token. Copiemos este valor, ya que lo utilizaremos en los pasos siguientes.

![Texto Descripción generada automáticamente](Aspose.Words.6be16035-2bd3-4526-8fba-30f7129950cf.003.png)
### **5. Preparar el comando cURL**
- Para obtener información de un artista específico en Spotify, utilizaremos el endpoint "search" de la API.
- Supongamos que queremos obtener información sobre el artista "Maluma". Podemos usar el siguiente comando cURL como ejemplo:

curl --request GET \

`  `--url 'https://api.spotify.com/v1/search?q=Maluma&type=artist&limit=1' \

`  `--header 'Authorization: Bearer BQCmRAInjP5RTA3qHIhThy6dr5VsyHWYHbZhyWAFr-LKxjERGhCji2jCDki\_GOV6wxo2ZrUMjLQHcXZ-Wn5f-33M9s8kcY2RViCab37iKCSmca0ys38'

- Reemplaza el token de acceso después de "Bearer" con el Access Token obtenido del script de Python.

![](Aspose.Words.6be16035-2bd3-4526-8fba-30f7129950cf.004.png)
### **6. Guardar el Access token como parámetro**
![](Aspose.Words.6be16035-2bd3-4526-8fba-30f7129950cf.005.png)
### **7. Preparar los datos de entrada**
- Crea una lista de artistas colombianos en una nueva tabla y nómbrala **“Datos de entrada”** donde cada artista esté en una nueva línea.

![Interfaz de usuario gráfica, Aplicación, Tabla

Descripción generada automáticamente](Aspose.Words.6be16035-2bd3-4526-8fba-30f7129950cf.006.png)
### **8. Crear la función en Power Query**
- Abre Power Query, crea una nueva consulta y abre el editor avanzado.
- Copia el siguiente código:

(Artistname as text) =>

let

`    `Source = Json.Document(

`        `Web.Contents("https://api.spotify.com/v1/search?q="&Artistname&"&type=artist&limit=1",

`            `[Headers=

`                `[

`                    `Authorization=#"Authorization Bearer"

`                `]

`            `]

`        `)

`    `)

in

`    `Source

- Dale un nombre a la función, por ejemplo:
  - Nombre de la consulta: **“Func\_Obtener\_Artista”**

![](Aspose.Words.6be16035-2bd3-4526-8fba-30f7129950cf.007.png)
### **9. Invocar la función de obtención de información del artista**
- Crear una referencia de **“Datos de entrada”** y nombra esta nueva tabla como **“Spotify Artistas”**
- En la tabla **“Spotify Artistas”** agrega una nueva columna llamada **"Spotify\_Artista"** utilizando la opción "Agregar columna invocada como función".
- En la invocación de la función, utiliza la función **"Func\_Obtener\_Artista"** y establece la columna "Artista" como parámetro.
- Expande todas las columnas en la salida de la función.
- Eliminar las columnas que no necesitas
- Asigna a cada columna el tipo de datos que debe tener

![](Aspose.Words.6be16035-2bd3-4526-8fba-30f7129950cf.008.png)
### **10. Organizar las consultas en carpetas**
- Crea grupos de carpetas en Power Query para organizar las consultas. Por ejemplo, crea carpetas para **"Parámetros", "Data de entrada", "Funciones" y "Datos de salida".**

![Aplicación

Descripción generada automáticamente con confianza media](Aspose.Words.6be16035-2bd3-4526-8fba-30f7129950cf.009.png)

¡Felicitaciones! Has completado una ETL utilizando Power Query para obtener información de artistas de Spotify. Ahora puedes utilizar estos datos para análisis, visualizaciones o cualquier otro propósito necesario.

