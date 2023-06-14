# PIP

Para verificar que version de pip esta instalada en nuestro entorno de trabajo utilice el siguiente comando:

```bash
pip -V
```

Para instalar una dependencia a traves de pip utilice el siguiente comando:

```bash
pip install <nombre_dependencia>
```

Para instalar una version especifica de una dependencia, utilice el siguiente comando

```bash
pip install <nombre_dependencia>==<version>
```

Para desinstalar una dependencia a traves de pip utilice el siguiente comando:

```bash
pip uninstall <nombre_dependencia>
```

Para listar las dependencias instaladas en nuestro entorno de trabajo utilice el siguiente comando:

```bash
pip freeze
```

# Ambientes virtuales

Para instalar el modulo de ambientes virtuales utilice el siguiente comando:

```bash
sudo apt install -y python3-venv
```

Para crear un ambiente virtual utilice el siguiente comando:

```bash
python -m venv <nombre_ambiente_virtual>
```

Para activar el ambiente virtual, utilice el siguiente comando:

```bash
source env/bin/activate
```

Para desactivar el ambiente virtual, utilice el siguiente comando:

```bash
deactivate
```

# requirements.txt
Puedes generar el archivo requirements.txt con el siguiente comando:

```bash
pip3 freeze > requirements.txt
```

Para revisar lo que hay dentro del archivo

```bash
cat requirements.txt
```

## Flujo de trabajo en python
```bash
git clone
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

# Docker y python
1. Crear un archivo llamado Dockerfile
2. Dentro de este archivo, escribir las instrucciones para crear la imagen

```bash
FROM python:3.8

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD bash -c "while true; do sleep 1; done"
```

3. Crear el archivo docker-compose.yml

```bash
version: "3.8"

services:
  app:
    build:
        context: .
        dockerfile: Dockerfile
    volumes:
        - .:/app
```

4. Crear la imagen

```bash
docker-compose build
```

5. Correr la imagen

```bash
docker-compose up
```

6. Para verificar que la imagen esta corriendo

```bash
docker-compose ps
```

7. Para acceder a la consola de la imagen

```bash
docker-compose exec app bash
```

8. Para detener la imagen

```bash
docker-compose down
```






