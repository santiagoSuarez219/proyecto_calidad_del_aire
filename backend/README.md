# Creacion del proyecto

1. Crear carpeta del proyecto
2. Iniciar un proyecto de nodejs con el comando 
```bash
npm init
```
3. Iniciar el repositorio de git con el comando 
```bash
git init
```
4. Crear el archivo .gitignore y agregar los archivos que no se quieren subir al repositorio
5. Crear la carpeta src y dentro de ella el archivo index.js
6. Modificar el archivo package.json para agregar los script de start
```json
"scripts": {
    "dev": "nodemon src/index.js",
    "start": "node src/index.js",
  },
```
7. Instalar las dependencias necesarias para el proyecto
```bash
npm i nodemon express
```

8. Para correr el programa utilice
```bash
npm run dev
```

# Servidor HTTP con Express JS
1. Instalar Express
```bash
npm i express
```
2. En el archivo src/index.js implemente el siguiente codigo

```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/',(req,res) =>{
  res.send('Hello World');
});

app.listen(port, () => {
  console.log('Mi port' + port);
});
```




