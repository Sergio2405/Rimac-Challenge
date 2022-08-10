# Rimac Challenge
## Descripción

Repositorio que crea un api para un modelo que predice la probabilidad de tener una enfermedad cardiaca.

## Guía de Usuario

### Instalar paquetes

1. Crear un entorno virtual para instalar los requerimientos
```bash
virtualenv challenge
```
2. Activar el entorno virtual
```bash
challenge\Scripts\activate
```
3. Luego se instalan los requerimientos
```bash
pip install -r requirements.txt
```
### Deployar api y Testearlo
1. Asegurarse de estar en el directorio donde esta el app y abra 2 consolas
2. En la **primera consola** despligue localmente el api con el siguiente comando
```bash
uvicorn app.api:app --reload --port 8001
```
3. Una vez desplegado el api abra la **segunda consola** para realizar el testeo
```bash
curl -d @./tests/example1.json -H "Content-Type: application/json" -X POST http://127.0.0.1:8001/predict
```
4. El api le debería retornar un objeto json `{"prob" : 0.9}`
